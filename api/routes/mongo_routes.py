from fastapi import APIRouter, Query, HTTPException, Path, Body
from typing import List

from api.services.mongo_services import add_data, get_data, update_data, \
    delete_data, find_data, add_file_to_data, delete_file_from_data
from api.models import Data, DataInDB, UpdateData, File
from api.schemas.mongo_schemas import data_entity
from api.routes.decorators import count_route_usage

from enum import Enum

class SortOrder(str, Enum):
    asc = "asc"
    desc = "desc"

router = APIRouter()


@router.get("",
            summary="Retrieve some information from the MongoDB.",
            description="Retrieve some information from the MongoDB.",
            response_model=List[DataInDB],
            
            )
@count_route_usage("get_mongo")
async def get_mongo(
    search: str = Query(
        None,
        description="Search for specific data."),
    limit: int = Query(
        10,
        description="Limit the number of results returned."),
    sort: SortOrder = Query(
        SortOrder.asc,
        description="Sort the results in ascending (asc) or descending (desc) order.")
    ):
    """
    Retrieve some information from the MongoDB.
    """
    return await find_data(search, limit, sort)
    


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
@count_route_usage("get_id_mongo")
async def get_id_mongo(id: str = Path(...,
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
@count_route_usage("post_mongo")
async def post_mongo(data: Data):
    """
    Store some information from the MongoDB.
    """
    new_data = await add_data(data)
    return new_data


@router.put("/{id}",
            summary="Store some information from the MongoDB.",
            description="Store some information from the MongoDB.",
            status_code=204)
@count_route_usage("put_mongo")
async def put_mongo(data_to_update: UpdateData,
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
@count_route_usage("delete_mongo")
async def delete_mongo(id: str = Path(...,
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


@router.put("/{id}/add-file",
            summary="Add a file to the files list of a MongoDB document.",
            description="Add a file to the files list of a MongoDB document.",
            status_code=204)
@count_route_usage("put_add_file_mongo")
async def add_file_mongo(id: str = Path(..., description="The unique identifier of the data."),
                         file_info: File = Body(..., description="The file to add.")):
    """
    Add a file to the files list of a MongoDB document.
    """
    # First, check if the data exists.
    data = await get_data(id)
    if not data:
        raise HTTPException(status_code=404, detail="Data not found.")
    
    await add_file_to_data(id, file_info)
    return None


# @router.delete("/{id}/file/{bucket}/{file}",
#                summary="Remove a file from the files list of a MongoDB document.",
#                description="Remove a file from the files list of a MongoDB document.",
#                status_code=204)
# @count_route_usage("delete_file_mongo")
# async def remove_file_mongo(id: str = Path(..., description="The unique identifier of the data."),
#                             bucket: str = Query(..., description="The bucket of the file to remove."),
#                             file: str = Query(..., description="The name of the file to remove.")):
#     """
#     Remove a file from the files list of a MongoDB document.
#     """
#     # First, check if the data exists.
#     data = await get_data(id)
#     if not data:
#         raise HTTPException(status_code=404, detail="Data not found.")
    
#     await delete_file_from_data(id, bucket, file)
#     return None