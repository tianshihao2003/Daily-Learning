"""
需求1：要求输入梯形的上底、下底、高，然后计算梯形的面积
需求2：要求输入圆的半径，然后计算圆的周长和面积(周长：2πr，面积：πr²)
需求3：身体质量指数BMI的计算（BMI = 体重(kg)／身高(m)²)
        a． 输入体重(单位kg)
        b． 输入身高(单位m)
        c． 计算身体质量指数BMI并输出
需求4：输入一个秒数，把它转换成小时+分钟+秒输出。例如输入 130→输出：0小时 2分10秒
需求5：输入苹果单价、购买重量，计算总价，并输出一句话：“苹果单价X元，购买X斤，总价X元”
需求6：输入语文、数学、英语三科成绩，计算总分和平均分，并输出。
需求7：接收用户输入一个整数，判断该数字是否大于10并且小于50，打印最终判断结果（True/False）。
需求8：接收用户输入一个整数，判断该数字是否小于等于10或者大于等于50，打印最终判断结果（如果满
足条件输出True，不满足输出False）。
需求9：输入语文、数学成绩，判断是否至少有一科分数大于90 分，输出结果（如果有输出True，没有输出
False)。
需求10:
    模拟成绩统计与评优：
        i．输入姓名、语文成绩、英语成绩；
        ii． 计算两科总分与平均分;
        iii． 评优规则：两科分数都大于 85 分 或者 总分大于 180 分，评为优秀；
        iv．输出结果：姓名、总分、平均分、是否评为优秀。具体格式为： 姓名：王林，总分：192，平均分：
        96，是否评为优秀：True
"""
from functools import total_ordering

# print("=========================================")
# # 需求1：要求输入梯形的上底、下底、高，然后计算梯形的面积
# print("需求1")
# shangdi=float(input("请输入梯形的上底:\n"))
# xiadi=float(input("请输入梯形的下底:\n"))
# gao=float(input("请输入梯形的高:\n"))
#
# print("梯形的面积为: %s"%((shangdi+xiadi)*gao*0.5))


# print("=========================================")
# # 需求2：要求输入圆的半径，然后计算圆的周长和面积(周长：2πr，面积：πr²)
# print("需求2")
#
# PI=3.1415926
# r=float(input("请输入圆的半径:\n"))
# print(f"圆的周长为: {PI*r*r}\n圆的周长为: {2*PI*r}")


# print("=========================================")
# 需求3：身体质量指数BMI的计算（BMI = 体重(kg)／身高(m)²)
# Weight, Height
# print("需求3")
#
# weight=float(input("请输入你的体重(单位kg):\n"))
# height=float(input("请输入你的身高(单位m):\n"))
#
# BMI=weight/height
#
# print(f"你的BMI指数为: {BMI}")


# # print("=========================================")
# # 需求4：输入一个秒数，把它转换成小时+分钟+秒输出。例如输入 130→输出：0小时 2分10秒
# # Hours, Minutes, Seconds
# print("需求4")
# seconds=int(input("请输入一个秒数:\n"))
# """
# 一分钟60s
# 一小时3600s
# """
# Hours=seconds//3600
# Minutes=seconds//60%60
# seconds=seconds%60
#
# print(f"{Hours}时{Minutes}分{seconds}秒")

# # print("=========================================")
# # 需求5：输入苹果单价、购买重量，计算总价，并输出一句话：“苹果单价X元，购买X斤，总价X元”
#
# # 苹果,单价,重量,价格
# # Apple, unit price, weight, price
#
# apple_unit=float(input("请输入苹果单价:\n"))
# weight=float(input("请输入购入重量:\n"))
#
# # Total 总计
#
# total_price=apple_unit*weight
#
# print(f"苹果单价:{apple_unit}元,购买{weight}斤,总价{total_price}元")


# print("=========================================")
# 需求6：输入语文、数学、英语三科成绩，计算总分和平均分，并输出。

# 语文,数学,英语,总分,平均分
# Chinese, Mathematics, English, Total Score, Average Score

# chinese=float(input("请输入你的语文成绩:\n"))
# mathematics=float(input("请输入你的数学成绩:\n"))
# english=float(input("请输入你的英语成绩:\n"))
#
# total_score=chinese+mathematics+english
#
# average_score=total_score/3
#
# print(f"你的总分为:{total_score},平均分为:{average_score}")

# print("=========================================")
# # 需求7：接收用户输入一个整数，判断该数字是否大于10并且小于50，
# #       打印最终判断结果（True/False）。
# enter_int=int(input("请输入一个人整数:\n"))
#
# print(f"结果为:{(enter_int> 10) and (enter_int<50)}")


# print("=========================================")
# 需求8：接收用户输入一个整数，判断该数字是否小于等于10或者大于等于50，
#       打印最终判断结果（如果满足条件输出True，不满足输出False）。
# enter_int = int(input("请输入一个整数:\n"))
#
# print(f"结果为:{(enter_int<= 10) or (enter_int>=50)}")

# 需求9：输入语文、数学成绩，判断是否至少有一科分数大于90 分，\
#       输出结果（如果有输出True，没有输出False)。

# chinese=float(input("请输入你的语文成绩:\n"))
# mathematics=float(input("请输入你的数学成绩:\n"))
#
# print(f"结果为{chinese>90 or mathematics>90}")

# print("=========================================")
# 需求10:
#     模拟成绩统计与评优：
#         i．输入姓名、语文成绩、英语成绩；
#         ii． 计算两科总分与平均分;
#         iii． 评优规则：两科分数都大于 85 分 或者 总分大于 180 分，评为优秀；
#         iv．输出结果：姓名、总分、平均分、是否评为优秀。具体格式为： 姓名：王林，
#         总分：192，平均分：96，是否评为优秀：True

name = input("请输入你的姓名:\n")
chinese=float(input("请输入你的语文成绩:\n"))
english=float(input("请输入你的英语成绩:\n"))

total_score=chinese+english
average_score=total_score/2

print("True为优秀,False为不优秀")
print((chinese>85 and english>85) or (total_score>180))
print(f"姓名:{name},总分:{total_score},平均分:{average_score},是否评为优秀:{(chinese>85 and english>85) or (total_score>180)}")

