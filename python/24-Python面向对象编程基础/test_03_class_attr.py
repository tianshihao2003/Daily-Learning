# ============================================
# 题目2-2：大家共享的类属性
# ============================================
# 完成以下操作：
# 1. 定义"学生"类：创建对象时传入姓名和成绩
# 2. 加一个所有学生共享的学校名（改一次，所有学生看到的一样）
# 3. 加一个共享计数器：每创建一个学生对象就加 1
# 4. 创建 3 个学生对象，分别打印姓名；最后用类名读出计数器，看看一共创建了几个学生
# ============================================

# 在下面写你的代码：
class Student:
    school_name = "清华大学"
    count = 0
    def __init__(self, name, score):
        self.name = name
        self.score = score
        Student.count += 1

student1 = Student("张三", 95)
student2 = Student("李四", 55)
student3 = Student("王五", 80)
print(student1.name)
print(student2.name)
print(student3.name)
print(Student.count)
