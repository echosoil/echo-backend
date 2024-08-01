from functools import wraps  
from api.config import db


def count_route_usage(route_template, dynamic_paths=None):
    """
    A decorator that counts how often a specific route is used.
    
    Parameters
    ----------
    route_template : str
        A string template for the route that might contain placeholders for
        dynamic parts.
    dynamic_paths : list of tuples, optional
        An optional list of tuples where each tuple contains the name of a
        dynamic path segment and its position in the route template.
    """
    def decorator_count_route(func):
        # The actual decorator that wraps the function (the route handler).
        @wraps(func)  # Uses 'wraps' to preserve the original function's name,
                      # docstring, etc.
        async def wrapper_count_route(*args, **kwargs):
            # The wrapper function around the original route handler,
            # making it async since it's intended for use with async functions.
            
            # Initialize a dictionary to hold the parts of the route that are
            # dynamic.
            dynamic_parts = {}
            if dynamic_paths:
                # If there are dynamic paths specified, loop through them.
                for path_name, position in dynamic_paths:
                    # For each dynamic path, check if it's passed in kwargs to
                    # the function.
                    if path_name in kwargs:
                        # If present, add the dynamic path value to the
                        # 'dynamic_parts' dictionary.
                        dynamic_parts[position] = str(kwargs[path_name])
            
            # Construct the full route by formatting the route template with
            # the dynamic parts.
            full_route = route_template.format(**dynamic_parts)

            # Increment the counter in MongoDB for this route.
            db.route_counts.update_one(
                {"route_name": full_route}, # Query part: find the document with the route name.
                {"$inc": {"count": 1}},  # Update part: increment the 'count' field by 1.
                upsert=True  # If the document doesn't exist, insert it with the initial count of 1.
            )

            # Call the original function (route handler) with its arguments
            # and return its result.
            return await func(*args, **kwargs)

        return wrapper_count_route
    return decorator_count_route
