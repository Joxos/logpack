"""
Interface of the olylog.
"""
import os
from sys import exit
from realization import Logger


class LogManager:
    def __init__(self):
        self.appenders = {}

    def register(self, name):
        self.appenders[name] = Logger(name)
        self.append(name, "info", "Register and start the logger.")

    def append(self, name, level, msg):
        self.appenders[name].append(level, msg)

    def dump(self, name):
        # ensure the directory is exsist
        if not os.path.exists(self.appenders[name].settings.destination):
            self.append(name, "warning",
                        "Can't find the target directory. Creating...")
            try:
                os.mkdir(self.appenders[name].settings.destination)
            except:
                self.append(name, "fatal",
                            "Can't create the target directory, exit.")
                exit(1)
            else:
                self.append(
                    name, "info", "Successfully create the target directory.")
        self.append(name, "info", "Record before dump the events.")
        with open(self.appenders[name].settings.destination+name, 'a') as f:
            f.write(self.appenders[name].format())
        # clear the event list
        self.appenders[name].events = []

    def stop(self, name, dump=True):
        self.append(name, "info", "Stop logging.")
        if dump:
            self.dump(name)
        self.appenders[name].is_running = False

    def start(self, name):
        self.appenders[name].is_running = True
        self.append(name, "info", "Start logging.")

    def delete(self, name, dump=True):
        self.append(name, "info", "Delete the logger.")
        if dump:
            self.dump(name)
        del self.appenders[name]
