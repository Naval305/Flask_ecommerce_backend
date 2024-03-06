import os
import sys
from typing import List

sys.path.append(f"{os.getcwd()}/fastapi_env/lib/python3.10/site-packages")

from fastapi import APIRouter
from pymongo.errors import PyMongoError

from app.db.database import db
from app.schemas.custom_response import CustomResponse
from app.schemas.product_schemas import ProductCreateSchema, ProductModel


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


@router.get("/list", response_model=List[ProductModel])
async def get_product_list():
    """
    Fetch all documents from the 'products' collection.

    Returns:
    - List of product documents.

    Example Response:
    ```json
    [
        {
            "name": "Product1",
            "sku": "1234",
            "description": "Description1",
            "price": 500.0,
            "quantity": 10,
            "status": True,
            "is_featured": False,
            "category": {"name": "Category1", "id": "1234567890"}
        },
        {
            "name": "Product2",
            "sku": "5678",
            "description": "Description2",
            "price": 750.0,
            "quantity": 5,
            "status": True,
            "is_featured": True,
            "category": {"name": "Category2", "id": "0987654321"}
        },
        ...
    ]
    ```

    Possible Errors:
    - 500 Internal Server Error: If there's an issue with the server.
    """
    try:
        products = await db["products"].find().to_list(length=None)
        return products
    except PyMongoError as mongo_error:
        return CustomResponse(
            status_code=500, message="MongoDB Error", exception=mongo_error
        )
    except Exception as e:
        return CustomResponse(
            status_code=500, message="Internal Server Error", exception=e
        )


@router.get("/get/{sku}", response_model=ProductModel)
async def get_product(sku: str):
    try:
        product = await db["products"].find_one({"sku": sku})
        if not product:
            return CustomResponse(
                message="Product with provided sku not found", status_code=404
            )
        return product
    except PyMongoError as mongo_error:
        return CustomResponse(
            status_code=500, message="MongoDB Error", exception=mongo_error
        )
    except Exception as e:
        return CustomResponse(
            status_code=500, message="Internal Server Error", exception=e
        )
