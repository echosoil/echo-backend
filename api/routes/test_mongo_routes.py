from fastapi import APIRouter

from api.services.test_services import get_test, post_test, delete_test

test_route = APIRouter()
base = '/test/'


@test_route.get(base)
async def get_test():
    """
    Retrieve some information from the MongoDB.
    """
    return await get_test()


@test_route.post(base)
async def get_test():
    """
    Store some information from the MongoDB.
    """
    return await post_test()


@test_route.delete(base)
async def get_test():
    """
    Delete some information from the MongoDB.
    """
    return await delete_test()
