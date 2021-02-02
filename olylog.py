"""
Interface of the olylog.
"""
from realization import Events


class Logger(object):
    def __init__(self, name):
        self.events = Events(name)

    def trace(self, msg):
        self.events.append("trace", msg)

    def debug(self, msg):
        self.events.append("debug", msg)

    def info(self, msg):
        self.events.append("info", msg)

    def warning(self, msg):
        self.events.append("warning", msg)

    def error(self, msg):
        self.events.append("error", msg)

    def fatal(self, msg):
        self.events.append("fatal", msg)

    def stop(self):
        self.events.stop()
