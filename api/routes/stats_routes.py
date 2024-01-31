from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any


from api.services.stats_services import get_route_counter, delete_route_counter

router = APIRouter()

@router.get("/",
            summary="Retrieve the usage count of all routes.",
            description="Returns the number of times each route has been called.",
            response_model=List[Dict[str, Any]])  # You might need to define a more specific response model
async def get_route_usage():
    """
    Retrieve the usage count of all routes.
    """
    status, response = await get_route_counter()
    if status:
        return response
    else:
        return HTTPException(status_code=500, detail=response)


@router.delete("/",
                summary="Delete all documents in the route_counter collection.",
                description="Delete all documents in the route_counter collection.",
                status_code=204,
                responses={
                     500: {
                          "description": "Internal server error."
                     }
                })
async def delete_route_usage():
    """
    Delete all documents in the route_counter collection.
    """
    status = await delete_route_counter()
    if status:
        return "Route counter collection deleted successfully."
    else:
        raise HTTPException(status_code=500, detail="Internal server error.")
