l = []

# 1. 从键盘输入10个整数，将其存储到列表l
for i in range(10):
    s = int(input("请输入一个整数："))
    l.append(s)
print(l)

# 2. 对列表l进行排序
l.sort()
print(l)

# 3. 找印列表l中最大的数和最小的数
print(l[-1])
print(l[0])

# 4. 计算列表l中所有元素的平均值
sum1=0

for i in range(10):
    sum1 = sum1 + l[i]
print(sum1/10)

print(sum(l)/len(l))
