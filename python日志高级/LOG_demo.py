import logging

# logging 模块默认级别是warning级别
logging.basicConfig(level=logging.INFO)  # 将默认级别设置成INFO级别
# 设置那个级别，就会打印这个级别及以上级别的日志
logging.warning("Watch out")  # print a message
logging.info("I told you so")  # print nothing
logging.error("This is an error level log")
