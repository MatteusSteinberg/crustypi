from database import get_mongo_client
from schema import validation_rule

dbName = 'crustypi'
collectionName = 'airdata'

def insert_data(data: dict[str, any]):
    client = get_mongo_client()
    db = client[dbName]

    if not collectionName in db.list_collection_names():
        collection = db.create_collection(collectionName, validation_rule)
    else:
        collection = db[collectionName]


    collection.insert_one(data)
    client.close()
    return