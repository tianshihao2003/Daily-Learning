# 合并如下三个列表，并对合并后的列表进行元素的去重，然后排好序后输出到控制台
list1 = ['M', 'A', 'C', 'E', 'F', 'G', 'H', 'L', 'N', 'I', 'J', 'K', 'O']
list2 = ['X', 'Z', 'T', 'Y', 'D', 'E', 'F', 'G']
list3 = ['W', 'A', 'S', 'D']

new_list=list1+list2+list3

new_list01=[]

for i in new_list:
    if i not in new_list01:
        new_list01.append(i)

print(new_list01)

new_list01.sort()
print(new_list01)