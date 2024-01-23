from fastapi import APIRouter, Query, HTTPException, Path
from typing import List

from api.services.mongo_services import add_data, get_data, update_data, \
    delete_data, find_data
from api.models import Data, DataInDB, UpdateData
from api.schemas.mongo_schemas import data_entity
from api.routes.decorators import count_route_usage

router = APIRouter()


@router.get("",
            summary="Retrieve some information from the MongoDB.",
            description="Retrieve some information from the MongoDB.",
            response_model=List[DataInDB],
            
            )
@count_route_usage("get_router")
async def get_router(
    search: str = Query(
        None,
        description="Search for specific data."),
    limit: int = Query(
        10,
        description="Limit the number of results returned.")):
    """
    Retrieve some information from the MongoDB.
    """
    return await find_data(search, limit)
    


@router.get("/{id}",
            summary="Retrieve some information from the MongoDB.",
            description="Retrieve some information from the MongoDB.",
            response_model=DataInDB,
            status_code=200,
            responses={
                404: {
                    "description": "Data not found."
                }
            })
@count_route_usage("get_id_router")
async def get_id_router(id: str = Path(...,
                        description="The unique identifier of the data.")):
    """
    Retrieve some information from the MongoDB.
    """
    # First, check if the data exists.
    data = await get_data(id)
    if not data:
        raise HTTPException(status_code=404, detail="Data not found.")
    return data_entity(data)


@router.post("",
             summary="Store some information from the MongoDB.",
             description="Store some information from the MongoDB.",
             response_model=DataInDB,
             status_code=201)
@count_route_usage("post_router")
async def post_router(data: Data):
    """
    Store some information from the MongoDB.
    """
    new_data = await add_data(data)
    print(new_data)
    return new_data


@router.put("/{id}",
            summary="Store some information from the MongoDB.",
            description="Store some information from the MongoDB.",
            status_code=204)
@count_route_usage("put_router")
async def put_router(data_to_update: UpdateData,
                     id: str = Path(...,
                        description="The unique identifier of the data.")):
    """
    Store some information from the MongoDB.
    """
    # First, check if the data exists.
    data = await get_data(id)
    if not data:
        raise HTTPException(status_code=404, detail="Data not found.")
    await update_data(id, data_to_update)
    return None


@router.delete("/{id}",
               summary="Delete some information from the MongoDB.",
               description="Delete some information from the MongoDB.",
               status_code=204)
@count_route_usage("delete_router")
async def delete_router(id: str = Path(...,
                        description="The unique identifier of the data.")):
    """
    Delete some information from the MongoDB.
    """
    # First, check if the data exists.
    data = await get_data(id)
    if not data:
        raise HTTPException(status_code=404, detail="Data not found.")
    await delete_data(id)
    return None
