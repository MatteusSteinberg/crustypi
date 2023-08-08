from pymongo import MongoClient
def get_database():

   CONNECTION_STRING = "mongodb+srv://127.0.0.1:27017/crustypi"
 

   client = MongoClient(CONNECTION_STRING)
 

   return client['user_shopping_list']