a = int(input("请输入a:\n"))
b = int(input("请输入b:\n"))
c = int(input("请输入c:\n"))

if (a+b>c) and (a+c>b) and (b+c>a):
    if a==b==c:
        print("等边")
    elif a==b or b==c or c==a:
        print("等腰")
    else:
        print("普通三角形")
else:
    print("不构成三角形!!")