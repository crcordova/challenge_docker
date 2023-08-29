import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv
import pandas as pd

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
        cursor.execute("SELECT * FROM Marcs")
        column_names = [d[0] for d in cursor.description]
        results = cursor.fetchall()
        results = pd.DataFrame(results)


except Error as e:
    print("Error:", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexión cerrada.")