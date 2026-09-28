# ============================================
# 综合题：教务管理系统
# ============================================

# ============================================
# 第一步：显示菜单
# ============================================
# 用 print 打印菜单，让用户知道有哪些功能
# 提示：可以用多行字符串 """ """
# ============================================

# 在下面写你的代码：
ts = """"欢迎使用教务管理系统
请选择你需要使用的功能：
1. 添加学生信息：录入学生姓名、语文、数学、英语成绩
2. 修改学生信息：根据姓名修改成绩
3. 删除学生信息：根据姓名删除学生
4. 查询学生信息：根据姓名查询成绩
5. 列出所有学生：遍历所有学生信息
6. 统计班级成绩：最高分、最低分、平均分
7. 退出系统
"""
print(ts)


# ============================================
# 第二步：用字典存储学生信息
# ============================================
# 创建一个空字典 student_scores
# 字典格式: {姓名: {"chinese": 语文, "math": 数学, "english": 英语}}
# 提示：student_scores = {}
# ============================================

# 在下面写你的代码：
student_scores = {}


# ============================================
# 第三步：用 while 循环实现主循环
# ============================================
# 用 while True 创建无限循环
# 每次循环显示菜单，获取用户输入
# 用 match...case 匹配用户选择
# ============================================

# 在下面写你的代码：

while True:
    choice = int(input("请选择要执行的操作(1-7): "))

    match choice:
        # ============================================
        # 第四步：实现添加学生功能
        # ============================================
        # 1. 获取学生姓名：input("请输入学生姓名: ")
        # 2. 检查学生是否已存在：if student_name in student_scores:
        # 3. 如果不存在，获取各科成绩
        # 4. 保存到字典：student_scores[student_name] = {...}
        # ============================================

        # 在下面写你的代码：
        case 1:
            student_name = input("请输入学生姓名: ")
            if student_name in student_scores:
                print("该学生已存在, 请重新选择 ~")
            else:
                chinese_score = float(input("请输入语文成绩: "))
                math_score = float(input("请输入数学成绩: "))
                english_score = float(input("请输入英语成绩: "))
                student_scores[student_name] = {
                    "chinese": chinese_score,
                    "math": math_score,
                    "english": english_score,
                }
                print("添加成功 ~")

        # ============================================
        # 第五步：实现修改学生功能
        # ============================================
        # 1. 获取要修改的学生姓名
        # 2. 检查学生是否存在：if student_name not in student_scores:
        # 3. 如果不存在，用 continue 跳过
        # 4. 如果存在，获取新成绩并更新
        # ============================================

        # 在下面写你的代码：
        case 2:
            student_name = input("请输入学生姓名: ")
            if student_name not in student_scores:
                print("该学生不存在, 请重新选择 ~")
            else:
                chinese_score = float(input("请输入语文成绩: "))
                math_score = float(input("请输入数学成绩: "))
                english_score = float(input("请输入英语成绩: "))
                student_scores[student_name] = {
                    "chinese": chinese_score,
                    "math": math_score,
                }
                print("修改完毕！")

        # ============================================
        # 第六步：实现删除学生功能
        # ============================================
        # 1. 获取要删除的学生姓名
        # 2. 检查学生是否存在
        # 3. 如果存在，用 del 删除：del student_scores[student_name]
        # ============================================

        # 在下面写你的代码：
        case 3:
            student_name = input("请输入学生姓名: ")
            if student_name not in student_scores:
                print("该学生不存在, 请重新选择 ~")
            else:
                del student_scores[student_name]
                print("删除成功 ~")

        # ============================================
        # 第七步：实现查询学生功能
        # ============================================
        # 1. 获取要查询的学生姓名
        # 2. 检查学生是否存在
        # 3. 如果存在，用 f-string 打印学生信息
        # ============================================

        # 在下面写你的代码：
        case 4:
            student_name = input("请输入学生姓名: ")
            if student_name not in student_scores:
                print("该学生不存在, 请重新选择 ~")
            else:
                print(f"{student_name} 的成绩为:")
                print(f"语文: {student_scores[student_name]['chinese']}")
                print(f"数学: {student_scores[student_name]['math']}")
                print(f"英语: {student_scores[student_name]['english']}")

        # ============================================
        # 第八步：实现列出所有学生功能
        # ============================================
        # 1. 用 for 循环遍历字典：for name, scores in student_scores.items():
        # 2. 打印每个学生的信息
        # ============================================

        # 在下面写你的代码：
        case 5:
            for name, scores in student_scores.items():
                print(f"{name} 的成绩为:")
                print(f"语文: {scores['chinese']}")
                print(f"数学: {scores['math']}")
                print(f"英语: {scores['english']}")

        # ============================================
        # 第九步：实现统计班级成绩功能
        # ============================================
        # 1. 创建空列表收集各科成绩
        # 2. 用 for 循环遍历字典，收集成绩
        # 3. 用 max()、min()、sum()、len() 计算统计值
        # 4. 打印统计结果
        # ============================================

        # 在下面写你的代码：
        case 6:
            chinese_scores = []
            math_scores = []
            english_scores = []
            for name, scores in student_scores.items():
                chinese_scores.append(scores["chinese"])
                math_scores.append(scores["math"])
                english_scores.append(scores["english"])
            print()
            print(f"班级语文平均分: {sum(chinese_scores) / len(chinese_scores):.2f}")
            print(f"班级数学平均分: {sum(math_scores) / len(math_scores):.2f}")
            print(f"班级英语平均分: {sum(english_scores) / len(english_scores):.2f}")
            print(
                f"班级总分平均分: {(sum(chinese_scores) + sum(math_scores) + sum(english_scores)) / len(student_scores):.2f}"
            )

        # ============================================
        # 第十步：实现退出系统功能
        # ============================================
        # 1. 打印 "Bye ~"
        # 2. 用 break 跳出循环
        # 在下面写你的代码：

        case 7:
            print("Bye ~")
            break
        case _:  # 其他情况
            print("非法操作, 不支持!!!")

