# c = 1  # 全局变量
#
#
# def fn():
#     # 局部变量
#     global c
#     c = c + 2
#     print(c)
#
#
# fn()
# def fn(a: int):
#     a + 1
#
#
# li = list(filter(lambda x: (x % 2 == 0 and x != 0), range(20)))
# print(li)
import calendar


def solution(year):
    # 定义一个星期
    weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    # 求出一年多少天
    # if calendar.isleap(year):
    #     days = 366
    # else:
    #     days = 365
    days = 366 if calendar.isleap(year) else 365
    # 第一天是周几
    begin_index = calendar.weekday(year, 1, 1)

    # 求出余下几天，返回结果--days/7
    rest = days % 7

    # 判断返回结果
    if rest == 1:
        return [weekday[begin_index]]
    elif rest == 2:
        if begin_index == 6:
            return [weekday[0], weekday[begin_index]]
        else:
            return [weekday[begin_index], weekday[begin_index + 1]]


if __name__ == '__main__':
    assert solution(2022) == ["Saturday"]
    assert solution(2860) == ["Thursday", "Friday"]
    assert solution(1984) == ["Monday", "Sunday"]
