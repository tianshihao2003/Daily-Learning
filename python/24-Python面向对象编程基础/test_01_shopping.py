# ============================================
# 综合练习：购物车管理系统
# ============================================

# ============================================
# 第一步：定义商品类 Goods
# ============================================
# 1. 定义 __init__ 方法，初始化 name、price、num 属性
# -> class Goods: def __init__(self, name, price, num):
# 2. 定义 __str__ 方法，返回商品信息字符串
# -> def __str__(self): return f"商品名称: {self.name}..."
# ============================================

# 在下面写你的代码：

class Goods:
    def __init__(self,name,price,num):
        self.name = name
        self.price = price
        self.num = num

    def __str__(self):
        return f"商品名称: {self.name}, 商品价格: {self.price}, 商品数量: {self.num}"


# ============================================
# 第二步：为商品类添加修改方法
# ============================================
# 定义 update_info 方法，可以修改价格和数量
# 使用默认参数 price=None, num=None
# -> def update_info(self, price=None, num=None):
# ============================================

# 在下面写你的代码：

    def update_info(self, price=None, num=None):
        if price != None:
            self.price = price
        if num != None:
            self.num = num

# ============================================
# 第三步：定义购物车类 ShoppingCart
# ============================================
# 1. 定义类属性 system_version 和 system_name
# -> system_version = "1.0"
# 2. 定义 __init__ 方法，初始化空列表 goods_list
# -> self.goods_list = []
# ============================================

# 在下面写你的代码：
class ShoppingCart:
    system_version = "1.0"
    system_name = "购物车管理系统"

    def __init__(self):
        self.goods_list = []


# ============================================
# 第四步：实现添加商品功能
# ============================================
# 1. 获取用户输入的商品信息
# 2. 检查商品是否已存在：for goods in self.goods_list:
# 3. 创建 Goods 对象并添加到列表：self.goods_list.append(goods)
# ============================================

# 在下面写你的代码：
    def add_goods(self):
        name = input("请输入商品名称：")
        for goods in self.goods_list:
            if goods.name == name:
                print("商品已存在")
                return
        price = float(input("请输入商品价格："))
        num = int(input("请输入商品数量："))

        if price <= 0 or num <= 0:
            print("价格或数量不能小于等于0")
            return
        goods = Goods(name, price, num)
        self.goods_list.append(goods)
        print("商品添加成功")
        return



# ============================================
# 第五步：实现修改商品功能
# ============================================
# 1. 根据名称查找商品
# 2. 调用商品的 update_info 方法
# -> goods.update_info(price, num)
# ============================================

# 在下面写你的代码：

    def update_goods(self):
        name = input("请输入商品名称：")

        for goods in self.goods_list:
            if goods.name == name:
                print(f"当前商品信息：{goods}")
                price = float(input("请输入新的商品价格："))
                num = int(input("请输入新的商品数量："))

                if price <= 0 or num <= 0:
                    print("价格或数量不能小于等于0")
                    return
                goods.update_info(price, num)
                print("商品修改成功")
                return
            print("没有找到该商品")




# ============================================
# 第六步：实现删除商品功能
# ============================================
# 1. 根据名称查找商品
# 2. 用 remove() 从列表中删除
# -> self.goods_list.remove(goods)
# ============================================

# 在下面写你的代码：
    def delete_goods(self):
        name = input("请输入商品名称：")

        for goods in self.goods_list:
            if goods.name == name:
                self.goods_list.remove(goods)
                print("商品删除成功")
                return
            print("没有找到该商品")


# ============================================
# 第七步：实现查询功能
# ============================================
# 遍历列表，打印每个商品（会自动调用 __str__ 方法）
# -> for goods in self.goods_list: print(goods)
# ============================================

# 在下面写你的代码：
    def query_goods(self):
        if not self.goods_list:
            print("商品列表为空")
            return
        for goods in self.goods_list:
            print(goods)
            return



# ============================================
# 第八步：实现主循环
# ============================================
# 1. 用 while True 显示菜单
# 2. 用 match...case 匹配用户选择
# ============================================

# 在下面写你的代码：
    def main(self):
        while True:
            print("1. 添加商品")
            print("2. 删除商品")
            print("3. 查询商品")
            print("4. 退出")
            choice = input("请输入操作：")
            match choice:
                case "1":
                    self.add_goods()
                case "2":
                    self.delete_goods()
                case "3":
                    self.query_goods()
                case "4":
                    break
                case _:
                    print("输入有误，请重新输入")

#测试运行
if __name__ == '__main__':
    shopping_cart = ShoppingCart()
    shopping_cart.main()






# ============================================
# 完整参考答案（写完后取消注释对比）
# ============================================

# # 商品类
# class Goods:
#     def __init__(self, name, price, num):
#         self.name = name
#         self.price = price
#         self.num = num
#
#     def __str__(self):
#         return f"商品名称: {self.name}, 商品价格: {self.price}, 商品数量: {self.num}"
#
#     def update_info(self, price=None, num=None):
#         if price is not None:
#             self.price = price
#         if num is not None:
#             self.num = num
#
#
# # 购物车系统类
# class ShoppingCart:
#     system_version = "1.0"
#     system_name = "购物车管理系统"
#
#     def __init__(self):
#         self.goods_list = []
#
#     def add_goods(self):
#         name = input("请输入商品名称: ")
#         for goods in self.goods_list:
#             if goods.name == name:
#                 print("该商品已在购物车中，添加失败!")
#                 return
#         price = float(input("请输入商品价格: "))
#         num = int(input("请输入商品数量: "))
#         if price >= 0 and num >= 0:
#             goods = Goods(name, price, num)
#             self.goods_list.append(goods)
#             print("商品添加成功 ~")
#         else:
#             print("价格和数量必须为非负数!")
#
#     def update_goods(self):
#         name = input("请输入要修改的商品名称: ")
#         for goods in self.goods_list:
#             if goods.name == name:
#                 print(f"当前商品信息: {goods}")
#                 price = float(input("请输入修改后的商品价格: "))
#                 num = int(input("请输入修改后的商品数量: "))
#                 if price >= 0 and num >= 0:
#                     goods.update_info(price, num)
#                     print("商品信息修改成功 ~")
#                 else:
#                     print("价格和数量必须为非负数!")
#                 return
#         print("未找到该商品，修改失败!")
#
#     def delete_goods(self):
#         name = input("请输入要删除的商品名称: ")
#         for goods in self.goods_list:
#             if goods.name == name:
#                 self.goods_list.remove(goods)
#                 print("商品删除成功 ~")
#                 return
#         print("未找到该商品，删除失败!")
#
#     def query_all_goods(self):
#         if not self.goods_list:
#             print("购物车为空!")
#             return
#         print("购物车中的商品信息:")
#         print("-" * 40)
#         for goods in self.goods_list:
#             print(goods)
#         print("-" * 40)
#         print(f"总计商品数量: {len(self.goods_list)}")
#
#     def run(self):
#         print(f"欢迎使用{ShoppingCart.system_name} V{ShoppingCart.system_version}")
#         while True:
#             print()
#             print("# " * 35)
#             print("#       1.添加商品  2.修改商品  3.删除商品  4.查询购物车  5.退出系统        #")
#             print("# " * 35)
#             choice = input("请选择要执行的操作，输入1-5: ")
#             match choice:
#                 case "1": self.add_goods()
#                 case "2": self.update_goods()
#                 case "3": self.delete_goods()
#                 case "4": self.query_all_goods()
#                 case "5":
#                     print("感谢使用购物车管理系统，再见!")
#                     break
#                 case _: print("输入错误，请选择1-5之间的菜单功能!")
#
#
# # 测试
# if __name__ == '__main__':
#     shopping_cart = ShoppingCart()
#     shopping_cart.run()
