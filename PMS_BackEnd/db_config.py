import pymysql
import traceback

def get_connection():
    print("Connecting to MySQL using pymysql...")
    try:
        connection = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            database="bg_database",
            connect_timeout=5,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("Connection established (pymysql).")
        return connection
    except Exception as e:
        print("pymysql connection failed:")
        traceback.print_exc()
        raise