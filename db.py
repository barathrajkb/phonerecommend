import mysql.connector
import pandas as pd
import streamlit as st

def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password',
            database='abcheck'
        )
        return connection
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
        return None

def get_alldata_from_database():
    # Connect to the MySQL database
    conn = connect_to_db()

    # Query to fetch data from the table
    query = "SELECT * FROM abcheck;"  # Replace 'your_table_name' with your actual table name

    # Use pandas to read data from the database and create a DataFrame
    df = pd.read_sql_query(query, conn)

    # Close the connection
    conn.close()

    return df
