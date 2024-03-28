tax_groups = {
    'Banana': 'A',
    'Toilet Paper': 'B',
    'Bread': 'E'
}

tax_rates = {
    'A': 12,
    'B': 8,
    'E': 22
}

item_prices = {
    'Banana': 50,
    'Toilet Paper': 1000,
    'Bread': 500
}


# use a single function returning div mod !!!
def get_formated_price(price):
    """
    takes price as int in gr and return string (looking like a float)
    """
    return f"{price//100}.{(price % 100):02}zl"


def cash_register_input():
    receipt = []
    for i in range(3):
        name, quantity = input("name;quantity: ").split(';')
        receipt.append((name, int(quantity)))
    return receipt


def generate_receipt(receipt):
    i = 1  # indeks iteracji pentli
    total_tax = 0
    total_value = 0

    for name, quantity in receipt:
        tax_group = tax_groups.get(name, "n/a")
        tax_rate = tax_rates.get(tax_group, 'n/a')
        price = item_prices.get(name, -1)

        total_item_value = quantity * price
        total_item_tax = int(total_item_value*(tax_rate/100))

        total_tax += total_item_tax
        total_value += total_item_value
 
        print(f"{i:3}. {name:20} {get_formated_price(total_item_tax):>10} {get_formated_price(total_item_value):>10} {tax_group}")
        i += 1

    print(50*'-')
    print(f"total {get_formated_price(total_tax):>30} {get_formated_price(total_value):>10}")


receipt = [
    ("Banana", 10),
    ("Bread", 2),
    ("Toilet Paper", 1)
]


generate_receipt(receipt)
