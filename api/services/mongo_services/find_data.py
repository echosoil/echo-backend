# Desc: Find data in mongo database
from bson import ObjectId, regex

from api.config import db
from api.schemas.mongo_schemas import data_collection


async def find_data(search=None, limit=10):
    if search is None:
        result = db.data.find().limit(limit)
    else:
        query_conditions = [
            {"name": {"$regex": regex.Regex(search)}},
            {"description": {"$regex": regex.Regex(search)}},
            {"created": {"$regex": regex.Regex(search)}},
            {"modified": {"$regex": regex.Regex(search)}}
        ]

        # Intenta convertir la búsqueda a un número para buscar en campos numéricos
        try:
            numeric_search = int(search)
            query_conditions.append({"age": numeric_search})
        except ValueError:
            pass

        # Intenta convertir la búsqueda a ObjectId para buscar en '_id'
        if ObjectId.is_valid(search):
            query_conditions.append({"_id": ObjectId(search)})
        
        result = db.data.find({"$or": query_conditions}).limit(limit)

    return data_collection(result)