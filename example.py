from olylog import Logger
logger = Logger()
logger.register("network")
logger.appenders["network"].append("info", "Network initialized successfully.")
logger.appenders["network"].stop()
