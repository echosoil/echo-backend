# Desc: Update data in mongo database
from datetime import datetime
from bson import ObjectId

from api.config import db
from api.services.utils.date_to_str import date_to_str

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
    data_dict = data.to_dict()

    # Delete None values
    data_dict = {k: v for k, v in data_dict.items() if v is not None}

    # Add modified timestamp
    actual_date = date_to_str(datetime.utcnow())
    data_dict['modified'] = actual_date
    # Update data in mongo database
    return db.data.update_one({"_id": ObjectId(id)}, {'$set': data_dict})
