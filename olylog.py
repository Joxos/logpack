"""
Interface of the olylog.
"""
import os
from sys import exit
from realization import Appender


class Logger:
    def __init__(self):
        self.appenders = {}

    def register(self, name):
        self.appenders[name] = Appender(name)

    def stop(self, name):
        if self.appenders[name].is_running:
            self.appenders[name].append("info", "Stop logging.")
            self.dump(name)
            self.appenders[name].is_running = False

    def delete(self, name, dump=True):
        if dump:
            self.stop(name)
        del self.appenders[name]

    def dump(self, name):
        if self.appenders[name].is_running:
            # ensure the directory is exsist
            if not os.path.exists(self.appenders[name].settings.path):
                self.appenders[name].append(
                    "warning", "Can't find the target directory. Creating...")
                try:
                    os.mkdir(self.appenders[name].settings.path)
                except:
                    self.appenders[name].append(
                        "fatal", "Can't create the target directory, exit.")
                    exit(1)
                else:
                    self.appenders[name].append(
                        "info", "Successfully create the target directory.")
            self.appenders[name].append(
                "info", "Record before dump the events")
            with open(self.appenders[name].settings.path+name, 'a') as f:
                f.write(self.appenders[name].format())
            # clear the event list
            self.appenders[name].events = []
