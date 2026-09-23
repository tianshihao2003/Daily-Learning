# ============================================
# 题目2：回文串判断
# ============================================
# 定义一个函数 is_palindrome(s)，判断字符串是否是回文串
# 1. 回文串：正读和反读相同 |---知识点：return s == s[::-1]---|
# 2. 字符串切片 s[::-1] 可以反转字符串 |---知识点：s[::-1]---|
# ============================================
# 在下面写你的代码：
def is_palindrome(s):
    return s == s[::-1]


print(is_palindrome("level"))


# ============================================
# 参考答案（写完后取消注释对比）
# ============================================
# def is_palindrome(s):
#     return s == s[::-1]
#
# print(is_palindrome("level"))          # True
# print(is_palindrome("hello"))          # False
# print(is_palindrome("黄山落叶松叶落山黄"))  # True
# print(is_palindrome("12321"))          # True
# print(is_palindrome("12345"))          # False
