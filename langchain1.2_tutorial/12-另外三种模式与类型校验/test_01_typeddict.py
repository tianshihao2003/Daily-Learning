# ============================================
# 题目1：TypedDict 版 Schema
# ============================================
# 完成以下操作：
# 1. 用 TypedDict 定义 MovieDict：title(str)、year(int)、director(str)、rating(float)
#    - 前三个字段用 Annotated[类型, ..., "描述"] 标成必填
#    - rating 用 Annotated[类型, "描述"]，不标必填
# 2. 绑定 with_structured_output 调用一次
# 3. 打印结果和 type(结果)，确认返回的是不是 dict
# 4. 挑战：故意在字段描述里不写清楚，看抽取效果有什么变化
# ============================================

# 在下面写你的代码：
