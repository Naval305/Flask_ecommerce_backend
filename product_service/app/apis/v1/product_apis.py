import os
import sys

sys.path.append(f"{os.getcwd()}/fastapi_env/lib/python3.10/site-packages")

from fastapi import APIRouter
from pymongo.errors import PyMongoError

from app.db.database import db
from app.schemas.custom_response import CustomResponse
from app.schemas.product_schemas import ProductCreateSchema


router = APIRouter()


@router.post("/create")
async def create_product(product: ProductCreateSchema):
    """
    Create a new product.

    Parameters:
    - `product`: The product data as per the `ProductCreateSchema` model.

    Returns:
    - JSON response with details of the created product.

    Example:
    ```json
    {
        "data": {"product_id": "1234567890"},
        "message": "Product Added",
        "status_code": 201
    }
    ```

    Possible Errors:
    - 500 Internal Server Error: If there's an issue with the server.
    - 404 Not Found: If the specified category doesn't exist.
    - 400 Bad Request: If there's an issue with the input data.

    """
    try:
        product_data = product.model_dump()
        category = product_data["category"]

        category_obj = await db.category.find_one({"name": category})
        if category_obj is None:
            return CustomResponse(
                message=f"Category '{category}' not found.", status_code=404
            )

        product_data["category"] = {"name": category, "id": str(category_obj["_id"])}

        try:
            product_data["price"] = float(product_data["price"])
        except ValueError:
            return CustomResponse(message="Invalid price format", status_code=400)

        result = await db["products"].insert_one(product_data)

        return CustomResponse(
            data={"product_id": str(result.inserted_id)},
            message="Product Added",
            status_code=201,
        )
    except PyMongoError as e:
        return CustomResponse(
            message="MongoDB Error", status_code=500, exception=str(e)
        )
    except Exception as e:
        return CustomResponse(
            message="Internal Server Error", status_code=500, exception=str(e)
        )


@router.get("/get-list")
async def get_product_list():
    pass


@router.get("/get/{product_id}")
async def get_product():
    pass
