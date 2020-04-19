import datetime
import os


class Logger:

    def add_to_log(self, msg):
        f = open("/Users/darylmizrahi/Desktop/PythonDay1/log/log.text", "a+")
        date = datetime.datetime.now()
        date = date.strftime("%d/%m%/%Y , %H:%M:%S")
        f.write(date + msg)


log = Logger()
