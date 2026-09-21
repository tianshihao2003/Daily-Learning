# ============================================
# 综合题：给"发邮件"加上人工审批
# ============================================
# 完成以下操作：
# 定义一个 send_email_tool（函数体里 print("真的执行了")），用 HumanInTheLoopMiddleware 对它开启审批
# 配好 checkpointer=InMemorySaver() 和 config={"configurable": {"thread_id": "1"}}
# 第一步：invoke 一次，从返回里取出 __interrupt__，打印待审批的 action_requests
# 第二步：用 Command(resume={"decisions": [{"type": "reject"}]}) 拒绝，确认工具没被执行、且产生了 rejected 的 ToolMessage
# 第三步：换个 thread_id 重来，改用 approve，确认工具真的执行了
# ============================================

# 在下面写你的代码：
