from fastapi import APIRouter
from typing import List, Dict, Any

from api.config.db import db

router = APIRouter()

@router.get("/",
            summary="Retrieve the usage count of all routes.",
            description="Returns the number of times each route has been called.",
            response_model=List[Dict[str, Any]])  # You might need to define a more specific response model
async def get_route_usage():
    """
    Retrieve the usage count of all routes.
    """
    route_usage_data = db.route_counts.find()
    # Delete the _id field from the response
    response = []
    for route in route_usage_data:
        del route["_id"]
        response.append(route)
    return response
