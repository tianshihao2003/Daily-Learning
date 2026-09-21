# ============================================
# 题目1：给 Agent 加上自动摘要
# ============================================
# 完成以下操作：
# 建一个带 SummarizationMiddleware 的 Agent：trigger=[("messages", 6)]、keep=("messages", 2)
# 连续 invoke 若干轮（每轮往 messages 里追加一条 HumanMessage）
# 观察触发摘要后消息条数如何"掉下来"，并找出那条摘要消息（内容形如 Here is a summary of the conversation to date:）
# 挑战：把 trigger 改成 ("fraction", 0.5)，看会不会报错，再想想怎么解决
# ============================================

# 在下面写你的代码：
