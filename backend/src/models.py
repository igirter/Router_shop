from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from sqlalchemy.types import Double

from src.db import Base


class Checkout(Base):

    __tablename__ = "checkouts"

    id: Mapped[int] =  mapped_column(primary_key=True, index=True)
    full_name: Mapped[str] = mapped_column(nullable=False)
    phone: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    address: Mapped[str] = mapped_column(nullable=False)

    items: Mapped[list["CheckoutProduct"]] = relationship(
        "CheckoutProduct",
        back_populates="checkout"
    )



class CheckoutProduct(Base):

    __tablename__ = "checkout_product"

    checkout_id: Mapped[int] = mapped_column(
        ForeignKey("checkouts.id"),
        primary_key=True
    )
    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id"),
        primary_key=True
    )

    count: Mapped[int] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)

    checkout: Mapped["Checkout"] = relationship(
        "Checkout", back_populates="items"
    )
    product: Mapped["Product"] = relationship(
        "Product", back_populates="items"
    )

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[float] = mapped_column(Double, nullable=False)

    items: Mapped[list[CheckoutProduct]] = relationship(
        "CheckoutProduct",
        back_populates="product",
    )
