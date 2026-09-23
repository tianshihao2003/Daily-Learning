# ============================================
# 题目3：学生信息注册
# ============================================
# 定义一个函数 register(name, age, gender, city='北京')
# 1. 使用默认参数 city='北京' |---知识点：参数名=默认值---|
# 2. 返回学生信息字典 |---知识点：return {"name": name, ...}---|
# ============================================
# 在下面写你的代码：
def register(name, age, gender, city='北京'):
    return {"name": name, "age": age, "gender": gender, "city": city}

# 使用默认值
stu1 = register("张三", 18, "男")
print(stu1)

 # 覆盖默认值
stu2 = register("李四", 20, "女", "上海")
print(stu2)


# ============================================
# 参考答案（写完后取消注释对比）
# ============================================
# def register(name, age, gender, city='北京'):
#     return {"name": name, "age": age, "gender": gender, "city": city}
#
# # 使用默认值
# stu1 = register("张三", 18, "男")
# print(stu1)  # {'name': '张三', 'age': 18, 'gender': '男', 'city': '北京'}
#
# # 覆盖默认值
# stu2 = register("李四", 20, "女", "上海")
# print(stu2)  # {'name': '李四', 'age': 20, 'gender': '女', 'city': '上海'}
