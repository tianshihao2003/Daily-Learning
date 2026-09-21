# ============================================
# 题目2：让 Agent 自己记住用户信息
# ============================================
# 完成以下操作：
# 自定义 class CustomState(AgentState) 加一个 user_id 字段（NotRequired[str]）
# 写 save_user_info(name, runtime: ToolRuntime) 与 get_user_info(runtime: ToolRuntime) 两个工具
# 创建 Agent 时传 store=store、state_schema=CustomState
# 先让它记住"我叫韩立"（invoke 时带 "user_id": "user_1"）
# 再用新的 thread_id 问"我叫什么？"，观察长期记忆是否跨会话生效
# ============================================

# 在下面写你的代码：
