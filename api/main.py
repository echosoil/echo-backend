# Import FastAPI
from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

# Define a route
@app.get("/")
async def read_root():
    return {"Hello": "World"}

# Replace with your MongoDB credentials and hostname (use 'mongodb' as hostname if using Docker Compose)
client = MongoClient("mongodb://mongouser:mongopassword@mongodb:27017/")
db = client.test_db  # Replace 'test_db' with your database name

@app.get("/mongo_test")
async def mongo_test():
    # Performing a simple operation, e.g., inserting a document
    db.test_collection.insert_one({"message": "Hello, MongoDB!"})
    return {"message": "MongoDB connection successful!"}
# Create an instance of the FastAPI class

