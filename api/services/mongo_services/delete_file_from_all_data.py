# Desc: Delete a file info from the files list of a MongoDB document.
from datetime import datetime

from api.config import db
from api.services.utils.date_to_str import date_to_str


async def delete_file_from_all_data(bucket, file_name):
    """
    Remove a file from the 'files' list in all Data documents in MongoDB,
    and update the 'modified' field.
    
    Parameters
    ----------
    bucket : str
        Bucket name of the file to be removed.
    file_name : str
        Name of the file to be removed.
        
    Returns
    -------
    list
        List of Data entities.
    """

    # Current date and time
    current_time = datetime.utcnow()

    # Update the documents by removing the specified file from the files list and updating the modified field
    updated_data = db.data.update_many(
        {"files": {"$elemMatch": {"bucket": bucket, "file": file_name}}},
        {
            "$pull": {"files": {"bucket": bucket, "file": file_name}},
            "$set": {"modified": date_to_str(current_time)}
        }
    )

    # Check if the documents were found and updated
    if updated_data:
        return updated_data
    else:
        # Handle the case where the documents are not found
        # You might raise an exception or handle it in another way according to your business logic
        return None
