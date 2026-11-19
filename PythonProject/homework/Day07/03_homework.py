class Car:
    def __init__(self,brand,color,price):
        self.brand=brand
        self.color=color
        self.__price=price

    def start(self):
        print(f"{self.brand}开始启动")

    def run(self):
        print(f"{self.brand}运行中")

    def stop(self):
        print(f"{self.brand}正在停车")

class FuelCar(Car):
    def add_oil(self):
        print(f"{self.brand}正在加油")

class EletricCar(Car):
    def charge(self):
        print(f"{self.brand}正在充电")

dz=FuelCar("奥迪A6","红色",22)
tsl=EletricCar("未来","灰色",22)

dz.start()
dz.run()
dz.stop()
dz.add_oil()

tsl.start()
tsl.run()
tsl.stop()
tsl.charge()

print(dz.__dict__)

# AttributeError: 'FuelCar' object has no attribute '__price'
# print(dz.__price)


