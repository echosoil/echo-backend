# Desc: Get data from mongo

from api.config import db


async def get_data(id):
    """
    Get data from mongo database.

    Parameters
    ----------
    id: str
        ID of data to retrieve.
    """

    # Get data from mongo database
    return db.data.find_one({'id': id}, {'_id': 0, 'id': 0})
