import logging

# config
logging.basicConfig(level=logging.DEBUG,
        format='[%(asctime)s] %(levelname)s %(module)s %(lineno)d - %(message)s')

# add name
logger = logging.getLogger(__name__)

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
