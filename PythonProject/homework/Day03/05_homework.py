list01=[]

for i in range(10):
    str_list=input("请输入一个字符串:\n")
    new_list=str_list[::-1]
    list01.append(new_list)
print(list01)

for i in list01:
    print(i)