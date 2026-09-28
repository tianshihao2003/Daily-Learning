# ============================================
# 题目2-3：给多返回值函数加类型注解
# ============================================
# 完成以下操作：
# 1. 写函数 min_max_avg(scores)：一次返回最大值、最小值、平均值
# 2. 返回值类型注解写成"三个元素依次为整数、整数、小数的元组"
# 3. 用 [85, 90, 95, 100] 调用，把三个结果分别打印（应该是 100 85 92.5）
# ============================================

# 在下面写你的代码：

def min_max_avg(scores: list[int]) -> tuple[int, int, float | int]:
    max_score = max(scores)
    min_score = min(scores)
    avg_score = sum(scores) / len(scores)
    return (max_score, min_score, avg_score)
scores = [85, 90, 95, 100]
print(min_max_avg(scores))


