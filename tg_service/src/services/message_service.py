



def format_message(params: dict) -> str:
    message = f'''
            Заказчик: {params["full_name"]}
            Номер телефона: {params["phone"]}
            Почта: {params["email"]}
            Адрес: {params["address"]}
            Товары:
    '''
    for item in params["items"]:
        message += f'''
            Название:{item["product_name"]}
            Количество:{item["count"]}
            Цена:{item["price"]}
        '''
    return message
