from functools import wraps
from api.config import db

def count_route_usage(route_name):
    def decorator_count_route(func):
        @wraps(func)
        async def wrapper_count_route(*args, **kwargs):
            # Increment the count in MongoDB
            db.route_counts.update_one(
                {"route_name": route_name},
                {"$inc": {"count": 1}},
                upsert=True
            )
            # Call the original function
            return await func(*args, **kwargs)
        return wrapper_count_route
    return decorator_count_route
