import requests
from datetime import datetime

urls = {
    "findAll": "https://api.gios.gov.pl/pjp-api/rest/station/findAll",
    "sensors": "https://api.gios.gov.pl/pjp-api/rest/station/sensors/{stationId}",
    "getData": "https://api.gios.gov.pl/pjp-api/rest/data/getData/{sensorId}",  # https://api.gios.gov.pl/pjp-api/rest/data/getData/50
    "index": "https://api.gios.gov.pl/pjp-api/rest/aqindex/getIndex/{stationId}",
}


def get_station():
    stations = requests.get(urls["findAll"]).json()
    return [Station(station) for station in stations]
    # all_stations = []
    # for station_data in stations:
    #     station = Station(station_data)
    #     all_stations.append(station)
    # return all_stations


class AirApiObject:
    def __init__(self, data):
        self._data = data

    @property
    def id(self):
        pass
        return self._data["id"]

    def _get(self, key):
        # uzywamy get zamiast [], zeby jak wartosc
        # nie bedzie istniala, dostac none, a zeby nie wykrzaczylo
        return self._data.get(key)


class Station(AirApiObject):
    @property
    def stationName(self):
        return self._get("stationName")

    @property
    def gegrLat(self):
        return self._get("gegrLat")

    @property
    def gegrLon(self):
        return self._get("gegrLon")

    @property
    def pos(self):
        lat = self._get("gegrLat")
        lon = self._get("gegrLon")
        return (float(lat), float(lon))

    @property
    def city_name(self):
        return self._get("city")["name"]

    @property
    def city_data(self):
        return self._get("city")

    def sensors(self):
        """sends an requests"""
        all_sensors = requests.get(urls["sensors"].format(stationId=self.id)).json()
        pass
        return [Sensor(sensor) for sensor in all_sensors]
        # return all_sensors.json()  # zwracamy wartosc w formie pythonowej listy

    def __str__(self):
        return self._get("stationName")


class Sensor(AirApiObject):
    # curl -s https://api.gios.gov.pl/pjp-api/rest/station/sensors/285 | jq

    @property
    def stationId(self):
        return self._get("stationId")

    @property
    def param(self):
        return self._get("param")

    @property
    def paramName(self):
        return self._get("param").get("paramName")

    @property
    def paramFormula(self):
        return self.param.get("paramFormula")

    @property
    def paramCode(self):
        return self.param.get("paramCode")

    @property
    def idParam(self):
        return self.param.get("idParam")

    def readings(self):
        # result is a dictionary
        result = requests.get(urls["getData"].format(sensorId=self.id)).json()

        key = result["key"]
        values = result["values"]
        pass
        # list comprehension
        return [
            Reading(self, key, datetime.fromisoformat(value["date"]), value["value"])
            for value in values
        ]


class Reading:
    """single reading from sensor"""

    def __init__(self, sensor, key, date, value):
        self._sensor = sensor
        self.key = key
        self.date = date
        self.value = value

    @property
    def sensor(self):
        return self._sensor
