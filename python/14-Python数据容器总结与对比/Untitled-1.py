def calc_data(scores: list[int]) -> tuple[int, int, float]:
    max_v = max(scores)
    min_v = min(scores)
    avg_v = sum(scores) / len(scores)
    return max_v, min_v, avg_v

# 调用
max_score, min_score, avg_score = calc_data([85, 90, 95, 100])
print(max_score, min_score, avg_score)  # 100 85 92.5