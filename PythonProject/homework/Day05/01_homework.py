def score_organize(score):
    if score > 90:
        return "A"
    elif score > 75:
        return "B"
    elif 0 < score < 60:
        return "C"
    else:
        print("输入错误")
        return None


print(score_organize(100))