import re

# complie() - -将字符串转换为正则表达式对象

# pattern = r"hogwarts"  # 正则表达式--匹配包含hogwarts的字符串

# 转换为正则对象

# prog = re.compile(pattern)
# 匹配以hog开头的字符串
# pattern = r"hog\w+"
# s1 = "Hogwarts is a magic school"
# match1 = re.match(pattern, s1, re.I) --匹配以hog开头
# search1 = re.search(pattern, s1, re.I) --匹配第一个hog开头的字符串
# find_list1 = re.findall(pattern, s1, re.I)  # 匹配所有hog开头的字符串 返回一个列表
# print(find_list1)
# print(f"匹配时的起始位置为：{find_list1.start()}")
# print(f"匹配时的结束位置为：{find_list1.end()}")
# print(f"匹配位置的元组为：{find_list1.span()}")
# print(f"要匹配的字符串为：{find_list1.string}")
# print(f"匹配到的数据为：{find_list1.group()}")

# s2 = "I like hogwarts hogwww"
# find_list2 = re.findall(pattern, s2, re.I)
# # print(find_list2)
# 匹配手机号码--sub() 替换方法
pattern = r"1[3458]\d{9}"

s1 = "中奖号码 123456,联系电话 15611111111"
result = re.sub(pattern, "1xxxxxxxxxx", s1)
print(result)

# 切分--split()
