from classes import file_handler
from classes import user
from pathlib import Path
from classes import log
import os
import csv


class Carlot:
    def __init__(self):
        self.list_of_vehicles = []
        self.user = user.User()
        self.file_handler = file_handler.FileHandler()
        self.pathUser = Path(__file__)
        self.log = log.Logger()

    def update_salary_by_name(self, salary, employee_name):
       # employee = {}
        role=self.user.user_auth(input("first-name"), input("password"))
        if role == "admin":
            newpath = os.path.join("/Users/darylmizrahi/Desktop/PythonProjectITC/csv_file/user.csv")
            self.file_handler.load_from_csv_file(newpath)
            for x in self.file_handler.employee:
                if x ["first_name"] == employee_name:
                    employee = x
            if employee:
                employee["salary"]=str(salary)
                remove_value = self.file_handler.remove_from_csv(newpath, employee["id"])
                if remove_value == True:
                    add_value = self.file_handler.append_to_csv(newpath, employee)
                    if add_value == True:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def add_to_fleet(self, path_external):
        try:
            with open(path_external, "r") as csv_external:
                csv_reader = csv.reader(csv_external)
                external_headers = next(csv_reader)
            with open("/Users/darylmizrahi/Desktop/PythonProjectITC/csv_file/vehicle.csv", "r")  as csv_file:
                csv_reader = csv.reader(csv_file)
                internal_headers = next(csv_reader)
            if external_headers != internal_headers:
                return False

            external_file = open(path_external, 'r')
            internal_file = open("/Users/darylmizrahi/Desktop/PythonProjectITC/csv_file/vehicle.csv", "r").readlines()

            if external_file != internal_file:
                with open("/Users/darylmizrahi/Desktop/PythonProjectITC/csv_file/vehicle.csv", "a") as csv_append:
                    next(external_file)
                    for row in external_file:
                        csv_append.writelines(row)
                return True
        except Exception as error:
            print(error)
            raise

    def get_fleet_size(self):
        try:
            with open("/Users/darylmizrahi/Desktop/PythonProjectITC/csv_file/vehicle.csv", "r") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=",")
                next(csv_file)
                for row in csv_reader:
                    self.list_of_vehicles.append(row)
                #print(self.list_of_vehicles)
                return len(self.list_of_vehicles)
        except Exception as e:
            print(e)
            raise


car = Carlot()
print(car.get_fleet_size())



#car = Carlot()
#print(car.add_to_fleet("/Users/darylmizrahi/Desktop/PythonProjectITC/csv_file/new_vehicles.csv"))




        #newpath = os.path.join(self.pathUser.parent.parent, "csv_file/vehicle.csv")
        #newpath = "/Users/darylmizrahi/Desktop/PythonProjectITC/csv_file/vehicle.csv"
        #print(newpath)
        #self.file_handler.load_from_csv_file(newpath)
        #origin_vehicle = self.file_handler.employee
        #self.file_handler.load_from_csv_file(path_external)
        #vehicle_lot_test = self.file_handler.employee
        #if vehicle_lot_test[0].keys == origin_vehicle[0].keys():
            #for dict in vehicle_lot_test:
                #self.file_handler.append_vehicle_to_csv(newpath, dict)

#carlot = Carlot()
#value = carlot.update_salary_by_name("5k", "Elie")
#print(value)


#carlot.add_to_fleet("/Users/darylmizrahi/Desktop/PythonProjectITC/csv_file/new_vehicles.csv")

    #def get_fleet_size(self):
        #try:
            #new_path = os.path.join(self.pathUser.parent.parent, "/Users/darylmizrahi/Desktop/PythonProjectITC/csv_file/vehicle.csv")
            #self.file_handler.load_from_csv_file(new_path)
            #return len(self.file_handler.employee)
        #except Exception as error:
            #print(error)