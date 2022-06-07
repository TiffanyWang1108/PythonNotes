import logging

logging.basicConfig(
    filename="../内置库/example.log",
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s (%(filename)s:%(lineno)s)",
    datefmt="%m/%d/%Y %I:%M:%S %p"
)
logging.debug("This is a debug log message and should go to the logfile")
logging.info("This is a info log message")
logging.warning("This is a warning log message")
logging.error("This is a error log message and non-ASCII stuff")
