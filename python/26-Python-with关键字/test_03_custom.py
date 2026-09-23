# ============================================
# 题目3：自定义上下文管理器
# ============================================
# 完成以下操作：
# 1. 用类实现一个计时器上下文管理器 |---知识点：class 类名:---|
# 2. 记录代码执行时间 |---知识点：__enter__、__exit__---|
# ============================================
# 在下面写你的代码：


# ============================================
# 参考答案（写完后取消注释对比）
# ============================================
# class Timer:
#     def __enter__(self):
#         import time
#         self.start = time.time()
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         import time
#         self.end = time.time()
#         print(f"耗时: {self.end - self.start:.2f}秒")
#         return False
#
# # 使用示例
# with Timer():
#     total = sum(range(1000000))
#     print(f"计算结果: {total}")
