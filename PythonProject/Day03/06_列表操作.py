nums=[]

for i in range(10):

    s=input("请输入一个数字:")
    nums.append(int(s))

print(nums)

print(max(nums))
print(min(nums))

print(sum(nums)/len(nums))