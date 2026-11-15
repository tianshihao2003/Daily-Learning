import math

students = (
("S001", "王林", 85, 92, 78),
("S002", "李慕婉", 92, 88, 95),
("S003", "十三", 78, 85, 82),
("S004", "曾牛", 88, 79, 91),
("S005", "周轶", 95, 96, 89),
("S006", "王卓", 76, 82, 77),
("S007", "红蝶", 89, 91, 94),
("S008", "徐立国", 75, 69, 82),
("S009", "许木", 86, 89, 98),
("S010", "遁天", 66, 59, 72)
)

for id,name,*scores in students:
    print(f"{name}的总分为：{sum(scores)},平均分为{sum(scores) / len(scores):.2f}")

# Chinese, Mathematics, English

chinese_scores=[i[2] for i in students]
math_scores=[i[3] for i in students]
english_scores=[i[4] for i in students]

print(chinese_scores, math_scores, english_scores)

print(f"语文成绩的最高分为：{max(chinese_scores)}")
print(f"数学成绩的最高分为：{max(math_scores)}")
print(f"英语成绩的最高分为：{max(english_scores)}")

print(f"语文成绩的最低分为：{min(chinese_scores)}")
print(f"数学成绩的最低分为：{min(math_scores)}")
print(f"英语成绩的最低分为：{min(english_scores)}")

print(f"语文成绩的平均分为：{sum(chinese_scores)/len(chinese_scores)}")
print(f"数学成绩的平均分为：{sum(math_scores)/len(math_scores)}")
print(f"语文成绩的平均分为：{sum(english_scores)/len(english_scores)}")

for id,name,*scores in students:
    if sum(scores)/len(scores)>90:
        print(f"{name}的成绩为优秀！！")


