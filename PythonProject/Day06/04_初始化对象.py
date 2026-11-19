class Person:
    # 定义初始化方法
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def Personal_Introduction(self):
        print(f"我是{self.name},我今年{self.age}岁")


# 创建对象
p1=Person("张三",44)
p2=Person("李四",33)

# 访问属性
print(p1.__dict__)
print(p2.__dict__)

p1.Personal_Introduction()
p2.Personal_Introduction()
