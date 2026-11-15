import random

random_num = random.randint(1, 100)

input_num = 0

while True:

    input_num=int(input("请输入你猜想的数字:\n"))

    if input_num>random_num:
        print("你猜大了!!")
        continue
    if input_num<random_num:
        print("你猜小了!!")
        continue
    if input_num==random_num:
        print("你猜对了!!")
        break

print(f"你本轮所猜的数字为:{random_num}")


