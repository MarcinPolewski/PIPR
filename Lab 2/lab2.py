
def main():

    print(power3(0))
    print(power3(1))
    print(power3(-3))
    print(power3(2e3))

    coeficients = (2, 2)
    print(calculateWielomian(coeficients, 4))

    print(get_time("adam", 5, 123456789))

    return 0


def calculateWielomian(coeficients, x):
    return coeficients[0]*x + coeficients[1]


def adding_number(a, b):
    return a+b


# parametr określający imię, numer zadania oraz czas wykonania zadania wyrazony w milisekundach
def get_time(name, problemNumber, executionTime):
    sec, milisec = divmod(executionTime, 1000)  # wykonuje wynik z dzielenia przez 1000 i reszty z dzielenia przez 1000 jednocześnie
    return f'{name} wykonał(a) zadanie nr {problemNumber} w {sec}.{milisec}s'


def get_middle_point(point_a, point_b):
    x = (point_a[0] + point_b[0])/2
    y = (point_a[1] + point_b[1])/2

    return (x, y)


def power3(a):
    return a*a*a


main()
