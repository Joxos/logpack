import json
import os
from datetime import datetime
from time import localtime, strftime
from random import randint
from collections import OrderedDict


time_zone = strftime("%z", localtime())


def get_time():
    return datetime.now().strftime("[%F %T:%f ")+time_zone+']'


class Event:
    def __init__(self, level, msg):
        self.time = get_time()
        self.level = level
        self.msg = msg


class Logger(object):
    '''
    Logical of events.
    '''

    def __init__(self, name):
        # events
        self.events = []
        # set the name of the logger
        self.name = name
        # running tiger
        self.is_running = True
        # read the settings
        self.settings = Settings(name)

    def append(self, level, msg):
        if self.is_running:
            self.events.append(Event(level, msg))

    def format(self):
        if self.settings.output_format == "log":
            # splicing strings
            msg = ""
            for event in self.events:
                msg += event.time+'['+event.level+']'+' '+event.msg+'\n'
            return msg
        if self.settings.output_format == "json":
            # add key-value
            msg = OrderedDict()
            for event in self.events:
                msg[event.time + str(randint(0, 1000))
                    ] = {"level": event.level, "message": event.msg}
            return json.dumps(msg, indent=2)


class Settings(object):
    '''
    Settings reader.
    '''

    def __init__(self, name):
        # Default Settings:
        # destination
        # if it is a directory, the file name is the logger name
        # if it is a file, then will dump into it
        self.destination = "./log/"

        # output format
        # supported format:
        #     - log
        #     - json
        self.output_format = "log"

        # dump pause time
        # 0 or False: real-time dump
        # x: dump after x second(s)
        # True: disable the automatically dump feature
        self.dump_pause_time = 60

        if os.path.exists("./settings.json"):
            with open("./settings.json", 'r') as f:
                own_settings = json.load(f).get(name)
            if own_settings:
                keys = own_settings.keys()
                if "destination" in keys:
                    self.destination = own_settings["destination"]
                if "output_format" in keys:
                    self.output_format = own_settings["output_format"]
                if "dump_pause_time" in keys:
                    self.dump_pause_time = own_settings["dump_pause_time"]
