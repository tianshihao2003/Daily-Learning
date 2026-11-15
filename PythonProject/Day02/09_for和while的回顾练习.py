total = 0

for i in range(1, 201):
    if i % 5 == 0:
        total += i

print(f"使用for循环:{total}")
#######################################

total1 = 0
j=0

while j < 201:
    if j % 5 == 0:
        total1 += j
    j += 1

print(f"使用while循环:{total1}")
