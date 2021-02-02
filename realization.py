import json
import os
import time
import datetime


class Events(object):
    '''
    Logical of events.
    '''

    def __init__(self, name):
        # events
        self.events = []
        # start logging events
        self.events.append(
            (datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S.%f]"), 0, "Start logging."))
        # tiger of is running
        self.running = True
        # set the name of the logger
        self.name = name
        # read the settings
        self.settings = Settings(name)
        # if there is no "settings.json", then warn the user
        if not os.path.exists("./settings.json"):
            self.events.append((datetime.datetime.now().strftime(
                "[%Y-%m-%d %H:%M:%S.%f]"), 0, "Can't find settings.json. Use default instead."))

    def log(self, level, msg):
        '''
        Log the message.
        '''
        # if the logger is running
        if self.running:
            # ATTENTION: DO NOT USE "level<=6 and level>=0"!
            if level == 0 or level == 1 or level == 2 or level == 3 or level == 4 or level == 5 or level == 6:
                # log the events
                self.events.append(
                    (datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S.%f]"), level, msg))
        # write it
        Destination(self.name, Formatter(self.name, self.events))
        # clear the events list after writing
        self.events = []

    def stop(self):
        '''
        Stop the logger.
        '''
        # set the tiger
        self.running = False
        # stop logging events
        self.events.append(
            (datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S.%f]"), 0, "Stop logging."))
        # write it
        Destination(self.name, Formatter(self.name, self.events))
        # clear the events list after writing
        self.events = []


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


def Destination(name, msg):
    '''
    Write real message into file.
    '''
    settings = Settings(name)
    if settings.format == "log":
        if settings.output == "file":
            with open(settings.path+name+".log", 'a') as write_file:
                write_file.write(msg)
    elif settings.format == "json":
        if settings.output == "file":
            with open(settings.path+name+".json", 'a') as write_file:
                write_file.write(json.dumps(msg, indent=2))


def Formatter(name, events):
    '''
    Format logic of events into real message.
    '''
    settings = Settings(name)
    if not os.path.exists(settings.path):
        os.mkdir(settings.path)
    if settings.format == "log":
        # splicing strings
        msg = ""
        for i in events:
            if i[1] == 0:
                msg += "[LOGGER]"
                msg += str(i[0])
                msg += ' '
                msg += str(i[2])
                msg += '\n'
            elif i[1] == 1:
                msg += "[TRACE] "
                msg += str(i[0])
                msg += ' '
                msg += str(i[2])
                msg += '\n'
            elif i[1] == 2:
                msg += "[DEBUG] "
                msg += str(i[0])
                msg += ' '
                msg += str(i[2])
                msg += '\n'
            elif i[1] == 3:
                msg += "[INFO]  "
                msg += str(i[0])
                msg += ' '
                msg += str(i[2])
                msg += '\n'
            elif i[1] == 4:
                msg += "[WARN]  "
                msg += str(i[0])
                msg += ' '
                msg += str(i[2])
                msg += '\n'
            elif i[1] == 5:
                msg += "[ERROR] "
                msg += str(i[0])
                msg += ' '
                msg += str(i[2])
                msg += '\n'
            elif i[1] == 6:
                msg += "[FATAL] "
                msg += str(i[0])
                msg += ' '
                msg += str(i[2])
                msg += '\n'
        return msg
    if settings.format == "json":
        # add key-value
        msg = {}
        for i in events:
            if i[1] == 0:
                msg[i[0]] = ("LOGGER", i[2])
            elif i[1] == 1:
                msg[i[0]] = ("TRACE", i[2])
            elif i[1] == 2:
                msg[i[0]] = ("DEBUG", i[2])
            elif i[1] == 3:
                msg[i[0]] = ("INFO", i[2])
            elif i[1] == 4:
                msg[i[0]] = ("WARN", i[2])
            elif i[1] == 5:
                msg[i[0]] = ("ERROR", i[2])
            elif i[1] == 6:
                msg[i[0]] = ("FATAL", i[2])
        return msg
