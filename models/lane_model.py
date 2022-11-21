from enums.enum_steering_override import SteeringOveride
from enums.enum_lka_status import LkaStatus


class LaneModel():
    def __init__(self, x1: int, x2: int) -> None:
        self.x1 = x1
        self.x2 = x2

    def __str__(self) -> str:
        return f"x1: {self.x1}, x2: {self.x2}"
