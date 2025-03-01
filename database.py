# database.py - MongoDB Connection Handling
from pymongo import MongoClient
from config import DATABASE_URI, DATABASE_NAME, COLLECTION_NAME

client = MongoClient(DATABASE_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

def save_file(file_id, file_name, user_id):
    data = {"file_id": file_id, "file_name": file_name, "user_id": user_id}
    collection.insert_one(data)

def get_random_file():
    return collection.aggregate([{ "$sample": { "size": 1 } }]).next()
