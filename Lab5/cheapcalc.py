""" cheapcalc - a cheap CLI calculator """  # to jest doc string - definiuje
import sys
import cheapcalc_tools


def get_user_input(argv):
    operations = {
        "add": cheapcalc_tools.add,  # w pythone w strokturze danych mozna trzymac funkcje
        "subtract": cheapcalc_tools.subtract,
    }

    try:
        (
            _,
            command,
            arg_left,
            arg_right,
        ) = argv  # pierwsze to nazwa pliku, nie interesuje nas, przez konwencje oznaczamy to _
    except Exception:
        print("invalid arguments provided: comand, first_number, second_number")

    try:
        operation = operations[command]
    except:
        print("no such opperation")

    return operation, arg_left, arg_right


def main():
    """Parses CLI parameters and runs CheapCalc logic"""  # doc string do main - przekazujemy parametry

    operation, first_number, second_number = get_user_input(sys.argv)

    result = operation(float(first_number), float(second_number))

    print("The result is: ", result)


if (
    __name__ == "__main__"
):  # kod wykona się tylko gdy bezposrednio odpalimy ten plik, nie odpali sie przy imporcie
    main()
