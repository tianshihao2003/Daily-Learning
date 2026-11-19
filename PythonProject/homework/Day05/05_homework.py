# （商品名、价格、数量）、优惠券、积分、运费
# product_name 商品名
# product_price 商品价格
# product_quantity 商品数量
# coupon 优惠券
# integral 积分
# freight 运费

# 创建一批商品信息
goods_info = {
    "笔记本电脑": (4999.0, 1.0, 100.0, 200.0, 10.0),
    "鼠标":       (199.0, 2.0,  50.0, 150.0,  5.0),
    "键盘":       (299.0, 1.0,  50.0,   0.0,  5.0)
}

def product_information(set01):
    # 求商品总总金额
    product_price_sum = 0
    for item in set01:
        product_price_sum += set01[item][0] * set01[item][1]

    # 求优惠券总金额
    coupon_sum = 0
    for item in set01:
        coupon_sum += set01[item][2]

    # 判断是优惠券是否可用
    if product_price_sum >= coupon_sum:
        coupon=True
    else:
        coupon=False

    # 计算积分总和
    integral_sum = 0
    for item in set01:
        integral_sum += set01[item][3]

    # 判断积分是否可用
    if product_price_sum>integral_sum/100:
        integral=True
    else:
        integral=False

    # 计算运费总和
    freight_sum = 0
    for item in set01:
        freight_sum += set01[item][4]

    # 计算最终金额
    if coupon&integral:
        return product_price_sum-coupon_sum-integral_sum/100+freight_sum
    elif coupon:
        return product_price_sum-coupon_sum+freight_sum
    elif integral:
        return product_price_sum-integral_sum/100+freight_sum
    else:
        return product_price_sum+freight_sum


print(product_information(goods_info))















