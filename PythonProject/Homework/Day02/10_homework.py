# sum=0
#
# for i in range(0,1001,5):
#     sum+=i
#
# print(sum)

sum=0

for i in range(0,1001):
    if i%5==0:
        sum=sum+i

print(sum)