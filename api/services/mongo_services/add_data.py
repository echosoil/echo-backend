# Desc: Add data to mongo database
from datetime import datetime

from api.config import db
from api.services.utils.date_to_str import date_to_str
from api.schemas.mongo_schemas import data_entity


async def add_data(data):
    """
    Add data to mongo database.
    
    Parameters
    ----------
    data : dict
        Data to add to mongo database.
    """
    data_dict = data.to_dict()
    # Add created and modified timestamps
    actual_date = date_to_str(datetime.utcnow())
    data_dict['created'] = actual_date
    data_dict['modified'] = actual_date
    # Add data to mongo database
    result =  db.data.insert_one(data_dict)
    
    # Retrieve the inserted document (or construct the representation)
    inserted_id = result.inserted_id
    inserted_document = db.data.find_one({'_id': inserted_id})
    # Serialize the result
    return data_entity(inserted_document)
