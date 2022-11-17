# from steering_system import SteeringSystem
# from alert_system import AlertSystem
# from data_main import Data
from data.data_model import DataModel
# from enum_steer_direction import SteerDirection
# from models.steer_model import SteeringModel
# import csv
# import time


def main():
    pass
    # DataModel(10, 20, 40, 0, 1)
    # initial
    # curr_steering_state = SteeringModel(SteerDirection.CENTER, 0)
    # curr_lane_state = DataModel(26, 76, 40, 0, 1)

    # while(True):
    #     # get random steer override

    #     # get random speed

    #     # get random on_off

    #     # get next lane coordinates
    #     curr_lane_state = get_data(curr_steering_state, curr_lane_state)

    #     # process the inputs and calculate steer angle
    #     # curr_steering_state = calculate_steer_angle(curr_lane_state)

    #     # alerts take decisions

    #     time.sleep(1)


# def get_data(steer_wheel_direction: SteeringModel, current_state: DataModel) -> DataModel:
#     if steer_wheel_direction.direction == SteerDirection.CENTER and steer_wheel_direction.angle == 0:
#         return current_state
#     elif steer_wheel_direction.direction == SteerDirection.RIGHT and steer_wheel_direction.angle == 30:
#         return current_state


if __name__ == "__main__":
    main()
