"""
1. 完成如下条件判断的需求
- 需求1：根据用户输入的数字，判断该数字是奇数还是偶数。
- 需求2：根据用户输入的年龄，判断该用户是否已经成年（>=18，成年；否则，未成年）。
- 需求3：根据用户输入的数字，判断该数字是正数还是负数还是0 。
- 需求4：根据用户输入的考试分数，判断该分数是否及格了（大于等于60就是及格了, 否则就是不及格）。
"""

# 需求一
input_num=int(input("请输入一个整数:\n"))

if input_num%2==0:
    print("是偶数")
else:
    print("是奇数")

# 需求二
input_num=int(input("请输入你的年龄:\n"))
if input_num>=18:
    print("已成年")
else:
    print("未成年")

# 需求三
input_num=int(input("请输入一个数字:\n"))
if input_num>=0:
    print("正数")
elif input_num<0:
    print("负数")
else:
    print("0")

# 需求四
input_num=int(input("请输入一个分数:\n"))

if input_num>=60:
    print("及格了")

else:
    print("不及格")