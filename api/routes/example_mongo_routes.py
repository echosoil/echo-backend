from fastapi import APIRouter, Query
from typing import List

from api.services.test_services import get_test, post_test, delete_test
from api.models import Data, DataInDB, UpdateData

router = APIRouter()


@router.get("",
            summary="Retrieve some information from the MongoDB.",
            description="Retrieve some information from the MongoDB.",
            response_model=List[DataInDB],
            
            )
async def get_router(
    search: str = Query(
        None,
        description="Search for specific data. Use (*) as a wildcard " + \
            "character to replace unknown characters or to search for a " + \
            "partial match."),
    limit: int = Query(
        10,
        description="Limit the number of results returned.")):
    """
    Retrieve some information from the MongoDB.
    """
    return await get_test(search, limit)


@router.post("",
             summary="Store some information from the MongoDB.",
             description="Store some information from the MongoDB.",
             response_model=DataInDB,
             status_code=201)
async def post_router(data: Data):
    """
    Store some information from the MongoDB.
    """
    return await post_test(data)


@router.put("",
            summary="Store some information from the MongoDB.",
            description="Store some information from the MongoDB.",
            status_code=204)
async def put_router(update_data: UpdateData,
                     id: str = Query(...,
                        description="The unique identifier of the data.")):
    """
    Store some information from the MongoDB.
    """
    return None


@router.delete("",
               summary="Delete some information from the MongoDB.",
               description="Delete some information from the MongoDB.",
               status_code=204)
async def delete_router(id: str = Query(...,
                        description="The unique identifier of the data.")):
    """
    Delete some information from the MongoDB.
    """
    return None
