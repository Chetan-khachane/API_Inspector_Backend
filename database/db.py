import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():


    try:
        return psycopg2.connect(
            os.getenv("DATABASE_URL"),
            sslmode="require"
        )

    except Exception as e:
        print("Database connection error:", e)
        return None