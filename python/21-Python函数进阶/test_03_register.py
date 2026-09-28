# ============================================
# 题目2-3：学生信息注册
# ============================================
# 定义一个函数 register(name, age, gender, city='北京')
# 1. 使用默认参数 city='北京'
# 2. 返回学生信息字典
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


