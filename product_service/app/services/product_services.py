from app.db.database import db


async def product_list():
    return await db["products"].find().to_list(length=None)


async def product_item(sku: str):
    return await db["products"].find_one({"sku": sku})