from olylog import Logger
logger = Logger()
logger.register("network")
logger.append("network", "info", "A new visitor!")
logger.stop("network")
logger.append("network", "fatal",
              "Can I append a log event when the appender is stopped?")
logger.start("network")
logger.append("network", "info", "Now I think I can.")
# speed test code:
# for i in range(int(input("Number to test: "))):
#     logger.append("network", "info", "A new visitor!")
logger.destroy("network")
