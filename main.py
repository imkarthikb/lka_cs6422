from steering_system import SteeringSystem
from alert_system import AlertSystem
from data_main import Data
import csv


def main():
    steering_system = SteeringSystem()
    alert_system = AlertSystem()

if __name__ == "__main__":
    data = Data()

    alldata = data.get_data("",
        "/home/amitsrivatsa/Assignments/CS6422 - Complex systems/LKM/cs6422_team3_LKA/data/vehicle_speed.csv",
        "/home/amitsrivatsa/Assignments/CS6422 - Complex systems/LKM/cs6422_team3_LKA/data/lka_status.csv",
        "/home/amitsrivatsa/Assignments/CS6422 - Complex systems/LKM/cs6422_team3_LKA/data/steering_override.csv")
        
    for data_item in alldata:
        print("x1:",data_item.x1)
        print("x2:",data_item.x2)
        print("Speed:",data_item.speed)
        print("Lka_status:",data_item.lka_onoff)
        print("Steering_override_status:",data_item.steering_override)

    main()
