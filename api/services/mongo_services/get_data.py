# Desc: Get data from mongo
from bson import ObjectId
from api.config import db


async def get_data(id):
    """
    Get data from mongo database.

    Parameters
    ----------
    id: str
        ID of data to retrieve.
    """
    # Check if id is a valid ObjectId
    if not ObjectId.is_valid(id):
        return None
    # Get data from mongo database
    return db.data.find_one({"_id": ObjectId(id)})
