num = int(input("请输入一个整数:\n"))

if num>100 or num<0:
    print("输入不合法")
elif 100 >= num >= 90:
    print("优秀")
elif num>=80:
    print("良好")
elif num>=70:
    print("中等")
elif num>=60:
    print("及格")
else:
    print("不及格")
