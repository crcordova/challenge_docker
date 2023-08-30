import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()
# Configuración de la conexión a la base de datos
db_config = {
    "host": os.getenv('host','localhost'),
    "user": os.getenv('user',"root"),
    "password": os.getenv('pass'),
    "bd":os.getenv("bd","Challenge")
}

create_database = f"CREATE DATABASE IF NOT EXISTS {db_config['bd']}"
use_database = f"USE {db_config['bd']}"

# Consulta para crear la tabla
create_users ="""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    password VARCHAR(255)
)"""

create_marcs = """
CREATE TABLE IF NOT EXISTS Marcs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user INT,
    datetime DATETIME,
    type VARCHAR(255),
    FOREIGN KEY (user) REFERENCES users(id)
)
"""

try:
    connection = mysql.connector.connect(user=db_config["user"],password=db_config["password"],host=db_config["host"], port=3306)
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute(create_database)
        cursor.execute(use_database)
        cursor.execute(create_users)
        cursor.execute(create_marcs)
        connection.commit()
        print("Habemus Tablas.")
except Error as e:
    print("Error:", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexión cerrada.")
