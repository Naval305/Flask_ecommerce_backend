
from motor.motor_asyncio import AsyncIOMotorClient

from app.config.config import db_host, db_port, db_name


client = AsyncIOMotorClient(db_host, db_port)

db = client[db_name]
