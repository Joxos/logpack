"""
Interface of the olylog.
"""
import os
from datetime import datetime
from time import localtime, strftime
from sys import exit
from logcore import Logger


class Event:
    def __init__(self, level, msg):
        # we think the server won't move when running
        # so we execute it once, and no more
        self.time_zone = strftime("%z", localtime())
        self.time = datetime.now().strftime("[%F %T:%f ")+self.time_zone+']'
        self.level = level
        self.msg = msg


class LogManager:
    def __init__(self):
        self.appenders = {}

    def register(self, name):
        self.appenders[name] = Logger(name)
        self.append(name, "info", "Register and start the logger.")

    def append(self, name, level, msg):
        if self.appenders[name].is_running:
            self.appenders[name].events.append(Event(level, msg))

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
        # add a recode before dump the events
        self.append(name, "info", "Record before dump the events.")
        # dump them
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
