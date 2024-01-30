# Desc: Add a File to an existing list of Files in a Data in MongoDB
from pymongo import ReturnDocument
from bson import ObjectId
from datetime import datetime

from api.config import db
from api.services.utils.date_to_str import date_to_str
from api.schemas.mongo_schemas import data_entity


async def add_file_to_data(data_id, file_info):
    """
    Add a File to an existing list of Files in a Data in MongoDB, and update
    the 'modified' field.
    
    Parameters
    ----------
    data_id : str
        Data ID.
    file_info : dict
        {'bucket': 'my_bucket', 'file': 'my_file.txt'}
        
    Returns
    -------
    dict
        Data entity.
    """

    # Convert data_id to ObjectId if necessary
    if isinstance(data_id, str):
        data_id = ObjectId(data_id)

    # Current date and time
    current_time = datetime.utcnow()

    # Update the document by adding file_info to the files list and updating
    # the modified field
    updated_data = db.data.find_one_and_update(
        {"_id": data_id},
        {
            "$push": {"files": file_info.to_dict()},
            "$set": {"modified": date_to_str(current_time)}
        },
        return_document=ReturnDocument.AFTER
    )

    # Check if the document was found and updated
    if updated_data:
        return data_entity(updated_data)
    else:
        # Handle the case where the document is not found
        # You might raise an exception or handle it in another way according to
        # your business logic
        return None
