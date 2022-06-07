# 异常捕获和处理
# def div(a, b):
#     return a / b
#
#
# list1 = [1, 2, 3]
# try:
#     # print(div(1, 0))
#     print(list1[3])
#     print("try:需要执行的代码块")
# except Exception as e:
#     print(e)
#     print("except:有异常发生时执行的代码块")
# else:
#     print("else:没有异常时执行的代码块")
# finally:  # finally 无论有无异常都会被执行
#     print("finally:无论有无异常都会被执行")

# 使用 raise 触发异常
# def set_age(age):
#     if age < 0 or age > 200:
#         raise ValueError("值错误")
#     else:
#         print(f"The age is：{age}")
#
#
# set_age(-1)


# 自定义异常
class MyException(Exception):
    def __init__(self, msg):
        print(f"This is My Exception:{msg}")


def set_age(age):
    if age < 0 or age > 200:
        raise MyException("值错误")
    else:
        print(f"The age is：{age}")


set_age(-1)
