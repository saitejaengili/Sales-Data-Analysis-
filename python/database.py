
import os
import psycopg2
from dotenv import load_dotenv
from pathlib import Path

# Find the main project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env from the main directory
load_dotenv(BASE_DIR / ".env")

def get_connection():

    # Read database credentials
    db_password = os.getenv("DB_PASSWORD")

    if not db_password:
        raise ValueError(
            "DB_PASSWORD is missing. Check your .env file."
        )

    try:
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=os.getenv("DB_PORT", "5432"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=db_password
        )

        return connection

    except psycopg2.Error as error:
        print("Database connection failed:", error)
        raise


if __name__ == "__main__":

    try:
        connection = get_connection()

        print("PostgreSQL connected successfully!")

        connection.close()

        print("Database connection closed.")

    except Exception as error:
        print("Please check your database configuration.")
        print("Error:", error)
