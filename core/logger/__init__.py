import logging

from config import config

formatter = logging.Formatter(
    "%(asctime)s,%(msecs)d %(levelname)-8s [{}: %(pathname)s:%(filename)s:%(lineno)d] %(message)s".format(
        config.SERVICE_NAME
    )
)


def setup_logger(name, log_file=None, level=logging.DEBUG):
    """To setup as many loggers as you want"""
    if log_file:
        handler = logging.FileHandler(log_file)
        handler.setFormatter(formatter)
    else:
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


console_logger = setup_logger("{}_console_logger".format(config.SERVICE_NAME))
