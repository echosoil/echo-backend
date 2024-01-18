from pymongo import MongoClient

from api.config.settings import settings


MongoClient = MongoClient(settings.mongo_url)

if settings.mode == "dev":
    db = MongoClient.EchoDev
else:
    db = MongoClient.EchoProd
