# 将如下列表中的正数提取出来，封装为一个新的列表。
list1 = [11, 2, 31, 4, -5, 15, 17, 28, 49, 10, -11, 16, 54, -14, 36, -16, 87, -39]

new_list = []

for i in list1:
    if i >0:
        new_list.append(i)

print(new_list)