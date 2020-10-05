import inspect
import logging
import pytest


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getlogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        filehandler = logging.FileHandler("logfile.txt")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)  # Filehandler object
        logger.setLevel(logging.DEBUG)
        return logger

