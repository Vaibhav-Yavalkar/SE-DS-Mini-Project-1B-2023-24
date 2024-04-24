import mysql.connector

def db_connect():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mane2004@",
            database="hospital"
        )
        print("Connected to MySQL database")
        return conn
    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)
        return None

if __name__ == "__main__":
    db_connect()
