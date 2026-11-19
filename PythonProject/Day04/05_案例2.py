import math

print("==========欢迎使用教务管理系统==========")

menu="""
# # # # # # # # # # # # # # # # # # # # # # # # # # 【菜单】 # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  1. 添加学生信息   2. 修改学生信息   3. 删除学生信息   4. 查询学生信息   5. 列出所有学生   6. 统计班级成绩   7. 退出系统       #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""
print(menu)

student_scores={
    "张三":{"chinese":80, "math":90, "english":55},
    "李四":{"chinese":100, "math":50, "english":44},
    "王五":{"chinese":40, "math":99, "english":66}
}




while True:
    operation=int(input("请输入你要进行的操作："))

    match operation:
        case 1:
            name=input("请输入学生的姓名：")
            if name in student_scores:
                print("该学生已存在，请选择修改功能！！")
                continue
            else:
                chinese=float(input(f"请输入{name}的语文成绩："))
                math=float(input(f"请输入{name}的数学成绩："))
                english=float(input(f"请输入{name}的英语成绩："))

                student_scores[name]={"chinese":chinese,"math":math,"english":english}

                print("添加学生信息成功！！！")
                continue
        case 2:
            name=input("请输入你要修改学生的姓名：")
            if name not in student_scores:
                print("该学生不在系统中，请先去添加学生信息！！")

            else:
                chinese=float(input(f"请输入{name}的语文成绩："))
                math=float(input(f"请输入{name}的数学成绩："))
                english=float(input(f"请输入{name}的英语成绩："))
                student_scores[name]={"chinese":chinese,"math":math,"english":english}

                print("修改学生信息成功！！！")
                continue


        case 3:
            name = input("请输入你要删除的学生姓名：")
            if name not in student_scores:
                print("你要删除的学生不存在！！！")
            else:
                student_scores.pop(name)
                print("删除成功！！！！")

        case 4:
            name=input("请输入你要查询的学生姓名：")
            if name not in student_scores:
                print("你要查询的学生信息不存在！！")
            else:
                print(f"{name}的成绩为：{student_scores[name]}")

        case 5:
            for i in student_scores.items():
                print(f"{i[0]}的语文成绩为：{i[1]['chinese']},数学成绩为：{i[1]['math']},英语成绩为：{i[1]['english']}")

        case 6:
            new_chinese=[]
            new_math=[]
            new_english=[]
            for i in student_scores.items():
                new_chinese.append(i[1]["chinese"])
                new_math.append(i[1]["math"])
                new_english.append(i[1]["english"])

            print(f"班级语文成绩最高分为：{max(new_chinese)}")
            print(f"班级英语成绩最高分为：{max(new_english)}")
            print(f"班级数学成绩最高分为：{max(new_math)}")
            # 最低分
            print(f"班级语文成绩最低分为：{min(new_chinese)}")
            print(f"班级英语成绩最低分为：{min(new_english)}")
            print(f"班级数学成绩最低分为：{min(new_math)}")

            # 平均分·
            # 保留两位小数
            print(f"班级语文成绩平均分为：{sum(new_chinese)/len(new_chinese):.2f}")
            print(f"班级英语成绩平均分为：{sum(new_english)/len(new_english):.2f}")
            print(f"班级数学成绩平均分为：{sum(new_math)/len(new_math):.2f}")

            max_chinese_name=[name for name,score in student_scores.items() if score['chinese'] == max(new_chinese)]
            print(f"班级语文成绩最高的学生为：{max_chinese_name}")
            max_math_name=[name for name,score in student_scores.items() if score['math'] == max(new_math)]
            print(f"班级数学成绩最高的学生为：{max_math_name}")
            max_english_name=[name for name,score in student_scores.items() if score['english'] == max(new_english)]
            print(f"班级英语成绩最高的学生为：{max_english_name}")

        case 7:
            print("谢谢使用！！！")
            break

        case _:
            print("你输入的操作有误，请重新输入！！")
