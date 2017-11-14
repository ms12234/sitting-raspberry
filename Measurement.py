from _ast import List
from datetime import datetime

import Sensor


class Measurement:
    def __init__(self):
        self.timestamp: datetime = datetime.now()
        self.sensors: List[Sensor] = []
        self.grade: float = 0.0

