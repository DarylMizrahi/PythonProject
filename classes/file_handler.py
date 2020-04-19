import csv
from classes import log
Logger = log.logger


class FileHandler:
    def __init__(self):
        self.employee = []
        self.log = Logger()

    def load_from_csv_file(self, *args):
        try:
            with open(args[0]) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        line_count += 1
                    else:
                        employee = {
                            "id": row[0],
                            "first_name": row[1],
                            "last_name": row[2],
                            "password": row[3],
                            "position": row[4],
                            "salary": row[5],
                            "role": row[6],
                        }
                        self.employee.append(employee)
                        self.log.add_to_log("We went through the csv file (user)""\n")

        except Exception as error:
            print("There is an error : " + str(error))

    def append_to_csv(self, path, data):
        keys = []
        for key in data.keys():
            keys.append(key)
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    if row == keys:
                        line_count += 1
                    else:
                        return False
                else:
                    if(data["id"]==row[0]):
                        return False
        with open(path, "a") as csv_file:
            try:
                csv_writer = csv.writer(csv_file, delimiter=',')
                csv_writer.writerow([data["id"], data["first_name"], data["last_name"], data["password"], data["position"], data["salary"], data["role"]])
                self.log.add_to_log("A new person was added to csv.file (user)""\n")
            except Exception as e:
                print(e)
                raise

file = FileHandler()
data = {
    "id": "22",
    "first_name": "Daryl",
    "last_name": "Mizrahi",
    "password": "3333333",
    "position": "student",
    "salary": "0",
    "role": "student"

}



#file = FileHandler()
file.append_to_csv("/Users/darylmizrahi/Desktop/PythonDay1/csv_file/user.csv", data)
#print(file.employee)


