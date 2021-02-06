# Part 1:
# Learn the Configuration

# there is an example of settings in settings.json
# you can try to customize it
# then start the tutorial


# Part 2:
# Tutorial Content

# import the LogManager
from logpack import LogManager

# create the log manager
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


# Part 3:
# Speed Test Code
# test data:
#   1. 2.06934*10^-5 s/line  2021/2/5
# uncomment if you want to test the speed
# from logpack import LogManager
# log_manager = LogManager()
# log_manager.register("network")
# for i in range(int(input("Number to test: "))):
#     log_manager.append("network", "info", "A new visitor!")
# log_manager.delete("network")


# TODO:
#  format message
#  tiny function to manage settings
#  compression support
#  dump time support
#  rotation and retention
#  caught the error using decorator
#  color support of the logging message
#  asynchronous, thread-safe, multiprocess-safe
#  fully descriptive exceptions
