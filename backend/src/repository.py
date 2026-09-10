from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload
from sqlalchemy.exc import SQLAlchemyError

from src.models import Checkout, CheckoutProduct, Product

def get_products(session: Session) -> list[Product]:
    return session.query(Product).all()

def get_product_by_id(product_id: int, session: Session):
    return session.query(Product).filter(Product.id == product_id).first()

def get_all_checkouts(session: Session) -> list[Checkout]:
    stmt = (
        select(Checkout)
        .options(
            selectinload(Checkout.items)
            .selectinload(CheckoutProduct.product)
        )
    )
    checkouts = session.scalars(stmt).all()

    return checkouts

def get_checkout_by_id(checkout_id: int, session: Session) -> Checkout:
    stmt = (
        select(Checkout)
        .where(Checkout.id == checkout_id)
        .options(
            selectinload(Checkout.items)
            .selectinload(CheckoutProduct.product)
        )
    )
    checkout = session.scalars(stmt).first()

    return checkout

def save_product(
    product_model: Product,
    session: Session
):
    session.add(product_model)
    session.commit()


def save_checkout(
    checkout_model: Checkout,
    model_products: list[CheckoutProduct],
    session: Session
):
    try:
        session.add(checkout_model)

        session.flush()

        for product in model_products:
            p = session.query(Product).filter(
                Product.id == product.product_id
            ).first()

            if p is None:
                raise SQLAlchemyError(
                    f"Product {product.product_id} not found"
                )

            product.checkout_id = checkout_model.id
            product.price = p.price * product.count

            session.add(product)

        session.commit()

    except SQLAlchemyError as e:
        session.rollback()
        raise e
