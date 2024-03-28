import airquality
import sys
from random import choice
from matplotlib import pyplot as plt
import argparse

# biblioteki mogą mieć rozne backendy
# mathplotlib.us ("Qt5Agg") # ustawiamy inny backend


def find_station(id):
    for station in airquality.get_station():
        if station.id == id:
            return station
    return None


def list_stations(args):
    # wypisuje wszystkie stacje w których nazwie jest
    # określony pattern
    pattern = args.list_stations
    all_stations = airquality.get_station()
    for station in all_stations:
        if pattern == " " or pattern in station.stationName:
            print(f"{station.id}\t{station.stationName}")


def list_sensors(args):
    station_id = float(args.list_sensors)
    station = find_station(station_id)

    # jeśli udało się znalźć taką stace
    if station:
        for sensor in station.sensors():
            print(f"{sensor.id}\t{sensor.paramName}")


def main(arguments):
    parser = argparse.ArgumentParser()

    # const - wartosc domyslna, jak nie podamy argumentu
    # nargs - ile argumentów się spodziewamy, ? - często się uzywa
    parser.add_argument("--list-stations", nargs="?", const=" ")
    # przy tej fladze zawsze musi być wartość
    parser.add_argument("--list-sensors")
    args = parser.parse_args(arguments[1:])
    # pomijamy pierwszy element, bo to zawsze nazwa pliku

    # jeśli ta wartość istnieje w args
    if args.list_stations:
        list_stations(args)
        return

    if args.list_sensors is not None:
        list_sensors(args)

    all_stations = airquality.get_station()
    station = choice(all_stations)
    all_sensors = station.sensors()
    # pomijamy, bo zaburza inne wartosci
    for sensor in all_sensors:
        if sensor.paramCode == "CO":
            continue
        readings = sensor.readings()
        keys = [
            reading.date.strftime("%d.%m.%Y %H:%M") for reading in readings
        ]  # formatujemy tate
        values = [reading.value for reading in readings]
        plt.plot(keys, values, "o-", label=sensor.paramName, markersize=3)
        # podajemy formatowanie wykresu dla "--" dostaniemy linie przerywane, dla ":" są kropli
        # dla "o" dostaniemy punkty, dla "o-" moemy kropli połączyć
        # markersize ustala nam wielkosc kropli

    plt.title(label=station.stationName)  # włącza tytuł wykresu
    plt.legend()  # włącza legende, jak opis osi
    plt.xticks(rotation=30, fontsize="xx-small", horizontalalignment="right")
    # obracamy opis poziomej osi i ustalamy wielkosc liter
    # wyrównujemy nie środkiem, tylko do prawej
    # if parser.save:
    #     plt.savefig("args.save", format="pdf")  # zapis do pdf
    # else:
    plt.savefig("station.stationName", format="pdf")  # zapis do pdf
    plt.show()


if __name__ == "__main__":
    main(sys.argv)
