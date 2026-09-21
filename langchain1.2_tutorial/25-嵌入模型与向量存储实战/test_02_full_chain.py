# ============================================
# 题目2：走一遍完整链路：加载 → 切分 → 向量化 → 入库
# ============================================
# 完成以下操作：
# 自造一份 knowledge.txt（写几条"公司政策/产品说明"）
# 用 TextLoader + RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20) 切分
# 用伪嵌入把每个 chunk 写进 InMemoryVectorStore（metadata 里带上 source 和 chunk_id）
# 打印"入库了多少条"，并做一次检索
# ============================================

# 在下面写你的代码：
