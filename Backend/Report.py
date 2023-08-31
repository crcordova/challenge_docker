import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv
import pandas as pd
import time

time.sleep(20)
load_dotenv()
db_config = {
    "host": os.getenv('host','localhost'),
    "user": os.getenv('user',"root"),
    "password": os.getenv('pass'),
    "bd":os.getenv("bd","Challenge")
}
use_database = f"USE {db_config['bd']}"
try:
    connection = mysql.connector.connect(
        user=db_config["user"],
        password=db_config["password"],
        host=db_config["host"], 
        database=db_config['bd']
        )
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute(use_database)
        cursor.execute("SELECT * FROM report")
        column_names = [d[0] for d in cursor.description]
        results = cursor.fetchall()
        df_results = pd.DataFrame(results, columns=column_names)
        df_results = df_results[df_results['status']=='incomplete']
        if df_results.empty == False:
            id_report = int(df_results['id'].values[0])
            cursor.execute("SELECT * FROM marcs")
            results = cursor.fetchall()
            column_names = [d[0] for d in cursor.description]
            df_marcs = pd.DataFrame(results, columns=column_names)
            df_marcs['date'] = df_marcs['datetime'].dt.date
            df_in = df_marcs[df_marcs['type']=='In']
            df_out = df_marcs[df_marcs['type']=='Out']
            df = pd.merge(df_in, df_out, on=['user','date'], how='inner',suffixes=('_in','_out'))[['user','datetime_in','datetime_out','date']]
            df['time'] = df['datetime_out'] - df['datetime_in']
            print('procesando reporte')
            df_json = df.to_json(orient="records")
            valores = (df_json,)
            valor_upt = (id_report,)
            query_insert = "INSERT INTO result (json_data) VALUES (%s)"
            query_update = "UPDATE report SET status = 'complete' WHERE id = %s"
            cursor.execute(query_insert, valores)
            cursor.execute(query_update, valor_upt)
            connection.commit()
            print('reporte creado')
        else:
            print('no hay reportes pendientes')

    cursor.close()
    connection.close()
    print("Conexión cerrada.")

except Error as e:
    print("Error:", e)
