from asyncio import sleep

import jsonpickle
import requests

from Measurement import Measurement
from Sensor import Sensor
from Serializer import Serializer
from position import Position


def read_sensors() -> Measurement:
    measurement = Measurement()
    sensor = Sensor()
    sensor.position = Position.Back
    sensor.x = 1
    sensor.y = 1
    sensor.value = 1
    measurement.sensors.append(sensor)
    measurement.sensors.append(sensor)
    measurement.sensors.append(sensor)
    measurement.sensors.append(sensor)
    return measurement


serializer = Serializer()
headers = {'content-type': 'application/json'}

while True:
    measurement = read_sensors()
    json = serializer.serialize(measurement)
    request = requests.post("http://localhost:8080/measurement", data=json,
                            headers=headers)
    print(json)
    sleep(700)
