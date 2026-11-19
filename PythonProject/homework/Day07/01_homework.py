class Phone:
    def __init__(self,brand,price):
        self.brand=brand
        self.__price=price

    def show_info(self):
        print(f"{self.brand}的价格为:{self.__price}")

    def set_price(self,price):
        if price>0 and price<=10000:
            self.__price=price
        else:
            print("输出不合法")

xiaomi = Phone("xiaomi",2999)
xiaomi.show_info()

xiaomi.set_price(12000)
xiaomi.set_price(3999)

xiaomi.show_info()

