import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv
import time

time.sleep(20)
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

create_users ="""
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
"""

create_marcs = """
CREATE TABLE IF NOT EXISTS marcs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user INT,
    datetime DATETIME,
    type VARCHAR(255),
    FOREIGN KEY (user) REFERENCES users(id)
)
"""

create_report = """
CREATE TABLE IF NOT EXISTS report (
    id INT AUTO_INCREMENT PRIMARY KEY,
    datetime DATETIME,
    status VARCHAR(25)
    )"""

create_results ="""
CREATE TABLE IF NOT EXISTS result (
    id INT AUTO_INCREMENT PRIMARY KEY,
    json_data JSON)"""

try:
    connection = mysql.connector.connect(user=db_config["user"],password=db_config["password"],host=db_config["host"])
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute(create_database)
        cursor.execute(use_database)
        cursor.execute(create_users)
        cursor.execute(create_marcs)
        cursor.execute(create_report)
        cursor.execute(create_results)
        connection.commit()
        print("Habemus Tablas.")
except Error as e:
    print("Error:", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexión cerrada.")
