from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from src.models import Checkout, CheckoutProduct, Product

def get_products(session: Session) -> list[Product]:
    return session.query(Product).all()

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
                raise SQLAlchemyError

            product.checkout_id = checkout_model.id
            product.price = p.price * product.count
            session.add(product)
        session.commit()

    except SQLAlchemyError as e:
        session.rollback()
        print(e)
