from pydantic import BaseModel, constr


class CategoryCreateSchema(BaseModel):
    name: constr(max_length=30)
    status: bool = True
    parent_id: str = None