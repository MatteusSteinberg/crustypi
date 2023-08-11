from os import path
import sqlite3

db_file = "db.json"

def get_database_connection():
   con = sqlite3.connect("sqlite.db")

   return con