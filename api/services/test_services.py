from api.config.db import db

async def get_test():
    pass 

async def post_test():
    test_data = {"test": "test"}
    result = db.test.insert_one(dict(test_data))
    print(result)
    
async def delete_test():
    pass
