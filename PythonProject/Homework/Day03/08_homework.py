# 【题目】
# 已知两个班级的学员编号：
# class_a = [101, 102, 105, 108, 102, 110, 105, 112, 108]
# class_b = [105, 106, 108, 109, 111, 101, 113, 106]
#
# 请完成以下操作：
# 1. 合并两个列表的数据，得到合并后的原始列表 merged
# 2. 对 merged 进行列表去重，保留第一次出现的顺序，得到 unique_list
# 3. 使用列表推导式，从 unique_list 中筛选出所有的奇数编号，生成 odd_list，并输出
# 4. 使用列表推导式，odd_list 中每个元素在其基础上加 10000，生成 new_list，并输出


class_a = [101, 102, 105, 108, 102, 110, 105, 112, 108]
class_b = [105, 106, 108, 109, 111, 101, 113, 106]

merged=[*class_a,*class_b]

print(merged)

unique_list=[]

for i in class_a:
    if i not in unique_list:
        unique_list.append(i)
odd_list=[i for i in unique_list if i % 2 ==1]
print(odd_list)

new_list=[i+10000 for i in odd_list if i % 2 ==1]

print(new_list)