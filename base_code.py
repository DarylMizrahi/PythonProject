import csv


class CarLot:
    size = 0
    cars = []
    employee = []

    def load_csv_file(self, *args):
        with open(args[0]) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    print(f'\trow 0 = {row[0]} , row 1={row[1]} row 2={row[2]}. row 3={row[3]}')
                    line_count += 1
            print(f'Processed {line_count} lines.')

    def load_car_data(self, *args):
        pass

    def load_employee_data(self, *args):
        pass


class Vehicle:
    engine_type = ""
    number_of_wheels = 4
    color = "white"

    def __init__(self):
        pass

    def some_func(self):
        print("something")

    def __some_protected_function(self):
        pass


class Car(Vehicle):
    __brand = ""
    __engine_number = ""
    car_owner = ""

    def __init__(self, *args):
        self.__brand = args[0]
        self.__engine_number = args[1]
        super().__init__()

    def some_func(self):
        print("override - something from car")

    def get_engine_number(self):
        return self.__engine_number

    def set_car_owner(self, name):
        self.car_owner = name


class Bike(Vehicle):
    def __init__(self):
        super().__init__()

    def some_func(self):
        print("override - something from bike")


'''
build a decorator function that adds top line and underline arround output of function
'''


def my_decorator(func):
    def inner1():
        print("--------------------------")
        func()
        print("--------------------------")

    return inner1


@my_decorator
def test():
    print("hello")


car_lot = CarLot()
car_lot.load_csv_file("user.csv")


