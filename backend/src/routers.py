import re


from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from src.db import get_db
from src.schemas import CheckoutCreateScheme, ProductCreationScheme
from src import service

router = APIRouter()

@router.get("/products")
def get_products(session: Session = Depends(get_db)):
    return service.get_products(session)

@router.get("/products/{product_id}")
def get_product(product_id: int, session: Session = Depends(get_db)):
    return service.get_product_by_id(product_id, session)

@router.post("/products")
def add_product(product: ProductCreationScheme, session: Session = Depends(get_db)):
    return service.add_product(product, session)

@router.get("/checkouts")
def get_checkouts(session: Session = Depends(get_db)):
    return service.get_all_checkouts(session)

@router.get("/checouts/{checkout_id}")
def get_checkout_by_id(checkout_id: int,  session: Session = Depends(get_db)):
    return service.get_checkout_by_id(checkout_id, session)

@router.post("/checkouts")
async def save_to_database(request: Request, checkout: CheckoutCreateScheme, session: Session = Depends(get_db)):
    return await service.process_checkout(request, checkout, session)
