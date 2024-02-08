from functools import wraps
from api.config import db

def count_route_usage(route_template, dynamic_paths=None):
    def decorator_count_route(func):
        @wraps(func)
        async def wrapper_count_route(*args, **kwargs):
            # Construir la ruta reemplazando los marcadores con los valores dinámicos
            dynamic_parts = {}
            if dynamic_paths:
                for path_name, position in dynamic_paths:
                    # Asumiendo que los nombres dinámicos se pasan como kwargs a la función
                    if path_name in kwargs:
                        dynamic_parts[position] = str(kwargs[path_name])
            
            # Construir la ruta final
            full_route = route_template.format(**dynamic_parts)

            # Incrementar el contador en MongoDB
            db.route_counts.update_one(
                {"route_name": full_route},
                {"$inc": {"count": 1}},
                upsert=True
            )

            # Llamar a la función original
            return await func(*args, **kwargs)

        return wrapper_count_route
    return decorator_count_route
