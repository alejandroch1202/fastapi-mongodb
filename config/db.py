from pymongo import MongoClient

mongodb_uri = "<your-db-url>"
port = 8000

client = MongoClient(mongodb_uri, port)

db = client["anchor"]