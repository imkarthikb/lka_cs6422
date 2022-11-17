from enums.enum_steer_direction import SteerDirection


class SteeringModel:
    def __init__(self, direction: SteerDirection, steer_angle: float) -> None:
        self.direction = direction
        self.angle = steer_angle

    def __str__(self) -> str:
        return "x1: %f, x2: %f, speed: %f, steering_override: %s, lka_onoff: %s".format(self.x1, self.x2, self.speed, self.steering_override, self.lka_onoff)
