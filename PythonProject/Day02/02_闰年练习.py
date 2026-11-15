year = int(input("请输入一个年份:\n"))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 and year % 100 == 0:

    print("这是一个闰年")

else:
    print("这不是一个闰年")
