print("开始登录!!!")

input_user=input("请输入你的用户名:\n")
input_password=input("请输入你的密码:\n")

user="admin"
password="666888"

while True:
    if input_user==user and input_password==password:
        print("登录成功，进入B站首页~")
        break
    elif input_user==user and input_password!=password:
        input_password=input("密码错误请重新输入：\n")
        continue
    else:
        print("用户名和密码都输错了请重新输入！！！")
        input_user = input("请输入你的用户名:\n")
        input_password = input("请输入你的密码:\n")
        continue


