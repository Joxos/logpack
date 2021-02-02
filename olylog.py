import realization


class Logger(object):
    def __init__(self, name):
        self.events = realization.Events(name)

    def trace(self, msg):
        self.events.log(1, msg)

    def debug(self, msg):
        self.events.log(2, msg)

    def info(self, msg):
        self.events.log(3, msg)

    def warn(self, msg):
        self.events.log(4, msg)

    def error(self, msg):
        self.events.log(5, msg)

    def fatal(self, msg):
        self.events.log(6, msg)

    def stop(self):
        self.events.stop()
