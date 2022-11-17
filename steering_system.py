from enum_steer_direction import SteerDirection


class SteeringSystem:
    def steer_vehicle(self, angle: float, direction: SteerDirection):
        print('Driver steers the vehicle towards %d by %f'.format(direction, angle))
