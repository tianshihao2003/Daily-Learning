# ============================================
# 题目5：bool() 转换练习
# ============================================
# 完成以下操作，运行并记录哪些是 True，哪些是 False：
# 1. 测试 0、1、-1
# 2. 测试 ""、"0"、"False"
# 3. 测试 []、[0]
# 4. 测试 None
# ============================================

# 在下面写你的代码：


print(bool(0),bool(1),bool(-1),bool(''),bool(False),bool([]),bool(None))

# ============================================
# 参考答案（写完后取消注释对比）
# ============================================
# print(f"bool(0) = {bool(0)}")         # False
# print(f"bool(1) = {bool(1)}")         # True
# print(f"bool(-1) = {bool(-1)}")       # True
# print(f"bool('') = {bool('')}")       # False
# print(f"bool('0') = {bool('0')}")     # True（非空字符串）
# print(f"bool('False') = {bool('False')}")  # True（非空字符串）
# print(f"bool([]) = {bool([])}")       # False
# print(f"bool([0]) = {bool([0])}")     # True（非空列表）
# print(f"bool(None) = {bool(None)}")   # False
#
# 规律：0、空字符串、空列表、None 转换为 False，其他为 True
