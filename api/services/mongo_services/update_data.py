# Desc: Update data in mongo database
from datetime import datetime

from api.config import db


async def update_data(id, data):
    """
    Update data in mongo database.
    
    Parameters
    ----------
    id : str
        ID of data to update.
    data : dict
        Data to update in mongo database.
    """
    # Add modified timestamp
    data['modified'] = datetime.utcnow()
    # Update data in mongo database
    return db.data.update_one({'id': id}, {'$set': data})
