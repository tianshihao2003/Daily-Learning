# ----------------------------------------------------------
# 需求1：定义一个函数 is_leap_year，接收一个年份 year（整数），
#       判断该年份是否为闰年，返回 True 或 False。
#
#       闰年规则：
#         - 能被 400 整除的是闰年
#         - 能被 4 整除但不能被 100 整除的也是闰年
#         - 其余不是闰年
#
#       调用该函数，分别判断 2000年、2024年、1900年、2025年 是否为闰年。
# ----------------------------------------------------------
def is_leap_year(year):
    if year%4==0 and year%100!=0 or year%400==0:
        return True
    else:
        return False

print()
print(is_leap_year(2024))
print(is_leap_year(1900))
print(is_leap_year(2025))
# ----------------------------------------------------------`
# 需求2：定义一个函数 count_case，接收一个字符串参数，
#       统计其中大写字母和小写字母的个数，返回两个结果。
#       （提示：可用字符串的 .isupper()判断是否为大写字母 和 .islower() 方法判断该字母是否为小写字母）
#
#       调用该函数，传入字符串 "Hello World! Python3 编程"，
#       用解包方式接收并打印大写字母个数和小写字母个数。
# ----------------------------------------------------------
def count_case(string):
    da_num=0
    xia_num=0
    for i in string:
        if i.isupper():
            da_num+=1
        elif i.islower():
            xia_num+=1
    return f"大写字母有{da_num}个，小写字母有{xia_num}个"
print(count_case("Hello World! Python3 编程"))
