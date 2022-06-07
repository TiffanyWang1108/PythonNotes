# # for
# for i in range(1, 101):
#     if i % 3 == 2 and i % 5 == 3 and i % 7 == 2:
#         print(f"符合条件的整数：{i}")

# while
# num = 1
# while num <= 100:
#     if num % 3 == 2 and num % 5 == 3 and num % 7 == 2:
#         print(f"符合条件的整数：{num}")
#     num += 1

# 题目二：鸡兔同笼
# 双循环
# for x in range(36):
#     for y in range(36):
#         if (x + y == 35) and (2 * x + 4*y == 94):
#             print(f"鸡{x}只, 兔{y}只")
# 单循环
# for x in range(36):
#     if 2 * x + 4 * (35 - x) == 94:
#         print(f"鸡{x}只, 兔{35 - x}只")

# s = "hogwarts"
# print(s)
#
# s1 = s.replace(s[0], "x")
# print(s1)
