import csv
import collections
from classes import log
Logger = log.Logger


class FileHandler:
    def __init__(self):
        self.employee = []
        self.log = Logger()
        self.collections = collections

    def load_from_csv_file(self, *args):
        try:
            self.employee = []
            employee = {}
            with open(args[0]) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        header = row
                        line_count += 1
                    else:
                        i = 0
                        employee = {}
                        for x in header:
                            employee[x] = row[i]
                            i += 1
                        self.employee.append(employee)
                self.log.add_to_log("We went through the csv file (user)""\n")

        except Exception as error:
            print("There is an error : " + str(error))
            self.log.add_to_log(" We tried to go through the csv file user but there is an error""\n")

    def append_to_csv(self, path, data):
        keys = []
        for key in data.keys():
            keys.append(key)
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    if self.collections.Counter(row) == self.collections.Counter(keys):
                        line_count += 1
                    else:
                        return False
                else:
                    if data["id"] == row[0]:
                        return False
        with open(path, "a") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerow([data["id"], data["first_name"], data["last_name"], data["password"], data["position"], data["salary"], data["role"]])
            self.log.add_to_log("A new person was added to csv.file (user)""\n")

    def remove_from_csv(self, path, id): #Exercise1 daily mini project2
        try:
            lines = list()
            value = False
            with open(path, 'r') as readFile:
                reader = csv.reader(readFile)
                for row in reader:
                    if row[0] != str(id):
                        lines.append(row)
                    else:
                        value = True
                        self.log.add_to_log("added a new user to user csv file \n")
            with open(path, 'w', newline="") as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(lines)
            return value
        except Exception as e:
            self.log.add_to_log("Tried to add a new user to csv file user but there was an error \n")

            print("There was an error: " + str(e))

    def update_csv(self, path, id, row):
        value = self.remove_from_csv(path, id)
        print(value)
        if value == True:
            row["id"]=str(id)
            print(row)
            appendValue = self.append_to_csv(path, row)
            if appendValue == True:
                self.log.add_to_log("update a user on csv user file")
                return True
            else:
                self.log.add_to_log("Tried to update a user but there was an error")
                return False
        else:
            return False


file = FileHandler()
data = {
    "id": "30",
    "first_name": "Max",
    "last_name": "TEST",
    "password": "3333333",
    "position": "student",
    "salary": "0",
    "role": "admin"

}


#file.append_to_csv("/Users/darylmizrahi/Desktop/PythonProjectITC/csv_file/user.csv", data)

#file = FileHandler()
#file.load_from_csv_file("/Users/darylmizrahi/Desktop/PythonProjectITC/csv_file/user.csv", data)

#remove_value = file.remove_from_csv("/Users/darylmizrahi/Desktop/PythonProjectITC/csv_file/user.csv", "25")
#print(remove_value)


#file.update_csv("/Users/darylmizrahi/Desktop/PythonProjectITC/csv_file/user.csv", "22", row)





