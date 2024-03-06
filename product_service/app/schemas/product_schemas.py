from pydantic import BaseModel, Field
from typing import Optional
from decimal import Decimal


class ProductCreateSchema(BaseModel):
    name: str = Field(max_length=100)
    sku: str = Field(max_length=45)
    description: Optional[str] = None
    price: Decimal = Field(ge=0.01, decimal_places=2)
    quantity: int = 1
    status: bool = True
    is_featured: bool = False
    category: str = None


class ProductModel(BaseModel):
    name: str
    sku: str
    description: str
    price: float
    quantity: int
    status: bool
    is_featured: bool
    category: dict