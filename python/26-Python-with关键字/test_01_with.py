# ============================================
# 题目1：with 语句基本用法
# ============================================
# 完成以下操作：
# 1. 用 with 语句读取文件内容 |---知识点：with open(文件, 'r') as f:---|
# 2. 用 with 语句写入文件 |---知识点：with open(文件, 'w') as f:---|
# ============================================
# 在下面写你的代码：

with open("text.txt", "w") as f:
    f.write("Hello Python!")

with open("text.txt", "r") as f:
    c = f.read()
    print(c)


# ============================================
# 参考答案（写完后取消注释对比）
# ============================================
# # 写入文件
# with open('test.txt', 'w') as f:
#     f.write("Hello, Python!")
#
# # 读取文件
# with open('test.txt', 'r') as f:
#     content = f.read()
#     print(content)
