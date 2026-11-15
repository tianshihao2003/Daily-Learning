product_total=float(input("请输入您购入商品的总额:\n"))

if product_total >= 500:
    print(f"您应支付的金额为:{product_total * 0.8}元")
elif product_total >= 300:
    print(f"您应支付的金额为:{product_total*0.9}元")
elif product_total >= 100:
    print(f"您应支付的金额为:{product_total*0.95}元")
elif 100 > product_total >= 0:
    print(f"您应支付的金额为:{product_total}元")
else:
    print("你输入的金额不合法")

