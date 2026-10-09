from pydantic import BaseModel, Field

class ProductCreationScheme(BaseModel):
    name: str
    description: str
    price: float

class ProductScheme(ProductCreationScheme):
    id: int

class ItemCreation(BaseModel):
    product_id: int
    count: int

class Item(ItemCreation):
    name: str
    price: float

class CheckoutCreateScheme(BaseModel):
    full_name: str = Field(max_length=128)
    phone: str = Field(min_length=11, max_length=12, pattern=r"^(?:\+7|8)\d{10}$")
    email: str = Field(max_length=128)
    address: str = Field(max_length=255)
    products: list[ItemCreation]

class CheckoutScheme(BaseModel):
    id: int
    full_name: str = Field(max_length=128)
    phone: str = Field(min_length=11, max_length=12, pattern=r"^(?:\+7|8)\d{10}$")
    email: str = Field(max_length=128)
    address: str = Field(max_length=255)
    products: list[Item]
