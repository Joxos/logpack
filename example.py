from olylog import Logger
logger = Logger()
logger.register("network")
for i in range(int(input("Number to test: "))):
    logger.append("network", "info", "A new visitor!")
logger.dump("network")
