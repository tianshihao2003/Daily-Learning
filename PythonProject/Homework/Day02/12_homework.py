from tokenize import blank_re

balance = 10000

while True:
    options = input("1. 查询余额\n2. 存款\n3. 取款\n4. 退出\n请输入您要进行的操作:\n")

    match options:
        case "1":
            print(f"您的账户余额为{balance}")
        case "2":
            save_money = int(input("请输入你要存款的金额:\n"))
            balance = balance + save_money
        case "3":
            withdraw_money = int(input("请输入你要取款的金额:\n"))
            balance = balance - withdraw_money
        case "4":
            print("退出成功!!")
            break
