from src.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Checkout(Base):

    __tablename__ = "checkouts"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    address = Column(String, nullable=False)

    items = relationship("CheckoutProduct", back_populates="checkout")



class CheckoutProduct(Base):

    __tablename__ = "checkout_product"

    checkout_id = Column(
        Integer,
        ForeignKey("checkouts.id"),
        primary_key=True)

    product_id = Column(
        Integer,
        ForeignKey("products.id"),
        primary_key=True)


    count = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)

    checkout = relationship("Checkout", back_populates="items")
    product = relationship("Product", back_populates="items")

class Product(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Integer, nullable=False)

    items = relationship("CheckoutProduct", back_populates="product")
