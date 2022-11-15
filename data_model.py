from enum_steering_override import SteeringOveride
from enum_lka_status import LkaStatus

class DataModel:
    def __init__(self,x1:float,x2:float,speed:float,steering_override:SteeringOveride,lka_onoff:LkaStatus) -> None:
        self.x1 = x1
        self.x2 = x2
        self.speed = speed
        self.steering_override = steering_override
        self.lka_onoff = lka_onoff

    def __str__(self) -> str:
        return "x1: %f, x2: %f, speed: %f, steering_override: %s, lka_onoff: %s".format(self.x1, self.x2, self.speed, self.steering_override, self.lka_onoff)