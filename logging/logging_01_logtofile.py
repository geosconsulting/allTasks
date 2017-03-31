import logging

logging.basicConfig(filename="sample.log", level=logging.INFO)

logging.debug("This is a debug message")
logging.info("Informational message")
logging.error("An error has happened!")
log = logging.getLogger("ex")

try:
    raise RuntimeError
except Exception, err:
    log.exception("Error!")