"""
Interface of the olylog.
"""
from realization import Appender


class Logger:
    def __init__(self):
        self.appenders = {}

    def register(self, name):
        self.appenders[name] = Appender(name)
