""" Модуль призначено для формування заявки ...
яка формується з файлів 'prices' та 'tovari' """

from data_service import get_prices, get_tovar

TITLE = "Аналіз зміни рівняння ринкових цін"
HEADER = \
"""
============================================================================================================
Код товару    :    Назва товару    :    Місяць :   Середня ринкова ціна за місяць :   Роздрібна ціна   :    Рівень зміни цін 
============================================================================================================
"""
price = get_prices()
tovar = get_tovar()

def find_name_tovares(name_code):
    """ шукає в довіднику назву товару по його коду"""

    for price in prices:
        if price_code == price[0]:
            return price[1]

    return "нема назви"        

def str_to_num(str_num):
    """перетворює строкове число в число"""
    if str_num.isnumeric():
        return float(str_num)
    else:
        str_num = str_num[:-1]

def show_analys(analysu):
    """вивід результатів на екран"""
    print(TITLE)
    print(HEADER)
    for row in analysu:
        print(f"{row['code']:4}", 
              f"{row['month']:15}",
              f"{row['averprice']:16}", 
              f"{row['retprice']:7.2f}",
              f"{row['change']:7.2f}", 
              f"{row['name']:6.2f}"
          )
              
         

analys = {
    'code' : "" ,     # код товару                         (tovari)
    'name' : "",      # назва товару                       (tovari)
    'month' : "",     # місяць                             (month)
    'averprice' : 0,  # середня ринкова ціна за місяць     (price)
    'retprice' : 0.0, # роздрібна ціна, грн                (price)
    'change' :  0.0   # рівень зміни цін                   (averprice*retprice)
}


analyss = []

for prices in tovar:
    analys['code'] = prices[1]
    analys['month'] = prices[3]
    analys['averprice'] = prices[2]
    analys['retprice'] = prices[4]
    analys['change'] = str_to_num(prices[2]) * str_to_num(prices[4])
    analys['name'] = find_name_tovares(str_to_num(price[0]))

    # changes.append(change)
    changes += change

    analyss.append(analys)
    

pass