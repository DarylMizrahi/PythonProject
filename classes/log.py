import datetime
import os

from pathlib import Path


class Logger:
    def __init__(self):
        self.path = Path(__file__)

    def add_to_log(self, msg):
        f = open(os.path.join(self.path.parent.parent, "log/log.txt"), "a+")
        date = datetime.datetime.now()
        date = date.strftime("%d/%m%/%Y , %H:%M:%S")
        f.write(date + msg)


log = Logger()

#f = open("/Users/darylmizrahi/Desktop/PythonProjectITC/log/log.text", "a+")
