# ============================================
# 题目3：时间转换
# ============================================
# 定义一个函数 time_convert(seconds)，将秒转换为小时、分钟、秒
# 1. 小时 = 秒 // 3600 |---知识点：整除 //---|
# 2. 分钟 = (秒 % 3600) // 60 |---知识点：取余 %---|
# 3. 剩余秒 = (秒 % 3600) % 60 |---知识点：return 字符串---|
# ============================================
# 在下面写你的代码：
def time_conver(seconds):
    hours=seconds//3600
    minutes=seconds%3600//60
    seconds=seconds%3600%60
    return f"{hours} 小时 {minutes} 分钟 {seconds} 秒"

print(time_conver(772))



# ============================================
# 参考答案（写完后取消注释对比）
# ============================================
# def time_convert(seconds):
#     hours = seconds // 3600
#     minutes = (seconds % 3600) // 60
#     seconds = (seconds % 3600) % 60
#     return f"{hours} 小时 {minutes} 分钟 {seconds} 秒"
#
# print(time_convert(3772))  # 1 小时 2 分钟 52 秒
