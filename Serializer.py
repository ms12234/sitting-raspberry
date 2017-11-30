from datetime import datetime


class Serializer:
    def serialize(self, measurement) -> str:
        seconds = (measurement.timestamp - datetime(1970, 1, 1)).total_seconds()

        timestamp = "\"time\":" + str(round(seconds)) + ","
        sensors = "\"sensors\": ["
        for sensor in measurement.sensors:
            x = "\"x\": {0},".format(sensor.x)
            y = "\"y\": {0},".format(sensor.y)
            position = "\"position\": \"{0}\",".format(sensor.position.name)
            value = "\"value\": {0}".format(sensor.value)
            sensors += "{" + x + y + position + value + "},"

        sensors = sensors[:-1]
        sensors += "]"
        return "{" + timestamp + sensors + "}"
