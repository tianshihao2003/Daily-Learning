# ============================================
# 题目3：include_raw 看 token 用量
# ============================================
# 完成以下操作：
# 1. 定义 Movie 模型（title/year/director/rating，带中文描述）
# 2. 用 with_structured_output(Movie, include_raw=True) 调用一次
# 3. 打印 resp.keys()、resp["parsed"]、resp["raw"].usage_metadata
# 4. 打印 resp["parsing_error"]，确认正常时它是 None
# 5. 挑战：让校验失败（比如把 Schema 定义成和问题完全对不上的结构），观察此时返回的三项分别是什么
# ============================================

# 在下面写你的代码：
