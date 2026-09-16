# ============================================
# 题目4：字符串查找与判断
# ============================================
# 完成以下操作：
# 1. 查找 "hello world" 中 world 的位置
# -> 查找位置：s.find(子串)（找不到返回-1）
# 2. 判断字符串是否以 hello 开头
# -> 判断开头：s.startswith(子串)
# 3. 判断字符串是否以 world 结尾
# -> 判断结尾：s.endswith(子串)
# 4. 判断字符串是否只包含字母
# -> 判断字母：s.isalpha()
# ============================================

# 在下面写你的代码：
s = "hello world"

print(s.find("world"))
print(s.startswith("hello"))
print(s.endswith("world"))
print('hello'.isalpha())


# ============================================
# 参考答案（写完后取消注释对比）
# ============================================
# s = "hello world"
#
# print(f"world的位置: {s.find('world')}")    # 6
# print(f"是否以hello开头: {s.startswith('hello')}")  # True
# print(f"是否以world结尾: {s.endswith('world')}")    # True
# print(f"是否只包含字母: {'hello'.isalpha()}")       # True
