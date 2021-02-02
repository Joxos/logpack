import olylog
logger = olylog.Logger("logger")
# logger.trace("Hello, trace!")
# logger.debug("Hello, debug!")
# logger.info("Hello, info!")
# logger.warn("Hello, warn!")
# logger.error("Hello, error!")
# logger.fatal("Hello, fatal!")
num = input("Number of the test: ")
for i in range(int(num)):
    logger.trace("A")
logger.stop()
