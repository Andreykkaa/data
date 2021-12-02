def get_prices():
    """читання файлу 'prices'
    та формування списку цін 
    повертає список цін
    """
    #накопичення файлових даних у списку
    with open("/Users/mac/Desktop/data-1/prices.csv", 'r') as f:
        price = f.readlines()


    # підготовка даних для подальшої обробки
    prices_splitted = []
    # порізати в циклі строки на окремі єлементи
    for price in prices_splitted :
        obj = split_line(price)
        prices_splitted.append(obj)

    return prices_splitted

def split_line(line):
    """повертає список об'єктів з строки"""
    object = line.split(',')
    return object

# читання файлу товарів 'tovari'
def get_tovar():
    """читання файлу 'tovari'
    та формування списку товарів
    повертає список товарів
    """
    # накопичення даних файлу у списку
    with open("/Users/mac/Desktop/data-1/tovari.csv", 'r') as f:
        tovari = f.readlines ()

    # підготовка даних для подальшої обробки      
        tovari_splitted = []
        #порізати в циклі строки на окремі елементи
        for tovar in tovari:
            obj = split_line (tovar)
            tovari_splitted.append (obj)

    return tovari_splitted


# вивід списку цін
def show_prices(prices):
    """виводить список цін по заданому інтервалу кодів
    """

    # задати інтервал кодів
    price_code_from = int (input("З якого кода ціна?"))
    price_code_to = int(input("До якого кода ціна?"))

    # відбір списку цін
    filtered_prices = []
    for price in prices:
        if price_code_from <= price [0] <= price_code_to:
            filtered_prices.append(price)
    if len(filtered_prices) == 0:
        print("В списку клієнтів немає таких кодів")
        return

# вивід списку товарів
def show_tovari(tovari):
    """виводить список товарів по заданому інтервалу кодів
    """

    # задати інтервал кодів
    tovar_code_from = int (input("З якого кода товар?"))
    tovar_code_to = int(input("До якого кода товар?"))

    # відбір списку товарів
    filtered_tovari = []
    for tovar in tovari:
        if tovar_code_from <= tovari [0] <= tovar_code_to:
            filtered_tovari.append(tovar)
    if len(filtered_tovari) == 0:
        print("В списку товарів немає таких кодів")
        return

 
if __name__ == '__main__':
    prices = get_prices()
    tovari = get_tovar ()
    
    pass

