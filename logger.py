import logging

# to log even debug messages since by default debug & info messages not logged
# Note: can only be called once
# logging.basicConfig(level=logging.DEBUG) 

# __name__ -> points to name of script
logger = logging.getLogger('my_log')

logging.warning('This is the root logger')
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')

# logging.error('This is an error message')
# logging.critical('This is a critical message')
