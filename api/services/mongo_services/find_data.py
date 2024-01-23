# Desc: Find data in mongo database
from api.config import db


async def find_data(search=None, limit=10):
    """
    Find data in mongo database.
    
    Parameters
    ----------
    search : str
        Search for specific data. Use (*) as a wildcard character to replace unknown characters or to search for a partial match.
    limit : int
        Limit the number of results returned.
    """
    if search is None:
        return db.data.find().limit(limit)
    else:
        # Search for data by any field
        return db.data.find({"$or": [
            {"id": {"$regex": search}},
            {"name": {"$regex": search}},
            {"description": {"$regex": search}},
            {"age": {"$regex": search}},
            {"created": {"$regex": search}},
            {"modified": {"$regex": search}},
        ]}).limit(limit)
