# 打开文件
f=open("诗.txt","r",encoding="utf-8")
# 读取文件内容
content=f.read()
print(content)
# 关闭文件
f.close()
print(type(content))
print(len(content))
print(content.count("飞"))
