import logging.config

logging.config.fileConfig("logging.conf")
logger = logging.getLogger("main")
logger.debug("This is debug 日志")
