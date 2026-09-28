# ============================================
# 题目2-4：一群对象放在一起
# ============================================
# 完成以下操作：
# 1. 定义一个"商品"类（名称、价格）
# 2. 创建 3 个商品对象放进一个列表，遍历列表打印每个商品
# 3. 找出价格最高的那件商品（先让 Python 知道两个商品之间怎么比大小，再借用内置的"取最大值"）
# ============================================

# 在下面写你的代码：
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return f"{self.name} - {self.price}"
    def __lt__(self, other):
        return self.price < other.price

# 创建 3 个商品对象放进一个列表，遍历列表打印每个商品
Product1 = Product("商品A", 100)
Product2 = Product("商品A", 100)
Product3 = Product("商品B", 200)
Product_list = [Product1, Product2, Product3]
for Product in Product_list:
    print(Product)

# 找出价格最高的那件商品
max_Product = max(Product_list)
print(f"价格最高的商品是 {max_Product}")


