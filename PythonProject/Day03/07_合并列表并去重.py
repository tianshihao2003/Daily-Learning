num_list1 = [1,2,3,4,5,6,7,8,9]
num_list2 = [1,2,3,4,5,6,7,8,9]

print(num_list1+num_list2)
# 合并列表
# 解包列表
new_list1 = [*num_list1,*num_list2]
print(new_list1)

# 去重
new_list2 = []

for num in new_list1:
    if num not in new_list2:
        new_list2.append(num)

print(new_list2)
