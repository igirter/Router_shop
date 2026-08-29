from sqlalchemy.orm import Session

from src.models import Product, Checkout, CheckoutProduct
from src import repository
from src.schemas import CheckoutScheme, ProductScheme, ProductCreationScheme


def get_products(session: Session):
    raw_products = repository.get_products(session)

    return [
        ProductScheme(
            id=product.id,
            name=product.name,
            description=product.description,
            price=product.price,
        )
        for product in raw_products
    ]

def add_product(product: ProductCreationScheme, session: Session):
    product_model = Product(
        name=product.name,
        description=product.description,
        price=product.price
    )

    return repository.save_product(product_model, session)

def process_checkout(checkout_scheme: CheckoutScheme, session: Session):
    checkout_model = Checkout(
        full_name=checkout_scheme.full_name,
        phone=checkout_scheme.phone,
        email=checkout_scheme.email,
        address=checkout_scheme.address,
    )

    model_products: list[CheckoutProduct] = []
    for item in checkout_scheme.products:
        model_products.append(
            CheckoutProduct(
                product_id=item.product_id,
                count=item.count,
            )
        )
    repository.save_checkout(checkout_model, model_products, session)
