class Person:
    def __init__(self,nmae,age,hobby):
        self.nmae=nmae
        self.__age=age
        self.hobby=hobby

    def show_info(self):
        print(f"姓名：{self.nmae}，年龄：{self.__age}，爱好：{self.hobby}")

    def get_age(self):
        return self.__age

    # 修改年龄
    def set_age(self,age):
        if age >=0 and age <=120:
            self.__age=age
        else:
            print("年龄输入错误")


per1=Person("张三",18,"篮球")

per1.show_info()

per1.set_age(20)
per1.show_info()

per1.set_age(210)

print(per1.get_age())

