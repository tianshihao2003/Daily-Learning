import os
import uuid
from openai import OpenAI

# 1. 配置客户端，指定 OpenCode Go 的 base_url
client = OpenAI(
    base_url="https://opencode.ai/zen/go/v1",
    api_key=os.environ.get("OPENCODE_GO_API_KEY")  # 从环境变量读取密钥
)

# 2. 生成一个会话 ID（必须！）
#    OpenCode Go 从 2026年9月5日起强制要求 x-opencode-session 请求头
session_id = str(uuid.uuid4())

# 3. 发送请求
response = client.chat.completions.create(
    model="deepseek-v4.1-flash",  # 替换为你需要使用的模型
    messages=[
        {"role": "user", "content": "你好，请介绍一下你自己。"}
    ],
    extra_headers={
        "x-opencode-session": session_id  # 关键：会话粘性标识
    }
)

# 4. 输出结果
print(response.choices[0].message.content)