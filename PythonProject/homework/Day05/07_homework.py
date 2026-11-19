# ============================================================================
# 练习2：成绩统计分析器
# ============================================================================
#
# 题目描述：
#   设计一个函数 analyze_scores，要求功能如下：
#   1. 通过 *args 接收任意数量的分数（0~100之间的数值）
#   2. 通过 **kwargs 接收配置项：
#      - round_ndigits：结果保留的小数位数（默认 1）
#      - show_detail：是否打印详细信息（默认 False）
#      - pass_line：及格线分数（默认 60）
#   3. 返回值是一个字典，包含：
#      - count：人数
#      - max_score：最高分
#      - min_score：最低分
#      - avg_score：平均分
#      - pass_rate：及格率（以百分比字符串表示，如 "75.0%"）
#   4. 如果 show_detail=True，在函数内部打印详细统计信息
#   5. 如果未传入任何分数，返回字典中各项均为 0 或 "0%"
#   6. 添加完整的类型注解
#
#   测试：
#     analyze_scores(85,92,78,89,95,88,76,90, round_ndigits=2, show_detail=True)
#       → {'count': 8, 'max_score': 95, 'min_score': 76, 'avg_score': 86.62, 'pass_rate': '100.0%'}
#     analyze_scores(45,55,38,62,70,59, pass_line=60, round_ndigits=1)
#       → {'count': 6, 'max_score': 70, 'min_score': 38, 'avg_score': 54.8, 'pass_rate': '33.3%'}
# ============================================================================



def analyze_scores(*args: int, **kwargs: int | bool | int) -> dict:
    round_ndigits = kwargs.get("round_ndigits", 1)
    show_detail = kwargs.get("show_detail", False)
    pass_line = kwargs.get("pass_line", 60)

    count_line = len(args)
    if count_line == 0:
        return {"count": 0, "max_score": 0, "min_score": 0, "avg_score": 0, "pass_rate": "0%"}

    max_score = max(args)
    min_score = min(args)
    avg_score = round(sum(args) / count_line, round_ndigits)

    sum_c = sum([1 for score in args if score >= pass_line]) / count_line * 100
    pass_rate= f"{sum_c:.{round_ndigits}f}%"

    if show_detail:
        print(f"人数：{count_line}，最高分：{max_score}，最低分：{min_score}，平均分：{avg_score}，及格率：{pass_rate}")

    return {"count": count_line, "max_score": max_score,"min_score": min_score,"avg_score": avg_score,"pass_rate": pass_rate}


analyze_scores(45,55,38,62,70,59, pass_line=70, round_ndigits=1, show_detail=True)

analyze_scores(85,22,78,89,95,22,22,33, pass_line=70, round_ndigits=1, show_detail=True)

