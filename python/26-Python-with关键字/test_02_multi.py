# ============================================
# 题目2：同时操作多个文件
# ============================================
# 完成以下操作：
# 1. 用 with 同时打开两个文件 |---知识点：with open(文件1) as f1, open(文件2) as f2:---|
# 2. 从一个文件读取内容，写入另一个文件 |---知识点：f.read()、f.write()---|
# ============================================
# 在下面写你的代码：
with open('source.txt','w') as f:
    f.write("你好")

with open('source.txt','r') as f1,open('dest.txt','w') as f2:
    s=f1.read()
    print(s)
    f2.write(s.upper())
    print(f2)
    



# ============================================
# 参考答案（写完后取消注释对比）
# ============================================
# # 先创建源文件
# with open('source.txt', 'w') as f:
#     f.write("这是源文件内容")
#
# # 同时读取和写入
# with open('source.txt', 'r') as infile, open('dest.txt', 'w') as outfile:
#     content = infile.read()
#     outfile.write(content.upper())
#     print("复制完成")
