from position import Position


class Sensor:
    def __init__(self, position: Position, value: float):
        self.x: float = 0.0
        self.y: float = 0.0
        self.position: Position = position
        self.value: float = value

