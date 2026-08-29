from sqlalchemy.orm import Session
from src.models import Checkout, CheckoutProduct

def save_to_database(checkout: Checkout, session: Session):
    session.add(checkout)

def save_to_database_CheckoutProduct(checkout_product: CheckoutProduct, session: Session):
    session.add(checkout_product)
