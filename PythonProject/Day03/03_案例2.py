# 创建两个列表
num_list1=[3,2,4,5,6,7,8,9,10]
num_list2=[3,2,4,5,6,7,8,9,10]

# 合并两个列表
for num in num_list1:
    num_list2.append(num)

# 打印合并后的列表
print(num_list2)

# 去重
new_list=[]

# 遍历num_list2，如果num不在new_list中，就将num添加到new_list中,达到去重的效果
for num in num_list2:
    if num not in new_list:
        new_list.append(num)

# 对new_list进行排序,并打印排序后的列表
new_list.sort()
print(new_list)