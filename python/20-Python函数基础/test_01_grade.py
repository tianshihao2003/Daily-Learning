# ============================================
# 题目1：分数等级判断
# ============================================
# 定义一个函数 get_grade(score)，根据传入的分数返回对应的等级：
# 1. 分数 >= 90：返回 "A" |---知识点：return "A"---|
# 2. 分数 >= 75：返回 "B" |---知识点：elif score >= 75:---|
# 3. 分数 >= 60：返回 "C" |---知识点：elif score >= 60:---|
# 4. 分数 < 60：返回 "D" |---知识点：else:---|
# ============================================
# 在下面写你的代码：


def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "D"


score = int(input("请输入："))

print(get_grade(score))


# ============================================
# 参考答案（写完后取消注释对比）
# ============================================
# def get_grade(score):
#     if score >= 90:
#         return "A"
#     elif score >= 75:
#         return "B"
#     elif score >= 60:
#         return "C"
#     else:
#         return "D"
#
# print(get_grade(93))   # A
# print(get_grade(80))   # B
# print(get_grade(65))   # C
# print(get_grade(40))   # D
