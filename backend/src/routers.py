from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session

from src.db import get_db
from src.schemas import (
    CheckoutCreateScheme,
    CheckoutScheme,
    ProductCreationScheme,
    ProductScheme,
)
from src import service
from src.enums import ResultEnum


router = APIRouter()


@router.get(
    "/products",
    response_model=list[ProductScheme]
)
def get_products(session: Session = Depends(get_db)):
    return service.get_products(session)


@router.get(
    "/products/{product_id}",
    status_code=200,
)
def get_product(
    product_id: int,
    session: Session = Depends(get_db)
):
    product = service.get_product_by_id(product_id, session)

    if product is None:
        raise HTTPException(
            status_code=500,
            detail="Product not found"
        )

    return product


@router.post(
    "/products",
    status_code=201
)
def add_product(
    product: ProductCreationScheme,
    session: Session = Depends(get_db)
):
    response = service.add_product(product, session)

    if response is None:
        raise HTTPException(
            status_code=500,
            detail="Product didn't add"
        )

    return {"message": "product added"}

@router.get(
    "/checkouts",
    response_model=list[CheckoutScheme]
)
def get_checkouts(session: Session = Depends(get_db)):
    return service.get_all_checkouts(session)


@router.get(
    "/checkouts/{checkout_id}",
    response_model=CheckoutScheme
)
def get_checkout_by_id(
    checkout_id: int,
    session: Session = Depends(get_db)
):
    checkout = service.get_checkout_by_id(checkout_id, session)

    if checkout is None:
        raise HTTPException(
            status_code=404,
            detail="Checkout not found"
        )

    return checkout


@router.post(
    "/checkouts",
    status_code=201
)
async def save_to_database(
    request: Request,
    checkout: CheckoutCreateScheme,
    session: Session = Depends(get_db)
):
    result = await service.process_checkout(
        request,
        checkout,
        session
    )

    if result == ResultEnum.OK:
        return {"message": "checkout created"}
    raise HTTPException(
        status_code=404,
        detail="checkout didn't create"
        )
