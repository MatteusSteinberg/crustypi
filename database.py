from pymongo import MongoClient

CONNECTION_STRING = "mongodb+srv://127.0.0.1:27017/"

def get_mongo_client():
   client = MongoClient(CONNECTION_STRING)

   return client