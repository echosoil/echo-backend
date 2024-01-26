from functools import wraps
from api.config import db

def count_route_usage(route_name, dynamic_path=None):
    def decorator_count_route(func):
        @wraps(func)
        async def wrapper_count_route(*args, **kwargs):
            # Extract the dynamic path value if it's specified and present in the kwargs
            dynamic_value = kwargs.get(dynamic_path) if dynamic_path else None
            
            # Construct the full route name with the dynamic value if available
            full_route_name = f"{route_name}/{dynamic_value}" if dynamic_value else route_name

            # Increment the count in MongoDB
            db.route_counts.update_one(
                {"route_name": full_route_name},
                {"$inc": {"count": 1}},
                upsert=True
            )
            # Call the original function
            return await func(*args, **kwargs)
        return wrapper_count_route
    return decorator_count_route