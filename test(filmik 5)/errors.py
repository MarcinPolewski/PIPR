# def div_or_none(a, b):
#     if b == 0:
#         return None
#     return a / b


# # outparam - wynik przekazujemy przez parametr, przydatne np w c
# # zwracamy tylko czy udało nam się znaleźć wynik
# def div_outparam(a, b, wynik):
#     if b == 0:
#         return False
#     wynik = a / b
#     return True


# def div(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError as e:
#         pass


# retult = div(1, 0)


# def div(a, b):
#     return a / b


# try:
#     result = div("adjslkfj", 0)
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)


# def div(a, b):
#     return a / b


# at_end = False
# while not at_end:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     try:
#         result = div(a, b)
#         print(f"{a}/{b} = {result}")
#     except ZeroDivisionError:
#         print("Division inpossible, becuase b == 0")
#         at_end = True


# def div(a, b):
#     return a / b


# at_end = False
# while not at_end:
#     try:
#         a = int(input("Enter first number: "))
#         b = int(input("Enter second number: "))
#     except ValueError:
#         print("incorrect input")
#         at_end = True
#     try:
#         result = div(a, b)
#         print(f"{a}/{b} = {result}")
#     except ZeroDivisionError:
#         print("Division inpossible, becuase b == 0")
#         at_end = True


# program pyta dopóki uzytkownik nie poda liczby


def div(a, b):
    return a / b


def input_value(prompt=""):
    correct_input = False
    a = 0
    while not correct_input:
        correct_input = True
        try:
            a = int(input("Enter first number: "))
        except TypeError:
            print("nonconvertable value provided! Try again")
            correct_input = False

    return a


# lepsza wersja


def input_value2(prompt=""):
    while True:
        try:
            text = input(prompt)
            return int(text)
        except ValueError:
            print("incorrect value entered")


at_end = False
while not at_end:
    a = input_value2("first number: ")
    b = input_value2("second number: ")

    try:
        result = div(a, b)
        print(f"{a}/{b} = {result}")
    except ZeroDivisionError:
        print("Division inpossible, becuase b == 0")
        at_end = True
