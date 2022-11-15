from data_model import DataModel
import glob
import csv
import os

class Data:

    def __init__(self) -> None:
        pass


    def get_data(self,lc_patha: str, speed_path: str, steering_path : str , lka_path :str ) -> list[DataModel]:

        x1 = []
        x2 = []
        speed = []
        steer = []
        lka = []
        paths = []
        data_list = []
        final_list = []
        finaldata_list = []

        default_lcpath = "/home/amitsrivatsa/OneDrive/Desktop/Assignments/CS6422 - Complex systems/LKM/cs6422_team3_LKA/data/lane_coordinates.csv"
        default_speedpath = "/home/amitsrivatsa/OneDrive/Desktop/Assignments/CS6422 - Complex systems/LKM/cs6422_team3_LKA/data/lka_status.csv"
        default_steerpath = "/home/amitsrivatsa/OneDrive/Desktop/Assignments/CS6422 - Complex systems/LKM/cs6422_team3_LKA/data/steering_override.csv"
        default_lkapath = "/home/amitsrivatsa/OneDrive/Desktop/Assignments/CS6422 - Complex systems/LKM/cs6422_team3_LKA/data/vehicle_speed.csv"

        lc_patha = lc_patha if (lc_patha is not None ) and (lc_patha != "") else default_lcpath
        speed_path = speed_path if (speed_path is not None ) and (speed_path != "") else default_speedpath
        steering_path = steering_path if (steering_path is not None ) and (steering_path != "") else default_steerpath
        lka_path = lka_path if (lka_path is not None ) and (lka_path != "") else default_lkapath

        paths.extend([lc_patha])
        paths.extend([speed_path])
        paths.extend([steering_path])
        paths.extend([lka_path])

        for files in paths:
            with open(files) as file:
                reader = csv.reader(file, delimiter=",")
                data_list.extend(list(reader))
    
        flat_list_a = [item for sublist in data_list[::2] for item in sublist]
        flat_list_b = [item for sublist in data_list[1::2] for item in sublist]
        final_list.extend([flat_list_a])
        final_list.extend([flat_list_b])

        

        for files in final_list:
            x1 = files[0]
            x2 = files[1]
            speed = files[2]
            lka = files[3]
            steer = files[4]
            data = DataModel(x1,x2,speed,steer,lka)
            finaldata_list.append(data)

        return finaldata_list

    if __name__ == "__main__":
        data = get_data("/home/amitsrivatsa/OneDrive/Desktop/Assignments/CS6422 - Complex systems/LKM/cs6422_team3_LKA/data/lane_coordinates.csv",
        "/home/amitsrivatsa/OneDrive/Desktop/Assignments/CS6422 - Complex systems/LKM/cs6422_team3_LKA/data/vehicle_speed.csv",
        "/home/amitsrivatsa/OneDrive/Desktop/Assignments/CS6422 - Complex systems/LKM/cs6422_team3_LKA/data/lka_status.csv",
        "/home/amitsrivatsa/OneDrive/Desktop/Assignments/CS6422 - Complex systems/LKM/cs6422_team3_LKA/data/steering_override.csv")

        for data_item in data:
            print(data_item.lka_onoff) 
            
    
        
