long = int(input("请输入直角三角形的边长:\n"))

for i in range(1,long+1):

    for j in range(1,i+1):
        print("*", end="  ")

    print()