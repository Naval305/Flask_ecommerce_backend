import uvicorn
from fastapi import FastAPI

from app.routers.product_routers import product_router
from app.routers.catergory_routers import catergory_router

app = FastAPI(docs_url="/swagger-ui", redoc_url="/redoc")

try:
    import pymongo
except Exception:
    import os
    import sys

    sys.path.append(
        f"{os.path.abspath(os.path.dirname(__file__))}/fastapi_env/lib/python3.10/site-packages"
    )

from app.db.database import *

app.include_router(product_router, prefix="/api")
app.include_router(catergory_router, prefix="/api")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
