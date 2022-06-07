import logging

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(message)s (%(filename)s:%(lineno)s)",
    datefmt="%m/%d/%Y %I:%M:%S %p")
logging.warning("is when this event was logged.")
