class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def start(self):
        print(f"{self.brand}开始启动")

    def run(self):
        print(f"{self.brand}运行中")

    def stop(self):
        print(f"{self.brand}正在停车")

class FuelCar(Car):
    pass

class EletricCar(Car):
    pass

dz=FuelCar("大众","朗逸")
tsl=EletricCar("特斯拉","Model3")

dz.start()
tsl.start()

dz.run()
tsl.run()

tsl.stop()
dz.stop()


