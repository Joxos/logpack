import json
import os
import datetime
from collections import OrderedDict


def get_time():
    return datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S.%f]")


class Event:
    def __init__(self, level, msg):
        self.time = get_time()
        self.level = level
        self.msg = msg


class Appender(object):
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
        # if there is no "settings.json", then warn the user
        if not os.path.exists("./settings.json"):
            self.append(
                "warning", "Can't find settings.json. Use default instead.")
        # read the settings
        self.settings = Settings(name)

    def append(self, level, msg):
        if self.is_running:
            self.events.append(Event(level, msg))

    def format(self):
        if self.settings.format == "log":
            # splicing strings
            msg = ""
            for event in self.events:
                msg += event.time+'['+event.level+']'+' '+event.msg+'\n'
            return msg
        if self.settings.format == "json":
            # add key-value
            msg = OrderedDict()
            for event in self.events:
                msg[event.time] = {"level": event.level, "message": event.msg}
            return json.dumps(msg, indent=2)


class Settings(object):
    '''
    Settings reader.
    '''

    def __init__(self, name):
        # default settings
        self.path = "./log/"
        self.format = "log"
        self.output = "file"
        # if exists "settings.json"
        if os.path.exists("./settings.json"):
            # read the settings
            with open("./settings.json", 'r') as json_settings:
                settings = json.loads(json_settings.read())
            # if have own settings
            if name in settings.keys():
                # read all
                own_settings = settings[name]
                if "path" in own_settings.keys():
                    self.path = own_settings["path"]
                if "format" in own_settings.keys():
                    self.format = own_settings["format"]
                if "output" in own_settings.keys():
                    self.output = own_settings["output"]
