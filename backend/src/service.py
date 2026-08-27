import repository
from sqlalchemy.orm import Session
from models import *
from schemas import CheckoutScheme

def process_checkout(checkout_scheme: CheckoutScheme, session: Session):

    checkout_model = Checkout(
        full_name=checkout_scheme.full_name,
        phone=checkout_scheme.phone,
        email=checkout_scheme.email,
        address=checkout_scheme.address,
    )
    # Доп логика
    # Проверяется наличие товара
    # Товар создается как экземпляр своего класс
    # клиент пересылается на сайт с оплатой. тут дерагется вебхук. если он отработал
    # мы сохраняем товар в бд и отправляем в телеграм админам инфу о заказе.
    # Переписать на асинхрон ожидание проверки с бд, ожидание вебхука. на клиенте сделать
    # вращающийся кружочек (например)
    return repository.save_to_database(checkout_model, session)
