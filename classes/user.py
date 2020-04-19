from classes import file_handler

FileHandler = file_handler.FileHandler


class User:
    def __init__(self):
        self.result = FileHandler()

    def user_auth(self, name, password):
        try:
            self.result.load_from_csv_file("/Users/darylmizrahi/Desktop/PythonDay1/csv_file/user.csv")
            for x in self.result.employee:
                if x["first_name"] == name and x["password"] == password:
                    return x["role"]
            return False

        except Exception as error:
            print("There is an error : " + str(error))


user = User()
role = user.user_auth("amir", "12345678")
print(role)