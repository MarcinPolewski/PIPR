def split_price(price):
    price_gr = price % 100
    price_zl = price // 100

    return price_zl, price_gr  # python automatycznie zwroci to jako krotke
    # return (price_zl, price_gr) <- mozna tak jak chce sie byc dokladnym


def get_description(name, price):
    price_parts = split_price(price)
    return f'Price of {name} is {price_parts[0]}.{price_parts[1]:02}'
# zwraca nam stringa ; korzystamy z fstring


def print_description(name, price_in_gr):
    description = get_description(name, price_in_gr)
    print(description)


def format_price(price):
    zl, gr = split_price(price)
    return f"{zl}.{gr:02}"


def get_product():
    product_name = input("Product name: ")
    product_price = input("Product price: ")

    return product_name, int(product_price)


def get_total_price(receipt):  # przyjmuje listę - paragon; zwraca wartość paragonu
    """
    Receives list of items in receipt as input.
    Returns total value of receipt. 
    """
    temp_sum = 0
    for name, price in receipt:
        temp_sum += price
    return temp_sum


def print_receipt(receipt):

    if not receipt:
        print("receipt is empty")
        return 

    for i in range(len(receipt)): 
        print(f"{i:3}. {receipt[i][0]:15}\t{format_price(receipt[i][1]):>6} {get_tax_group(receipt[i][0])}")
    print("-"*30)
    print(f"TOTAL: {format_price(get_total_price(receipt)):>23}")


def get_product_2():
    product_prices = {
        "Bananas": 800,
        "Oranges": 599,
        "Bread": 328, 
    }

    name = input("name: ")
    quantity = int(input("quantity: "))
    price = product_prices.get(name, 0)

    return name, (price*quantity)


def get_tax_group(name):
    """ 
    receives product's name and returns its tax group
    """
    tax_group_a = {'bread', 'milk', 'chocolate', 'Bananas'}
    tax_group_b = {'soap', 'sunlotion', 'tooth paste', 'Oranges'}
    tax_group_e = {"fuel", 'propan-butan'}
    if name in tax_group_a:
        return 'a'
    elif name in tax_group_b:
        return 'b'
    elif name in tax_group_e:
        return 'e'
    return 'n/a'


my_receipt = [
    ('Bananas', 499),
    ('Oranges', 1803),
    ('Milk', 315)
]


print(get_product_2())

# print_receipt(my_receipt)
# my_total_value = get_total_price(my_receipt)
# print(f"value of the receipt is {my_total_value[0]}zł and {my_total_value[1]}gr")
