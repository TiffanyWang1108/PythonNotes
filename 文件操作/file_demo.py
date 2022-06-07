# open (file,mode,encode)
# mode
# r:以只读模式打开文件，并将文件指针指向文件头；如果文件不存在会报错
# r+:在r的基础上增加可写功能
# w:以只写模式打开文件，并将文件指向文件夹；如果文件存在则将其内容清空，如果文件不存在则创建
# w+:在w的基础上增加可读功能
# a:以只追加可写模式打开文件，并将文件指针指向文件尾部，如果文件不存在则创建
# a+:在a的基础上增加了可读功能
# b:在读写二进制文件(默认是1，表示文本)，需要与上面几中模式搭配使用，如ab,wb,ab+


# 第一步：（以只读模式）打开文件
# f = open("data.txt", "r", encoding="utf-8")


# 第二步：读取文件内容
# print(f.readlines())
# f.read() # 一次读取文件所有内容，返回一个字符串
# f.read("size") # 每次最多读取指定长度的内容，返回一个str，size--字符长度
# f.readline() # 每次只读取一行内容
# # f.readlines() 一次读取文件所有内容，返回一个列表list
# print(type(f.read()))
# print(type(f.readlines()))
# f.seek(0) 读完一次之后，再次读取文件，内容将不是完整的，需要重新设置游标
# 设置光标读取之后的位置
# f.read()

# 第三步：关闭文件
# f.close()
# 忘记关闭文件：
# 打开文件达到一定数量，将会导致打开失败
# 占用内存空间，非常浪费资源
# 会导致系统自动回收资源，而丢失数据


# with open:自动关闭
# with open("data.txt", "r", encoding="utf-8") as f2:
#     print(f2.read())
#
# print(f2.closed)  # 判断是否关闭文件

# mode = "w+" : 读写权限，会新建文件，清空内容再写入
# mode = "r+" : 读写权限，替换原来的内容
# mode = "a+" : 读写权限，追加内容
with open("data1.txt", "a+", encoding="utf-8", ) as f2:
    print(f2.write("\nharry potter"))

print(f2.closed)
