for i in range(1,7):
    if i == 6:
        print("输入错误五次，不允许再操作了")
        break

    input_user = input("请输入你的用户名:\n")
    input_password = input("请输入你的密码:\n")

    if input_user == "admin" and input_password == "666888" or input_user == "zhangsan" and input_password == "123456"or input_user == "taoge" and input_password == "888666":
        print("密码正确登录成功!")
        break
    else:
        print("账号密码错误,请重新输入!!")


