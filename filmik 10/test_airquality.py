from airquality import Station, Sensor
import requests


def test_Station():
    data = {
        "id": 437,
        "stationName": "Skawina, os. Ogrody",
        "gegrLat": "49.971047",
        "gegrLon": "19.830422",
        "city": {
            "id": 834,
            "name": "Skawina",
            "commune": {
                "communeName": "Skawina",
                "districtName": "krakowski",
                "provinceName": "MAŁOPOLSKIE",
            },
        },
        "addressStreet": "os. Ogrody",
    }

    station = Station(data)

    assert station.id == 437
    assert station.stationName == "Skawina, os. Ogrody"
    assert station.gegrLat == "49.971047"
    assert station.gegrLon == "19.830422"


def test_Sensor():
    data = [
        {
            "id": 2001,
            "stationId": 285,
            "param": {
                "paramName": "dwutlenek azotu",
                "paramFormula": "NO2",
                "paramCode": "NO2",
                "idParam": 6,
            },
        },
        {
            "id": 2008,
            "stationId": 285,
            "param": {
                "paramName": "dwutlenek siarki",
                "paramFormula": "SO2",
                "paramCode": "SO2",
                "idParam": 1,
            },
        },
        {
            "id": 14367,
            "stationId": 285,
            "param": {
                "paramName": "benzen",
                "paramFormula": "C6H6",
                "paramCode": "C6H6",
                "idParam": 10,
            },
        },
        {
            "id": 16744,
            "stationId": 285,
            "param": {
                "paramName": "pył zawieszony PM10",
                "paramFormula": "PM10",
                "paramCode": "PM10",
                "idParam": 3,
            },
        },
        {
            "id": 26316,
            "stationId": 285,
            "param": {
                "paramName": "pył zawieszony PM2.5",
                "paramFormula": "PM2.5",
                "paramCode": "PM2.5",
                "idParam": 69,
            },
        },
        {
            "id": 28592,
            "stationId": 285,
            "param": {
                "paramName": "tlenek węgla",
                "paramFormula": "CO",
                "paramCode": "CO",
                "idParam": 8,
            },
        },
    ]
    sensor = Sensor(data[0])
    assert sensor.id == 2001
    assert sensor.stationId == 285
    assert sensor.paramName == "dwutlenek azotu"
    assert sensor.paramFormula == "NO2"
    assert sensor.paramCode == "NO2"
    assert sensor.idParam == 6
