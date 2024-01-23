# Desc:
from api.config import db


async def delete_data(id):
    """
    Delete data from mongo database.
    
    Parameters
    ----------
    id : str
        ID of data to delete.
    """
    # Delete data from mongo database
    return db.data.delete_one({'id': id})
