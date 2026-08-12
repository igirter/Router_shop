from pydantic import BaseModel, Field


class Item(BaseModel):
    product_id: int
    count: int
    price: float

class CheckoutScheme(BaseModel):
    full_name: str = Field(max_length=128)
    phone: str = Field(min_length=11, max_length=12, pattern="^(?:\+7|8)\d{10}$")
    email: str = Field(max_length=128)
    address: str = Field(max_length=255)

    products: list[Item]
