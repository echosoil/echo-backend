# Desc: Delete all documents in the route_counter collection.
from api.config.db import db
from pymongo.errors import PyMongoError


async def delete_route_counter():
    """
    Delete all documents in the route_counter collection.
    
    Returns
    -------
    bool
        True if the operation was successful, False otherwise.
    """
    try:
        db.route_counts.delete_many({})
        return True
    except PyMongoError as e:
        # Handle errors related to PyMongo
        print(f"An error occurred with MongoDB: {e}")
        return False
    except Exception as e:
        # Handle any other unexpected type of error
        print(f"An unexpected error occurred: {e}")
        return False
