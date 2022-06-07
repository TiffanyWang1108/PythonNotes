# 作为日志信息的内容输出
# 计算某个功能的执行时间
# 用日期命名一个日志文件
# 生成随机数（时间不会重复）
# time--基于C语言# calendar
# datetime--基于time包进行封装的高级包
# 时间的表现形式：时间戳、格式化的时间字符串
# 常用类
# datetime（from datetime import datetime) 时间日期相关
# timedelta (from datetime import timedelta) 计算两个时间的时间差
# timezone (from datetime import timezone) 时区相关

import datetime

# nowtime = datetime.datetime.now()
# print(datetime.datetime.now())
# print(nowtime.year)
# print(nowtime.fold)
# print(nowtime.timestamp()) #转时间戳


# 字符串转datetime
# ss = "2022-05-20 13:14:52"
# s1 = datetime.datetime.strptime(ss, "%Y-%m-%d %H:%M:%S")
# print(s1.timestamp())
#
# # 时间转字符串
# now = datetime.datetime.now()
# print(now.strftime("%a, %b, %d, %H:%M"))

mtimestamp = 1653023692.0
# 时间戳->时间
s = datetime.datetime.fromtimestamp(mtimestamp)
print(s)
# 时间->时间戳
print(s.timestamp())

# 时间->时间戳
