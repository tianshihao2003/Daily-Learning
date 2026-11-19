class Person:
    pass


# 创建对象
p1 = Person()

# 给对象赋于属性
p1.name = "张三"
p1.age = 19
p1.hobby = "喝酒"

# 访问
print(p1.name, p1.age, p1.hobby)

# 创建第二个对象

p2 = Person()

p2.name = "王五"
p2.age = 33
p2.hobby = "抽烟"

print(p2.name, p2.age, p2.hobby)

# 使用字典打印
print(p1.__dict__)
