# ============================================
# 题目2：同一份数据用 dataclass 定义
# ============================================
# 完成以下操作：
# 1. 用 @dataclass 定义 Movie：title、year、director、rating 四个字段
#    - 描述信息借用 pydantic 的 Field(description="...")
# 2. 绑定 with_structured_output 调用一次
# 3. 打印结果和 type(结果)
# 4. 对比：和题目1（TypedDict）的返回类型有什么共同点？和 Pydantic 有什么不同？
# 5. 挑战：把 @dataclass 去掉，改成手写 __init__ 的普通类，
#    用 langchain_core.utils.function_calling.convert_to_openai_tool 转换它，
#    看生成的 Schema 字段和 @dataclass 版本差在哪（会不会报错？字段还有描述吗？）
# ============================================

# 在下面写你的代码：
