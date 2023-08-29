import mysql.connector
from mysql.connector import Error
import os
from pandas import DataFrame
from dotenv import load_dotenv
from datetime import datetime

class Marcs:
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

    def get_all_marcs(self):
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM Marcs")
        column_names = [d[0] for d in self.cursor.description]
        results = self.cursor.fetchall()
        print(results)
        results = DataFrame(results).to_dict()

        return results
    
    def verify_user_last_marc(self, tipo):
        return True
    
    def create_marc(self,id_user, tipo ):
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
        now = datetime.now()
        # verify_user_last_marc(self)
        insert_query = """
            INSERT INTO Marcs (user, datetime, type)
            VALUES (%s, %s, %s)
        """
        self.cursor.execute(insert_query, (id_user, now, tipo))
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def delete_marc(self, id_user, tipo):
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
        delete_= """
            DELETE FROM Marcs
            WHERE user = %s AND type = %s
        """
        self.cursor.execute(delete_, (id_user, tipo))
        self.connection.commit()
        self.cursor.close()
        self.connection.close()