# Import FastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes.default_routes import default_route
from api.routes.test_mongo_routes import test_route
# from pymongo import MongoClient

origins = [
    "*", # Allow all origins
]

app = FastAPI(
    title="FastAPI-Users-Backend", description = "CRUD API",
    # root_path="/api"
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(default_route)
app.include_router(test_route)
