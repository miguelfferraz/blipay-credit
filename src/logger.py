import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(levelname)s (%(asctime)s): %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
)

stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)