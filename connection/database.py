# db/connection.py
import psycopg

def get_connection():
    """
    Returns a PostgreSQL connection object
    """
    conn = psycopg.connect(
        host="localhost",
        dbname="student_data_2024",
        user="postgres",
        password="1234",
        port=5432
    )
    return conn
