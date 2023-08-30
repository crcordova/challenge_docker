import mysql.connector
from mysql.connector import Error
import os
from pandas import DataFrame
from dotenv import load_dotenv
from datetime import datetime

def tests_connection():
    load_dotenv()
    db_config = {
        "host": os.getenv('host','localhost'),
        "user": os.getenv('user',"root"),
        "password": os.getenv('pass'),
        "bd":os.getenv("bd","Challenge")
    }
    print(db_config)
    try:
        connection = mysql.connector.connect(
            user=db_config["user"],
            password=db_config["password"],
            host=db_config["host"], 
            database=db_config['bd']
            )
        return{'conected':db_config}
    except:
        return { "Error":db_config}

class Users:
    def __init__(self) -> None:
        load_dotenv()
        db_config = {
            "host": os.getenv('host','localhost'),
            "user": os.getenv('user',"root"),
            "password": os.getenv('pass'),
            "bd":os.getenv("bd","Challenge")
        }
        use_database = f"USE {db_config['bd']}"
        try:
            self.connection = mysql.connector.connect(
                user=db_config["user"],
                password=db_config["password"],
                host=db_config["host"], 
                database=db_config['bd']
                )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                self.cursor.execute(use_database)
        except Error as e:
            print("Error:", e)

    def create(self,name, email, pasw):
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
        insert_query = """
            INSERT INTO users (name, email, password)
            VALUES (%s, %s, %s)
        """
        self.cursor.execute(insert_query, (name, email, pasw))
        self.connection.commit()
        self.cursor.close()
        self.connection.close()