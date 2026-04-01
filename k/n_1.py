def find_first_index(products, product_name): #вызываем функцию
     """Возвращает индекс первого восхождения товара
        Если не гайден, возвращает None"""
     for position, item in enumerate(products): #Перебираем в списке элементы с индексом
         if item == product_name:
             return position
     return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_first_index(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
