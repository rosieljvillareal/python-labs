import logging

# log to a file, by default 'a' append mode
logging.basicConfig(filename='example.log',
    level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
