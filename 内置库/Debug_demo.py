# name = "Wang"
# age = 18
#
# print("name is " + name + " ,age is " + str(age))

# 调试方法
# 使用 print or logging 打印日志信息
import logging

logging.basicConfig(level=logging.INFO)
a = 1
b = 2
if a == 1:
    flag = False
    # print(f"a == 1 : flag = {flag}")
    logging.info(f"a == 1 : flag = {flag}")
else:
    flag = True
    # print(f"a == 1 : flag = {flag}")

print(flag)
