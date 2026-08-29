from src.repository import repository
from src.sqlalchemy.orm import Session
from src.models import *
from src.schemas import CheckoutScheme

def process_checkout(checkout_scheme: CheckoutScheme, session: Session):

    try:
        checkout_model = Checkout(
            full_name=checkout_scheme.full_name,
            phone=checkout_scheme.phone,
            email=checkout_scheme.email,
            address=checkout_scheme.address,
        )

        repository.save_to_database(checkout_model, session)

        for item in checkout_scheme.products:
            product = CheckoutProduct(
                product_id=item.product_id,
                count=item.count,
                price=item.price
            )
            repository.save_to_database_CheckoutProduct(product, session)

        session.commit()
    except:
        session.rollback()
    # Доп логика
    # Проверяется наличие товара
    # Товар создается как экземпляр своего класс
    # клиент пересылается на сайт с оплатой. тут дерагется вебхук. если он отработал
    # мы сохраняем товар в бд и отправляем в телеграм админам инфу о заказе.
    # Переписать на асинхрон ожидание проверки с бд, ожидание вебхука. на клиенте сделать
    # вращающийся кружочек (например)
