import pandas as pd
import mysql.connector
from db import connect_to_db
def insert_data_from_csv(connection, csv_file_path):
    # Read data from CSV file
    df = pd.read_csv(csv_file_path)

    # Insert data into the table
    columns = ', '.join(df.columns)
    placeholders = ', '.join(['%s'] * len(df.columns))
    query = f'INSERT INTO abcheck ({columns}) VALUES ({placeholders})'

    cursor = connection.cursor()
    for row in df.itertuples(index=False):
        row_values = [None if pd.isna(value) else value for value in row]
        cursor.execute(query, row_values)

    connection.commit()
    cursor.close()

if __name__ == '__main__':

    conn = connect_to_db()

    csv_file_path = 'dat.csv'

    insert_data_from_csv(conn, csv_file_path)

    conn.close()

    print(f"Data has been inserted successfully into the table.")

def insert_values(connection, data):
    try:
        cursor = connection.cursor()
        insert_query = "INSERT INTO products (brand, model, operating_system, internal_memory, RAM, performance, main_camera, selfie_camera, battery_size, screen_size, weight, price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, data)
        connection.commit()
        st.success("Data inserted successfully!")
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
        connection.rollback()
