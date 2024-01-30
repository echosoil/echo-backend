# Desc: Find data in mongo database
from bson import ObjectId, regex

from api.config import db
from api.schemas.mongo_schemas import data_collection


async def find_data(search=None, limit=10, sort="asc"):
    """
    Find data in mongo database.
    
    Parameters
    ----------
    search : str
        Search for specific data.
    limit : int
        Limit the number of results returned.
    sort : SortOrder
        Sort the results in ascending (asc) or descending (desc) order.
        
    Returns
    -------
    list
        Data collection.
    """
    sort_order = 1 if sort == "asc" else -1

    if search is None:
        result = db.data.find().sort("modified", sort_order).limit(limit)
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
        
        result = db.data.find(
            {"$or": query_conditions}).sort("modified", sort_order).limit(limit)

    return data_collection(result)