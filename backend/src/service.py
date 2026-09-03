from sqlalchemy.orm import Session

from src.models import Product, Checkout, CheckoutProduct
from src import repository
from src.schemas import CheckoutCreateScheme, CheckoutScheme, Item, ProductScheme, ProductCreationScheme


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

def get_product_by_id(product_id: int, session: Session):
    raw_product = repository.get_product_by_id(product_id, session)

    return [
        ProductScheme(
            id=raw_product.id,
            name=raw_product.name,
            description=raw_product.description,
            price=raw_product.price,
        )
    ]


def get_all_checkouts(session: Session) -> list[CheckoutScheme]:
    checkouts = repository.get_all_checkouts(session)

    checkouts_schemas: list[CheckoutScheme] = []
    for raw in checkouts:
        checkout = CheckoutScheme(
            id=raw.id,
            full_name=raw.full_name,
            phone=raw.phone,
            email=raw.email,
            address=raw.address,
            products=[]
        )
        for i in raw.items:
            product = Item(
                product_id=i.product_id,
                name=i.product.name,
                count=i.count,
                price=i.price
            )
            checkout.products.append(product)
        checkouts_schemas.append(checkout)

    return checkouts_schemas


def get_checkout_by_id(checkout_id: int, session: Session):
    raw_checkout = repository.get_checkout_by_id(checkout_id, session)

    checkout = CheckoutScheme(
        id=raw_checkout.id,
        full_name=raw_checkout.full_name,
        phone=raw_checkout.phone,
        email=raw_checkout.email,
        address=raw_checkout.address,
        products=[]
    )
    for i in raw_checkout.items:
        product = Item(
            product_id=i.product_id,
            name=i.product.name,
            count=i.count,
            price=i.price
        )
        checkout.products.append(product)

    return checkout


def add_product(product: ProductCreationScheme, session: Session):
    product_model = Product(
        name=product.name,
        description=product.description,
        price=product.price
    )

    return repository.save_product(product_model, session)

def process_checkout(checkout_scheme: CheckoutCreateScheme, session: Session):
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
