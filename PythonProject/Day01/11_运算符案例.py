a = 324

# 324除10取余数
ge = a % 10

# 十位变个位，然后复用
shi = a // 10 % 10

# 同理
bai = a // 100 % 10

print(ge, shi, bai)
