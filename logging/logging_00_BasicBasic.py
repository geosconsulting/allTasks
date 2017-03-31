import logging

# A SCHERMO
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.debug('This is a log message.')

# SU FILE
# logging.basicConfig(filename='log_filename.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.debug('This is a log message.')

########################################################################################
### To log messages to a file AND printed to the screen, copy and paste the following:
########################################################################################

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

fh = logging.FileHandler('log_filename_1.txt')
fh.setLevel(logging.ERROR)
fh.setFormatter(formatter)
logger.addHandler(fh)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

logger.debug('This is a test log message.')
