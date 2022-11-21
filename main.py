from enums.enum_steering_override import SteeringOveride
from enums.enum_lka_status import LkaStatus
from enums.enum_steer_direction import SteerDirection
from models.lane_model import LaneModel
from models.steering_model import SteeringModel
import time
import random
import math


def main():
    # initial
    curr_steering_state = SteeringModel(SteerDirection.CENTER, 0, 0)
    curr_lane_state = get_random_lane()
    force_ctr = 0

    while(True):
        # get random steer override
        # steer_override = get_random_steer_override()
        steer_override = SteeringOveride.NO
        print(steer_override)
        if steer_override == SteeringOveride.YES:
            print('User is steering the vehicle manually')
        else:
            # get random speed
            # speed = get_random_speed()
            speed = 50

            print(speed)
            if speed < 5 or speed > 120:
                print('Lane keep assist does not work in the current the speed')
            else:
                # get random on_off
                # lka_status = get_random_lka_status()
                lka_status = LkaStatus.ON
                print(lka_status)
                if lka_status == LkaStatus.OFF:
                    print('Lane keep assist is turned off')
                else:
                    # get next lane coordinates
                    if curr_lane_state.x2 < curr_lane_state.x1 or curr_lane_state.x1 < 0 or curr_lane_state.x2 < 0 or curr_lane_state.x1 > 100 or curr_lane_state.x2 > 100:
                        print('Invalid lane coordinates', curr_lane_state)
                        curr_lane_state = get_random_lane()
                    else:
                        curr_lane_state = get_lane_data(
                            curr_steering_state, curr_lane_state, force_ctr >= 1)
                        print('Lane state', curr_lane_state)

                        if force_ctr >= 1:
                            force_ctr = 0

                        # process the inputs and calculate steer angle
                        curr_steering_state = calculate_steer_angle(
                            curr_lane_state)
                        print('Vehicle steers to - ', curr_steering_state)

                        if curr_steering_state.direction == SteerDirection.CENTER:
                            force_ctr += 1

                    # alerts take decisions
        print('-----------')
        time.sleep(1)


def get_random_lane() -> LaneModel:
    random_x1 = random.randint(-10, 100)
    random_lane_width = random.choices(population=[30, 40, 50, 60])[0]
    random_x2 = random_x1 + random_lane_width

    return LaneModel(random_x1, random_x2)


def get_random_steer_override() -> SteeringOveride:
    return random.choices(population=[SteeringOveride.YES, SteeringOveride.NO], weights=[0.15, 0.85], k=1)[0]


def get_random_lka_status() -> LkaStatus:
    return random.choices(population=[LkaStatus.ON, LkaStatus.OFF], weights=[0.85, 0.15], k=1)[0]


def get_random_speed() -> int:
    return random.choices(population=[4, 5, random.randint(6, 119), 120], weights=[0.1, 0.1, 0.7, 0.1], k=1)[0]


def get_lane_data(steer_wheel_direction: SteeringModel, current_lane_state: LaneModel, new_state: bool) -> LaneModel:
    if new_state:
        new_dir = random.choices(['right', 'left'])[0]
        factor = random.randint(1, 6)
        if new_dir == 'right':
            return LaneModel(current_lane_state.x1 + factor, current_lane_state.x2 + factor)
        else:
            return LaneModel(current_lane_state.x1 - factor, current_lane_state.x2 - factor)
    elif steer_wheel_direction.direction == SteerDirection.CENTER and steer_wheel_direction.angle == 0:
        return current_lane_state
    elif steer_wheel_direction.direction == SteerDirection.RIGHT:
        steer_wheel_direction.horizontal_distance_centre -= 1
        return LaneModel(int(current_lane_state.x1 - 1), int(current_lane_state.x2 - 1))
    else:
        steer_wheel_direction.horizontal_distance_centre -= 1
        return LaneModel(int(current_lane_state.x1 + 1), int(current_lane_state.x2 + 1))


def calculate_steer_angle(lane_coordinates: LaneModel) -> SteeringModel:
    mid = lane_coordinates.x1 + (lane_coordinates.x2 - lane_coordinates.x1) / 2
    angle_radians = math.atan2(25-0, mid-50)
    dir = SteerDirection.CENTER
    if abs(mid) > 50:
        dir = SteerDirection.RIGHT
    elif abs(mid) < 50:
        dir = SteerDirection.LEFT
    return SteeringModel(dir, 90 - math.degrees(angle_radians), abs(50 - mid))


if __name__ == "__main__":
    main()
