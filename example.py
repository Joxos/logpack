from logpack import LogManager


# there is an example of settings in settings.json
# you can try to customize it
# then start the tutorial

# create the manager
log_manager = LogManager()

# register the network logger
# settings will be load automatically
log_manager.register("network")

# append an info message
log_manager.append("network", "info", "A new visitor!")

# stop the network logger
# will dump the events automatically, use dump=False to disable
log_manager.stop("network")

# you can't append anything when a logger is disabled
log_manager.append("network", "fatal",
                   "Can I append a log event when the appender is stopped?")

# restart the network logger
log_manager.start("network")

# now you can append some messages
log_manager.append("network", "info", "Now I think I can.")
log_manager.append("network", "info", "A new visitor!")

# dump the messages
log_manager.dump("network")

# append something else
log_manager.append("network", "info", "A new user!")

# delete the logger
# will dump the events automatically, use dump=False to disable
log_manager.delete("network")

# now you've finished the tutorial!
# view the result in ./logs/


# speed test code, uncomment if you want to test the speed:
# for i in range(int(input("Number to test: "))):
#     logger.append("network", "info", "A new visitor!")


# TODO:
#  format message
#  tiny function to manage settings
#  compression support
#  dump time support
#  rotation and retention
#  caught the error using decorator
#  color support of the logging message
#  Asynchronous, Thread-safe, Multiprocess-safe
#  https://github.com/Delgan/loguru#fully-descriptive-exceptions
