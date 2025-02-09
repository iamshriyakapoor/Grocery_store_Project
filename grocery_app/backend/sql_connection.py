import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

# Load environment variables from .env file
load_dotenv()

__cnx = None

def get_sql_connection():
    global __cnx
    try:
        __cnx = mysql.connector.connect(
            user=os.getenv("DB_USER"),
            host=os.getenv("DB_HOST"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        if __cnx.is_connected():
            print("Successfully connected to the database")
    except Error as e:
        print("Error while connecting to MySQL", e)
    return __cnx
