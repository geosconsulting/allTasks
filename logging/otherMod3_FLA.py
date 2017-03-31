# otherMod3_FLA.py
import logging

module_logger = logging.getLogger("main.otherMod3_FLA")


# ----------------------------------------------------------------------
def add(x, y):
    """"""
    logger = logging.getLogger("main.otherMod3_FLA.add")
    logger.info("added %s and %s to get %s" % (x, y, x + y))
    return x + y