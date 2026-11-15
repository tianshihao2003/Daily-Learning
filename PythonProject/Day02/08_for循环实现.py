# i=0
# total_ji=0
#
# for i in range(1,101,2):
#     total_ji+=i
#     i+=1
# print(total_ji)
#
# j=0
# total_ou=0
# for j in range(0,101,2):
#     total_ou+=j
#     j+=1
# print(total_ou)

total=0

for i in range(100,501):
    if i%3==0:
        total+=i

print(f"有3的倍数的数字之和为{total}")

