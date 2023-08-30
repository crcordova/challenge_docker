from datetime import datetime
from dotenv import load_dotenv
import os
import mysql.connector
from mysql.connector import Error
from pandas import DataFrame, to_datetime
import json

def create_report():
    now = datetime.now()
    status='incomplete'
    load_dotenv()
    db_config = {
        "host": os.getenv('host','localhost'),
        "user": os.getenv('user',"root"),
        "password": os.getenv('pass'),
        "bd":os.getenv("bd","Challenge")
    }
    use_database = f"USE {db_config['bd']}"
    query =  """
            INSERT INTO report (datetime, status)
            VALUES (%s, %s)
        """
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
            cursor.execute(query, (now, status))
            connection.commit()
            cursor.close()
            connection.close()
    
    except Error as e:
            print("Error:", e)

def download_report():
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
            cursor.execute("SELECT * FROM result ORDER BY id DESC LIMIT 1")

            # Obtener el resultado de la consulta
            resultado = cursor.fetchone()

            if resultado:

                data_dict = json.loads(resultado[1])
                
                # Crear un DataFrame a partir del diccionario
                df = DataFrame(data_dict)
                for r in ['date','time','datetime_in','datetime_out']:
                    df[r]=to_datetime(df[r], unit='ms')
                df['time'] = df['time'].dt.minute/60
                return df

    except Error as e:
        print("Error:", e)