from typing import Annotated, List

from fastapi import APIRouter, Depends, Request
from pymongo.errors import PyMongoError

from app.db.database import db
from app.schemas.custom_response import CustomResponse
from app.schemas.category_schemas import CategoryCreateSchema, CategoryModel


router = APIRouter()


@router.post("/create")
async def create_category(category: CategoryCreateSchema, request: Request,):
    """
    Create a new category.

    Parameters:
    - `category`: The category data as per the `CategoryCreateSchema` model.

    Returns:
    - JSON response indicating the success or failure of the category creation.

    Example:
    ```json
    {
        "data": null,
        "message": "Success",
        "status_code": 200
    }
    ```

    Possible Errors:
    - 500 Internal Server Error: If there's an issue with the server.

    """
    try:
        token = request.headers.get("token")
        category_data = category.model_dump()
        breakpoint()
        category_data["created_by"] = {"id": 1, "email": "user1@gmail.com"}
        result = await db["category"].insert_one(category_data)
        return CustomResponse(
            message="Category Created",
            data={"category_id": str(result.inserted_id)},
            status_code=201,
        )
    except PyMongoError as mongo_error:
        return CustomResponse(message="MongoDB Error", exception=mongo_error)
    except Exception as e:
        return CustomResponse(message="Internal Server Error", exception=e, status_code=500)


@router.get("/list", response_model=List[CategoryModel])
async def category_list():
    """
    Fetch all documents from the 'category' collection.

    Returns:
    - List of category documents.

    Example Response:
    ```json
    [
        {
            "name": "Category1",
            "description": "Description1"
        },
        {
            "name": "Category2",
            "description": "Description2"
        },
        ...
    ]
    ```

    Possible Errors:
    - 500 Internal Server Error: If there's an issue with the server.
    """
    try:
        categories = await db["category"].find().to_list(length=None)
        return categories
    except PyMongoError as mongo_error:
        return CustomResponse(
            message="MongoDB Error", status_code=500, exception=mongo_error
        )
    except Exception as e:
        return CustomResponse(
            message="Internal Server Error", status_code=500, exception=e
        )
