# ============================================
# 题目1：最简结构化输出
# ============================================
# 完成以下操作：
# 1. 从 .env 读取密钥，用 init_chat_model 创建模型（model_provider="openai"）
# 2. 定义 Movie 模型：title(str)、year(int)、director(str)、rating(float)，每个字段都用 Field 写中文描述
# 3. 用 model.with_structured_output(Movie) 绑定 Schema 并调用一次（问题自拟，比如让它介绍一部电影）
# 4. 打印结果、type(结果)、以及 result.title
# ============================================

# 在下面写你的代码：
