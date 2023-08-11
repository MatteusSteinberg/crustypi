from database import get_database_connection

tableName = 'sensordata'

def create_table():
    con = get_database_connection()
    cursor = con.cursor()
    count = cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{tableName}'").rowcount

    if count == 0:
        cursor.execute(f'CREATE TABLE {tableName}(timestamp, humidity, temperature, pressure, detectedMotion)')
        con.commit()

    cursor.close()
    con.close()
    return

def insert_data(data: dict[str, any]):
    con = get_database_connection()
    cursor = con.cursor()

    cursor.execute(f"INSERT INTO {tableName} VALUES (?, ?, ?, ?, ?)", (
        data['timestamp'],
        data['humidity'],
        data['temperature'],
        data['pressure'],
        int(data['detectedMotion'])
    ))

    # Commits changes to database
    con.commit()

    cursor.close()
    con.close()
    return

def get_data():
    con = get_database_connection()
    cursor = con.cursor()
    res = cursor.execute(f'SELECT * FROM {tableName}')
    rows = res.fetchall()

    result = []
    for row in rows:
        data_dict = {
            'timestamp': row[0],
            'humidity': row[1],
            'temperature': row[2],
            'pressure': row[3],
            'detectedMotion': bool(row[4])
        }
        result.append(data_dict)

    cursor.close()
    con.close()
    return result

def delete_data():
    con = get_database_connection()
    cursor = con.cursor()
    cursor.execute(f"DELETE FROM {tableName}")

    con.commit()

    cursor.close()
    con.close()
    return
