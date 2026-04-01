# db.py

import os
import psycopg2
from datetime import datetime
from dotenv import load_dotenv


# Load .env file
load_dotenv()

# 🔹 Step 1: Connect to database
def get_connection():

    db_host = os.getenv("DB_HOST")
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")

    connection = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_password
    )

    return connection


# 🔹 Step 2: Create table if not exists
def create_table():

    connection = get_connection()
    cursor = connection.cursor()

    create_query = """
    CREATE TABLE IF NOT EXISTS chat_logs (
        id SERIAL PRIMARY KEY,
        user_message TEXT,
        bot_reply TEXT,
        timestamp TIMESTAMP
    );
    """

    cursor.execute(create_query)
    connection.commit()

    cursor.close()
    connection.close()


# 🔹 Step 3: Insert chat data
def save_chat(user_message, bot_reply):

    connection = get_connection()
    cursor = connection.cursor()

    insert_query = """
    INSERT INTO chat_logs (user_message, bot_reply, timestamp)
    VALUES (%s, %s, %s);
    """

    current_time = datetime.now()

    cursor.execute(insert_query, (user_message, bot_reply, current_time))
    connection.commit()

    cursor.close()
    connection.close()