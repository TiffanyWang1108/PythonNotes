import os
# Operating System
# os 模块的常用功能
# 跨平台的差异

# help(os)

# print(dir(os))
# 系统相关
# print(os.name)
#  获取系统环境变量信息
# print(os.environ)
# 执行系统指令
# os.system("pwd")
# 操作目录

# 获取当前目录
# print(os.getcwd())

# # 切换目录
# os.chdir("..")
# print(os.getcwd())

# # 列出当前目录内容
# print(os.listdir())

# # 创建空目录
# os.mkdir("mkdemo.py")

# # 递归创建多级目录
# os.makedirs("a/b/c")

# # 删除空目录
# os.rmdir("a")

# # 重命名目录
# os.renames("mkdemo.py", "mkdemo")

# # 删除文件
# os.removedirs("mkdemo")
# os.remove("hello.txt")


# # 操作路径


# 返回绝对路径
# print(os.path.abspath("./inner OS.py"))
#

# 返回文件名
# print(os.path.basename("E:/Users/Administrator/PycharmProjects/pythonModuleProject/inner OS.py"))

# 返回文件路径
# print(os.path.dirname("E:/Users/Administrator/PycharmProjects/pythonModuleProject/inner OS.py"))

# 分割路径
# print(os.path.split("E:/Users/Administrator/PycharmProjects/pythonModuleProject/inner OS.py"))

# 拼接路径
# print(os.path.join("E:/Users/Administrator/PycharmProjects/pythonModuleProject", "inner OS.py"))

# 判断路径是否存在
# print(os.path.exists("E:/Users/Administrator/PycharmProjects/pythonModuleProject/inner OS.py"))
# print(os.path.exists("./inner OS2.py"))

# 判断是否是目录
# print(os.path.isdir("E:/Users/Administrator/PycharmProjects/pythonModuleProject"))
# print(os.path.isdir("E:/Users/Administrator/PycharmProjects/pythonModuleProject2"))

# 判断是否是文件
# print(os.path.isfile("./inner OS.py"))
# print(os.path.isfile("E:/Users/Administrator/PycharmProjects/pythonModuleProject"))

# 获取文件大小
# print(os.path.getsize("./inner OS.py"))
