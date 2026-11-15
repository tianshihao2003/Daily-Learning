# 列表推导式
list01=[i ** 2 for i in range(1,21)]
print(list01)


# 普通循环实现
list02=[]

for i in range(1,21):
    new_i = i **2
    list02.append(new_i)
print(list02)

# 列表推导式实现,筛选出偶数的平方值
list03=[i ** 2 for i in range(1,21) if i%2==0]
print(list03)
