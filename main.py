from asyncio import sleep

import jsonpickle
import requests

from Measurement import Measurement
from Sensor import Sensor
from Serializer import Serializer
from position import Position
import RPi.GPIO as GPIO
import time


def read_sensors() -> Measurement:
    measurement = Measurement()
    for pin in pin_numbers:
        measurement.sensors.append(Position.Back, get_value_from_sensor(pin))
    return measurement


def get_value_from_sensor(pin_number: int):
    input_pin = GPIO.input(pin_number)
    if not input_pin:
        return 1
    else:
        return 0


serializer = Serializer()
headers = {'content-type': 'application/json'}
pin_numbers = [14]
GPIO.setmode(GPIO.BCM)
for pin in pin_numbers:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    measurement = read_sensors()
    json = serializer.serialize(measurement)
    request = requests.post("http://localhost:8080/measurement", data=json,
                            headers=headers)
    print(json)
    sleep(700)
