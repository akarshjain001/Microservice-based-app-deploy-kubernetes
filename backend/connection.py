from pymongo import MongoClient
from os import environ

MONGO_HOST = environ.get("MONGO_HOST", "localhost") # MongoDB host, default is localhost

client = MongoClient(MONGO_HOST, 27017) # MongoDB client, default port is 27017

db = client["fendir"] # This is the database where the data is stored

collection = db["names"] # This is the collection where the names are stored, collection is inside the database

