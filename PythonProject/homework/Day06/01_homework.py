import math


class Student:
    def __init__(self,name,chinese,math,english):
        self.name=name
        self.chinese=chinese
        self.math=math
        self.english=english

    # 定义 __repr__ 方法，用于打印对象信息
    def __repr__(self):
        return f"Student({self.name},{self.chinese},{self.math},{self.english})"





# 教务管理系统类
class StudentManagement:
    # 添加学生信息
    def add_student(self):

        student_name = input("请输入学生姓名：")
        chinese = int(input("请输入语文成绩："))
        math = int(input("请输入数学成绩："))
        english = int(input("请输入英语成绩："))

        # 创建学生对象
        student01=Student(student_name,chinese,math,english)
        # 存储学生对象
        print(student01)
        stu[student_name]=student01
        print("添加成功！")
        return stu

    # 修改学生信息
    def modify_student(self):

        # 从字典中获取学生对象
        student_name = input("请输入学生姓名：")
        if student_name in stu:
            # 修改学生信息
            student01=stu[student_name]
            # 修改学生信息
            chinese = int(input("请输入语文成绩："))
            math = int(input("请输入数学成绩："))
            english = int(input("请输入英语成绩："))
            # 更新学生对象
            student01.chinese=chinese
            student01.math=math
            student01.english=english
            # 打印修改后的学生信息
            print(student01)
            print("修改成功！")
            return student01
        else:
            print("学生不存在！")
            return None


    # 删除学生信息
    def del_student(self):

        student_name=input("请输入你要删除的学生姓名：")
        if student_name in stu:
            del stu[student_name]
            print(stu)
            print("删除成功！")
            return stu
        else:
            print("你要删除的学生不存在！")
            return None

    # 查询学生信息
    def query_student(self):
        student_name=input("请输入你要查询的学生姓名：")
        if student_name in stu:
            print(stu[student_name])
            print("查询成功！")
        else:
            print("你查询的学生不存在！！")

    # 显示所有学生信息
    def show_all(self):
        print(stu)
        print("显示所有学生信息成功！")

    # statistics
    def statistics(self):
        list_chinese = [object1.chinese for name, object1 in stu.items()]
        list_math = [object1.math for name, object1 in stu.items()]
        list_english = [object1.english for name, object1 in stu.items()]
        print(f"语文最高分{max(list_chinese)},数学最高分{max(list_math)},英语最高分{max(list_english)}")
        print(f"语文最低分{min(list_chinese)},数学最低分{min(list_math)},英语最低分{min(list_english)}")
        print(f"语文平均分{sum(list_chinese)/len(list_chinese)},数学平均分{sum(list_math)/len(list_math)},英语平均分{sum(list_english)/len(list_english)}")
        max_chinese_name=[name for name, object1 in stu.items() if object1.chinese==max(list_chinese)]
        max_math_name=[name for name, object1 in stu.items() if object1.math==max(list_math)]
        max_english_name=[name for name, object1 in stu.items() if object1.english==max(list_english)]

        print(f"语文最高分是{max_chinese_name},数学最高分是{max_math_name},英语最高分是{max_english_name}")

stu = {
    "张三": Student("张三", 88, 76, 90),
    "李四": Student("李四", 72, 85, 69),
    "王五": Student("王五", 95, 91, 87),
    "赵六": Student("赵六", 66, 70, 78),
    "田七": Student("田七", 82, 79, 93)
}
while True:
    print("欢迎来到教务管理系统！")

    # 创建教务管理系统对象
    StudentManagement01=StudentManagement()
    # 选择操作
    choice = int(input("请输入您的选择："))
    match choice:
        case 1:
            print("正在添加学生信息")
            print(StudentManagement01.add_student())
        case 2:
            print("正在修改学生信息")
            StudentManagement01.modify_student()
        case 3:
            print("正在删除学生信息")
            StudentManagement01.del_student()
        case 4:
            print("正在查询学生信息")
            StudentManagement01.query_student()
        case 5:
            print("正在显示所有学生信息")
            StudentManagement01.show_all()
        case 6:
            print("欢迎下次使用！")
            break
        case 7:
            print("正在统计班级成绩！！")
            StudentManagement01.statistics()



# 功能7：
#     统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，
#     以及语文、数学、英语最高分和     最低分的学员姓名。 打印结果
        case _:
            print("输入错误！")


