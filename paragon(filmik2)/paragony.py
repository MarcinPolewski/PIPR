def get_description(name, price_zl, price_gr): return f'Price of {name} is {price_zl}.{price_gr}'
# zwraca nam stringa ; korzystamy z fstring


def print_description(name, price_zl, price_gr):
    description = f'Price of {name} is {price_zl}.{price_gr}'
    print(description)


def split_price(price):
    price_gr = price%100
    price_zl = price//100

    return price_zl, price_gr  #python automatycznie zwroci to jako krotke
    # return (price_zl, price_gr) <- mozna tak jak chce sie byc dokladnym


def print_description_2(name, price_in_gr):
    splitPrice = split_price(price_in_gr)
    description = f'Price of {name} is {splitPrice[0]}.{splitPrice[1]:02}' # wpisując :2 mówimy, zeby python zapisal to na dwoch bitach

    print(description)


print(get_description("orange", 4, 99))
print_description("orange", 5, 99)
print_description_2("bananana", 101)