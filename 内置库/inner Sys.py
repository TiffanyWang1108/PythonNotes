import os.path
import sys

# help(sys)
# print(dir(sys))

# 返回python解释器版本
# print(sys.version)

# 返回操作系统平台名称
# print(sys.platform)

# 返回外部向程序传递的参数 : 动态收集3传递给命令行的参数列表
# print(sys.argv)

# 返回已导入的模块的信息--以字典格式
# print(sys.modules)
# print(sys.modules.keys())

# 返回导包的搜索路径列表
# print(sys.path)
# 添加自定义导包路径
# my_dir = os.path.dirname(os.path.abspath(__file__)) + "/hello"
# sys.path.append(my_dir)


# 常用方法

# 获取编码方式、
# print(sys.getdefaultencoding())

# 运行时退出-0:正常终止，任何非零值--被认为是异常终止
import time

for i in range(10):
    if i == 6:
        print("exit...")
        sys.exit("正常退出...")
    print(f"running{i}...")
    time.sleep(i)
