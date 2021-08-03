import logging
import sys
logger = logging.getLogger("VKAA")
logger.setLevel(logging.INFO)
fh = logging.FileHandler("vkaa.log")
formatter = logging.Formatter('[%(asctime)s] [%(name)s/%(levelname)s]: %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


def log_info(message):
    logger.info(message.encode("utf-8"))
    print("[INFO] " + str(message))


def log_warn(message):
    logger.warning(message)
    print("[WARN] " + str(message))


def log_error(message):
    logger.error(message)
    print("[ERROR] " + str(message))