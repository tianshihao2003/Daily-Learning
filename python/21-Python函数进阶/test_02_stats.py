# ============================================
# 题目2-2：成绩统计函数
# ============================================
# 定义一个函数 calc_stats(*scores)，接收任意数量的成绩
# 1. 用不定长参数接收多个成绩
# 2. 返回最高分、最低分、平均分
# ============================================

# 在下面写你的代码：


def calc_stats(*scores):
    return max(scores), min(scores), round(sum(scores) / len(scores), 1)


highest, lowest, avg = calc_stats(85, 92, 78, 96, 88)
print(f"最高分: {highest}, 最低分: {lowest}, 平均分: {avg}")


