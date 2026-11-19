try:
    num = int(input("请输入一个整数："))
    print(num)

    list01:list=[1,2,3,4,5,6,7,8,9,10]
    index01=int(input("请输入一个索引值："))
    print(list01[index01])
except ValueError as e:
    print(f"请输入一个整数！{e}")
except IndexError as e:
    print(f"索引值超出范围！{e}")

print("这是必须要执行的代码")
