# ============================================
# 综合题：班级成绩管理器
# ============================================
# 完成以下操作：
# 1. 定义学生类：创建对象时传入姓名和语文、数学、英语三科成绩，保存为对象自己的属性；
#    再用类属性记录学校名
# 2. 给这个类加方法：算总分、算平均分；直接打印对象时显示"姓名 总分 平均分"
# 3. 创建 4 个学生对象，放进一个列表
# 4. 遍历列表打印全部学生，并找出总分最高的学生
# 5. （可选）加一个菜单循环：1 查看全部学生 / 2 查看总分最高 / 3 退出
# ============================================

# 在下面写你的代码：

class Student:
    school = "清华大学"
    def __init__(self, name, math, english, chinese):
        self.name = name
        self.math = math
        self.english = english
        self.chinese = chinese
    def sum(self):
        return self.math + self.english + self.chinese
    def avg(self):
        return round((self.math + self.english + self.chinese) / 3, 2)
    def __str__(self):
        return f"{self.name} {self.sum()} {self.avg()}"
    def __lt__(self, other):
        return self.sum() < other.sum()

student1 = Student("张三", 90, 80, 70)
student2 = Student("李四", 80, 90, 80)
student3 = Student("王五", 95, 85, 95)
student4 = Student("赵六", 85, 95, 85)

student_list = [student1, student2, student3, student4]
print(student_list)
for student in student_list:
    print(student)

# 找出总分最高的学生
max_student = max(student_list)
print(f"总分最高的学生是 {max_student}")

