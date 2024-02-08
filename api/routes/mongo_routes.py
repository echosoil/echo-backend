from fastapi import APIRouter, Query, HTTPException, Path, Body
from typing import List

from api.services.mongo_services import add_data, get_data, update_data, \
    delete_data, find_data, add_file_to_data, delete_file_from_data
from api.services.minio_services import check_object
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
@count_route_usage("GET /mongo/")
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
@count_route_usage("GET /mongo/{id}", dynamic_paths=[("id", "id")])
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
             status_code=201,
             responses={
                404: {
                    "description": "File not found."
                }
             })
@count_route_usage("POST /mongo/")
async def post_mongo(data: Data):
    """
    Store some information from the MongoDB.
    """
    # First, check if data has files.
    data_info = data.to_dict()
    if "files" in data_info:
        # Check if the files are valid.
        for file in data_info["files"]:
            if not await check_object(file["bucket"], file["file"]):
                raise HTTPException(status_code=404, detail="File not found.")
    new_data = await add_data(data)
    return new_data


@router.put("/{id}",
            summary="Store some information from the MongoDB.",
            description="Store some information from the MongoDB.",
            status_code=204)
@count_route_usage("PUT /mongo/{id}", dynamic_paths=[("id", "id")])
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
    # Check if data has files.
    data_info = data_to_update.to_dict()
    if "files" in data_info:
        # Check if the files are valid.
        for file in data_info["files"]:
            if not await check_object(file["bucket"], file["file"]):
                raise HTTPException(status_code=404, detail="File not found.")
    await update_data(id, data_to_update)
    return None


@router.delete("/{id}",
               summary="Delete some information from the MongoDB.",
               description="Delete some information from the MongoDB.",
               status_code=204)
@count_route_usage("DELETE /mongo/{id}", dynamic_paths=[("id", "id")])
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


@router.put("/{id}/file",
            summary="Add a file to the files list of a MongoDB document.",
            description="Add a file to the files list of a MongoDB document.",
            status_code=204,
            responses={
                404: {
                    "description": "Data or file not found."
                }
            })
@count_route_usage("PUT /mongo/{id}/file", dynamic_paths=[("id", "id")])
async def add_file_mongo(id: str = Path(..., description="The unique identifier of the data."),
                         file_info: File = Body(..., description="The file to add.")):
    """
    Add a file to the files list of a MongoDB document.
    """
    # First, check if the data exists.
    data = await get_data(id)
    if not data:
        raise HTTPException(status_code=404, detail="Data not found.")
    # Check if the file is valid.
    file_dict = file_info.to_dict()
    if not await check_object(file_dict["bucket"], file_dict["file"]):
        raise HTTPException(status_code=404, detail="File not found.")
    await add_file_to_data(id, file_info)
    return None


@router.delete("/{id}/file/{bucket}/{file}",
               summary="Remove a file from the files list of a MongoDB document.",
               description="Remove a file from the files list of a MongoDB document.",
               status_code=204)
@count_route_usage("DELETE /mongo/{id}/file/{bucket}/{file}",
                   dynamic_paths=[
                       ("id", "id"),
                       ("bucket", "bucket"),
                       ("file", "file")])
async def remove_file_mongo(id: str = Path(...,
                                           description="The unique identifier of the data."),
                            bucket: str = Path(...,
                                               description="The bucket of the file to remove."),
                            file: str = Path(...,
                                             description="The name of the file to remove.")):
    """
    Remove a file from the files list of a MongoDB document.
    """
    # First, check if the data exists.
    data = await get_data(id)
    if not data:
        raise HTTPException(status_code=404, detail="Data not found.")
    
    await delete_file_from_data(id, bucket, file)
    return None
