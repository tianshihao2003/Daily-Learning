class Person:
    # 定义初始化方法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Personal_Introduction(self):
        print(f"我是{self.name},我今年{self.age}岁")

    # __repr__
    def __repr__(self):
        return f"我是{self.name},我今年{self.age}岁"

    # __eq__ 比较
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    # __lt__ 小于
    def __lt__(self, other):
        return self.age < other.age




# 创建对象
p1 = Person("张三", 44)
p2 = Person("李四", 33)

print(p1)
print(p1==p2)
print(p1>p2)

