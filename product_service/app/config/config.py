import os

from dotenv import load_dotenv


load_dotenv()

db_name = os.getenv("DB_NAME")
db_host = os.getenv("DB_HOST")
db_port = int(os.getenv("DB_PORT"))