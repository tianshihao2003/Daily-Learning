# ============================================
# 综合题：自己写一个 fake server，确认"只有 Pydantic 会校验"
# ============================================
# 分三步做：
#
# 第一步：写假服务端（可以就写在文件下半部分的 if __name__ 里）
#   - 监听 127.0.0.1:8889，处理 POST 请求
#   - 从请求体里取 tools[0]["function"]["name"]，打印出来
#   - 固定返回一份"字段名故意写错"的响应：
#       参数用 {"title1": "盗梦空间", "director": "克里斯托弗·诺兰", "rating": 9.3}
#       （没有 title、也没有 year）
#   - 响应里必须包含 choices[0].message.tool_calls[0].function.{name, arguments}
#     其中 arguments 是字符串形式的 JSON（要 json.dumps）
#
# 第二步：客户端用 Pydantic 模式调用
#   - ChatDeepSeek(model="deepseek-v4-flash", api_base="http://localhost:8889", api_key=...)
#   - 定义 MovieModel（title/year/director/rating）后调用，用 try/except 捕获异常
#   - 观察 ValidationError 的错误信息（注意 input_value 里的内容）
#
# 第三步：换成 TypedDict 再调一次
#   - 用 Annotated[str, ..., "电影标题"] 的写法定义 MovieDict
#   - 观察返回的字典：错误键名 title1 是不是被原样保留了？
#
# 提示：跑的时候要开两个终端——先启动服务端，再运行客户端；
#       如果写在同一个文件里，记得用 threading 把 server 放到后台线程
# ============================================

# 在下面写你的代码：
