# ============================================
# 题目2-3：让对象"会说话"、能比较
# ============================================
# 完成以下操作：
# 1. 定义一个"商品"类（名称、价格）
# 2. 直接打印对象时，显示成"商品名 价格"，而不是一串内存地址
# 3. 两件名称和价格都相同的商品，互相比较时结果为 True
# 4. 创建两个内容相同的商品和一个内容不同的商品，打印它们并两两比较
# ============================================

# 在下面写你的代码：
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return f"{self.name} {self.price}"
    def __eq__(self, other):
        return self.name == other.name and self.price == other.price

Product1 = Product("商品A", 100)
Product2 = Product("商品A", 100)
Product3 = Product("商品B", 200)
print(Product1)
print(Product2)
print(Product3)
print(Product1 == Product2)
print(Product1 == Product3)
print(Product2 == Product3)
