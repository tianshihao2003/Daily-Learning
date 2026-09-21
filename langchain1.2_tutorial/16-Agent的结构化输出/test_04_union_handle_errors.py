# ============================================
# 综合题：Union 多类型 + handle_errors 三种取值
# ============================================
# 完成以下操作：
# 定义 ContactInfo 和 EventDetails 两个模型
# 用 ToolStrategy(Union[ContactInfo, EventDetails]) 创建 Agent
# 分别用两段不同的文本调用（一段联系人信息、一段活动信息），看它选出哪个 Schema
# 把 handle_errors 依次设为 True、False、"请检查输入数据"，观察失败时的不同表现
# 想看错误信息就去翻消息列表里的 ToolMessage 内容
# ============================================

# 在下面写你的代码：
