import jsonpickle
import requests

from Measurement import Measurement
from Sensor import Sensor
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


while True:
    measurement = read_sensors()
    json = jsonpickle.encode(measurement)

    r = requests.post("http://localhost:8080/measurement",
                      data={'number': 12524, 'type': 'issue',
                            'action': 'show'})
    print(r.status_code, r.reason)
