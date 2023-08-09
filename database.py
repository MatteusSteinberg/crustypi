from tinydb import TinyDB
from os import path

db_file = "db.json"

def get_database():
   if not path.isfile(db_file):
      open(db_file, "w")
   db = TinyDB(db_file)

   return db