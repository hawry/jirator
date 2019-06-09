import logging
from constant import LOGGER

log = None

def setup_logger(verbose):
    # formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')
    formatter = logging.Formatter(fmt='%(message)s')
    if verbose:
        formatter = logging.Formatter(fmt='%(levelname)s : %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger = logging.getLogger(LOGGER)
    logger.setLevel((logging.INFO, logging.DEBUG)[verbose])
    logger.addHandler(handler)
    log = logger
