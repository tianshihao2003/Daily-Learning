# 定义列表
names = ['张三', '李四', '王五']
print(names)

# 访问列表中的元素
print(names[0])
print(names[1])
print(names[2])

# 访问列表中的元素，从后往前访问
print(names[-1])
print(names[-2])
print(names[-3])

# 修改列表中的元素
names[2] = "hangman"
print(names)

# 删除列表中的元素
del names[2]

# 遍历列表中的元素
for num in names:
    print(num)

# 遍历列表中的元素，同时获取元素的索引
for index,num in enumerate(names):
    print(f"{index} {num}")

