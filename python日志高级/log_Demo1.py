import logging

# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
# 流处理器--输出到终端
ch = logging.StreamHandler()
# 定义一个文件处理器，将日志输出到文件中
# ch = logging.FileHandler("mylogdemo1.log", encoding="utf-8")
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 定义一个文件处理器ch1

# 流处理器--输出到终端
# ch = logging.StreamHandler() --
# 定义一个文件处理器，将日志输出到文件中
ch_file = logging.FileHandler("mylogdemo2.log", encoding="utf-8")
ch_file.setLevel(logging.DEBUG)

# create formatter
formatter1 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch_file.setFormatter(formatter1)

# add ch to logger
logger.addHandler(ch_file)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
