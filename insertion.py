from database import get_database
from database import get_database

def insert_data(data: dict[str, any]):
    db = get_database()

    db.insert(data)

    db.close()
    return

def get_data():
    db = get_database()
    docs = db.all()

    db.close()
    return docs

def delete_data():
    db = get_database()
    db.drop_tables()

    db.close()
    return