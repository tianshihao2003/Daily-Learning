class Car:
    def __init__(self,color,brand):
        self.color = color
        self.brand = brand

    def start(self):
        print("汽车启动了")
    def __show_info(self):
        print(f"颜色：{self.color}，品牌：{self.brand}")


class Car1(Car):
    def __init__(self,color,brand):
        super().__init__(color,brand)
        self.age = 0
    def start(self):
        super().start()
        print("奔驰车启动了")


class Car2(Car):
    pass

de1=Car1("红色","奔驰")
de1.start()
print(de1.color)
print(de1.brand)

de2=Car2("蓝色","奔驰")
de2.start()
print(de2.color)
print(de2.brand)

# de1.__show_info()

# print(de1.__age)
print(de1.__dict__)
print(de2.__dict__)