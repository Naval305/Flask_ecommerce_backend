from app.db.database import db


async def category_create(data):
    return await db["category"].insert_one(data)

async def get_category_list():
    return await db["category"].find().to_list(length=None)