from asyncio import sleep

import RPi.GPIO as GPIO
import requests

from Measurement import Measurement
from Sensor import Sensor
from Serializer import Serializer
from position import Position


def read_sensors() -> Measurement:
    measurement = Measurement()
    for pin in pin_numbers:
        measurement.sensors.append(
            Sensor(Position.Back, get_value_from_sensor(pin)))
    return measurement


def get_value_from_sensor(pin_number):
    input_pin = GPIO.input(pin_number)
    if not input_pin:
        print("SDF")
        return 1
    else:
        return 0


serializer = Serializer()
headers = {'content-type': 'application/json'}
pin_numbers = [14]
GPIO.setmode(GPIO.BCM)
for pin in pin_numbers:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Starting to send data")
while True:
    measurement = read_sensors()
    json = serializer.serialize(measurement)
    request = requests.post("http://192.168.0.105:8080/measurement", data=json,
                            headers=headers)
    sleep(700)
