num = int(input("请输入一个四位数:\n"))

ge = num % 10
shi = num // 10 % 10
bai = num // 100 % 10
qian = num // 1000 % 10

print(ge == qian and shi == bai)

year = int(input("请输入一个年份:\n"))

print((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))
