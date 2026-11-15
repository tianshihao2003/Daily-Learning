# 初始金额
money = 10000
# 密码
password = 123123
# 输入密码
pw = input("请输入你的密码：\n")
# 输入金额
out_money = input("请输入你要取的金额：\n")
# 计算余额
num = money - int(out_money)
# 输出余额
print(f"你的余额还有{num}元")
