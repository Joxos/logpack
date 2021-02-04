from olylog import Logger
logger = Logger()
logger.register("network")
for i in range(int(input("Number to test: "))):
    logger.appenders["network"].append("info", "A new visitor!")
logger.delete("network", dump=True)
