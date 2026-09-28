# ============================================
# 综合题：成绩统计小程序（注解版）
# ============================================
# 完成以下操作：
# 1. 用带类型注解的方式定义 4 个变量：班级名（字符串）、学生名单（字符串列表）、
#    三科平均分（整数列表）、等级对照表（键和值都是字符串的字典）
# 2. 写函数 average(scores)：参数标注整数列表、返回值标注小数，返回平均分
# 3. 写函数 report(scores)：一次返回最高分、最低分、平均分，返回值标注"三个元素的元组"
# 4. 打印班级、人数、平均分（保留 2 位小数）、最高分/最低分和等级对照表
# 5. 故意把字符串列表传给第 2 步的函数，看报错信息来自哪里，
#    再用一句注释写下"注解只是提示，不是强制约束"的意思
# ============================================

# 在下面写你的代码：
class Summary:
    def __init__(self, class_name: str, students: list[str], scores: list[int], grade_dict: dict[str, str]):
        self.class_name = class_name
        self.students = students
        self.scores = scores
        self.grade_dict = grade_dict
    def average(self, scores: list[int]) -> float:
        return round(sum(scores) / len(scores), 2)
    def report(self, scores: list[int]) -> tuple[int, int, float]:
        return max(scores), min(scores), self.average(scores)
    def print_summary(self):
        print(f"班级：{self.class_name}")
        print(f"人数：{len(self.students)}")
        print(f"平均分：{self.average(self.scores):.2f}")
        print(f"最高分/最低分：{self.report(self.scores)}")
        print(f"等级对照表：{self.grade_dict}")
        # 注解只是提示，不是强制约束
summary = Summary("高一(1)班", ["张三", "李四", "王五"], [85, 90, 78], {"优秀": "A", "良好": "B", "中等": "C", "及格": "D", "不及格": "E"})
summary.print_summary()




