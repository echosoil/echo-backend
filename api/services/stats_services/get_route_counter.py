from api.config.db import db
from pymongo.errors import PyMongoError


async def get_route_counter():
    """
    Retrieve the usage count of all routes.
    
    Returns
    -------
    bool
        True if the operation was successful, False otherwise.
    list
        A list of dictionaries containing the route usage data
        if the operation was successful, an error message otherwise.
    """
    try:
        route_usage_data = db.route_counts.find()
        route_list = []
        for route in route_usage_data:
            # It's safe to assume "_id" will always be present,
            # but if you're not sure, you can check its existence before
            # deleting
            if "_id" in route:
                del route["_id"]
            route_list.append(route)
        # Add a new entry to the list with the total number of calls
        all_routes_count = 0
        for route in route_list:
            for key, value in route.items():
                if key == "count":
                    all_routes_count += value
        route_list.append(
            {"route_name": "all_routes", "count": all_routes_count})
        return True, route_list
    except PyMongoError as e:
        # Handle errors related to PyMongo
        print(f"An error occurred with MongoDB: {e}")
        return False, f"An error occurred with the dB: {e}"
    except Exception as e:
        # Handle any other unexpected type of error
        print(f"An unexpected error occurred: {e}")
        return False, f"An unexpected error occurred: {e}"
