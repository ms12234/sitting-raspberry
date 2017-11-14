from position import Position


class Sensor:
    def __init__(self):
        self.x: float = 0.0
        self.y: float = 0.0
        self.position: Position = Position.Back
        self.value: float = 0.0

