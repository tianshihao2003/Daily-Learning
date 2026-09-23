# ============================================
# 题目4：contextlib 模块
# ============================================
# 完成以下操作：
# 1. 用 @contextmanager 装饰器创建上下文管理器 |---知识点：from contextlib import contextmanager---|
# 2. 实现一个简单的标签生成器 |---知识点：@contextmanager、yield---|
# ============================================
# 在下面写你的代码：


# ============================================
# 参考答案（写完后取消注释对比）
# ============================================
# from contextlib import contextmanager
#
# @contextmanager
# def tag(name):
#     print(f"<{name}>")
#     yield
#     print(f"</{name}>")
#
# # 使用示例
# with tag("h1"):
#     print("这是一个标题")
#
# with tag("p"):
#     print("这是一个段落")
