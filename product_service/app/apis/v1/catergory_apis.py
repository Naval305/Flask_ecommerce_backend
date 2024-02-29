from fastapi import APIRouter
from pymongo.errors import PyMongoError

from app.db.database import db
from app.schemas.custom_response import CustomResponse
from app.schemas.category_schemas import CategoryCreateSchema


router = APIRouter()


@router.post("/create")
async def create_category(category: CategoryCreateSchema):
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
        category_data = category.model_dump()
        category_data["created_by"] = {"id": 1, "email": "user1@gmail.com"}
        await db["category"].insert_one(category_data)
        return CustomResponse.success()
    except PyMongoError as mongo_error:
        return CustomResponse.error(message="MongoDB Error", exception=mongo_error)
    except Exception as e:
        return CustomResponse(message="Internal Server Error", exception=e)
