method = input("请输入计算符号:\n")
a = float(input("请输入第一个数字:\n"))
b = float(input("请输入第二个数字:\n"))

match method:
    case "+":
        print(f"{a}+{b}={a + b}")
    case "-":
        print(f"{a}-{b}={a - b}")
    case "*":
        print(f"{a}*{b}={a * b}")
    case "/" :
        if b != 0:
            print(f"{a}/{b}={a / b}")
        else:
            print("b不能等于0")

    case "_":
        print("输入不合法!!")
