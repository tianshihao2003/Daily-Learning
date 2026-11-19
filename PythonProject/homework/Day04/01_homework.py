books_dict={
    "Python从入门到精通":{"author":"张三","price":100,"stock":100},
}

# 数据格式：{"书名":{"作者":"作者","价格":价格,"库存数量":库存数量}}

menu="""
# # # # # # # # # # # # # # # # # # # # # # # 【图书管理系统菜单】 # # # # # # # # # # # # # # # # # #
#       1. 添加图书  2. 修改图书  3. 删除图书  4. 查询图书  5. 列出所有图书  6. 图书统计  7. 退出系统       #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""

print(menu)

while True:
    operation=int(input("请输入你要进行的操作："))
    # 添加图书
    match operation:

        case 1:
            name = input("请输入图书的书名：")
            if name in books_dict:
                print("该图书已存在，请选择修改功能！！")
                continue
            else:
                author=input("请输入图书的作者：")
                price=float(input("请输入图书的价格："))
                stock=int(input("请输入图书的库存数量："))
                books_dict[name]={"author":author,"price":price,"stock":stock}
                print("添加图书成功！！！")
                continue
        # 修改图书
        case 2:
            name=input("请输入你要修改的图书的书名：")
            if name not in books_dict:
                print("该图书不在系统中，请先去添加图书信息！！")
                continue
            else:
                author=input("请输入新的作者：")
                price=float(input("请输入新的价格："))
                stock=int(input("请输入新的库存数量："))
                books_dict[name]={"author":author,"price":price,"stock":stock}
                print("修改图书信息成功！！！")
                continue
        # 删除图书
        case 3:
            name = input("请输入你要删除的图书的书名：")
            if name not in books_dict:
                print("你要删除的图书不存在！！！")
                continue
            else:
                books_dict.pop(name)
                print("删除成功！！！！")
                continue
        # 查询图书
        case 4:
            name=input("请输入你要查询的图书的书名：")
            if name not in books_dict:
                print("你要查询的图书不存在！！")
                continue
            else:
                print(f"{name}的作者为：{books_dict[name]['author']}",end=" ，")
                print(f"价格为：{books_dict[name]['price']}",end=" ，")
                print(f"库存数量为：{books_dict[name]['stock']}")
                continue
        # 列出所有图书
        case 5:
            for name in books_dict:
                print(f"{name}的作者为：{books_dict[name]['author']}",end="")
                print(f"价格为：{books_dict[name]['price']}",end="")
                print(f"库存数量为：{books_dict[name]['stock']}")
                continue
        # 图书统计
        case 6:
            total_books=len(books_dict)
            total_price=sum([books_dict[name]["price"] for name in books_dict])
            total_stock=sum([books_dict[name]["stock"] for name in books_dict])
            print(f"当前系统中总共有{total_books}本图书")
            print(f"当前系统中所有图书的总价格为：{total_price}")
            print(f"当前系统中所有图书的总库存数量为：{total_stock}")
            continue
        # 退出系统
        case 7:
            print("谢谢使用，再见！")
            break
        case _:
            print("请输入正确的操作！！")
            continue
