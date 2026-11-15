str01=input("请输入一个字符串：\n")

str02=str01[::-1]

if str01==str02:
    print("是回文")
else:
    print("不是回文")