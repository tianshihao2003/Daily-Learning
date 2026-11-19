menu = """
########### 购物车系统 ##########
#         1. 添加购物车         #
#         2. 修改购物车         #
#         3. 删除购物车         #
#         4. 查询购物车         #
#         5. 退出购物车         #
###############################
"""

print("欢迎使用购物车系统")
print(menu)

shopping_cart = {}

while True:
    choice = int(input("请输入您的选择："))
    match choice:
        case 1:
            name = input("请输入商品名称：")
            if name in shopping_cart:
                print("商品已存在，请使用功能2")
                continue
            else:
                price = int(input("请输入商品价格："))
                num = int(input("请输入库存数量："))
                shopping_cart[name] = {"price": price, "num": num}
                print("商品添加成功！！")
        case 2:
            name = input("请输入要修改的商品名称：")
            if name not in shopping_cart:
                print("该商品还未添加，请使用功能1添加！！")
                continue
            else:
                new_price = int(input("请输入要修改的价格："))
                new_num = int(input("请输入新的库存数量："))
                shopping_cart[name] = {"price": new_price, "num": new_num}
                continue

        case 3:
            name = input("请输入你要删除的商品：")
            if name not in shopping_cart:
                print("该商品不在库存中，请先添加！！")
            else:
                shopping_cart.pop(name)
                print(f"删除{name}商品成功~")
                continue

        case 4:
            name=input("请输入你要查询商品的名字：")
            if name not in shopping_cart:
                print("该商品不在库存中，请先添加！！")
                continue
            else:
                price = shopping_cart[name]["price"]
                num = shopping_cart[name]["num"]
                print(f"你查询的商品是{name},他的价格为{price},他的库存为{num}")
                continue
        case 5:
            break
        case _:
            print("非法选择，请重新选择！！")
