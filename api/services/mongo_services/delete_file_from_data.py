from pymongo import ReturnDocument
from bson import ObjectId
from datetime import datetime

from api.config import db
from api.schemas.mongo_schemas import data_entity

async def delete_file_from_data(data_id, bucket, file_name):
    """
    Remove a file from the 'files' list in a Data document in MongoDB, and update the 'modified' field.
    
    Parameters
    ----------
    data_id : str
        Data ID.
    bucket : str
        Bucket name of the file to be removed.
    file_name : str
        Name of the file to be removed.

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

    # Update the document by removing the specified file from the files list and updating the modified field
    updated_data = db.data.find_one_and_update(
        {"_id": data_id},
        {
            "$pull": {"files": {"bucket": bucket, "file": file_name}},
            "$set": {"modified": current_time}
        },
        return_document=ReturnDocument.AFTER
    )

    # Check if the document was found and updated
    if updated_data:
        return data_entity(updated_data)
    else:
        # Handle the case where the document is not found
        # You might raise an exception or handle it in another way according to your business logic
        return None