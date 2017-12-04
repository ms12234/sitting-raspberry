from datetime import datetime


class Measurement:
    def __init__(self):
        self.timestamp = datetime.now()
        self.sensors = []
        self.grade = 0.0
