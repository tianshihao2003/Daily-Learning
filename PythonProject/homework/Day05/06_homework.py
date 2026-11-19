# ============================================================================
# 练习1：智能数据筛选器
# ============================================================================
#
# 题目描述：
#   请设计一个通用数据筛选函数 filter_data，要求功能如下：
#   1. 通过 *args 接收任意数量的数值数据
#   2. 通过 **kwargs 接收筛选配置，支持的配置项包括：
#      - threshold：阈值，只保留大于等于该值的数据（默认：无阈值）
#      - top_n：只保留前N个（默认：全部保留）
#      - unique：是否去重（默认 False）
#      - sort_order：排序方式，"asc" 升序 / "desc" 降序（默认 "asc"）
#   3. 为所有函数添加完整的类型注解
#   4. 可以根据传入的筛选配置，对传入的数据进行处理，返回处理后的结果


#   测试：
#     filter_data(5,2,9,1,7,3,8,2,9,4, threshold=5, unique=True, sort_order="desc")
#       → [9, 8, 7, 5]
#     filter_data(3,5,1,8,6, top_n=3)
#       → [1, 3, 5]
# ============================================================================

def filter_data(*args: int, **kwargs) -> list:
    threshold = kwargs.get("threshold", None)
    top_n = kwargs.get("top_n", None)
    unique = kwargs.get("unique", False)
    sort_order = kwargs.get("sort_order", "asc")

    data_list = list(args)

    # 判断是否有阈值
    if threshold is not None:
        data_list = [i for i in data_list if i >= threshold]


    # 判断是否有去重
    if unique:
        data_list = list(set(data_list))

    # 判断是否有排序
    if sort_order == "desc":
        # 降序
        data_list = sorted(data_list, reverse=True)
    else:
        # 升序
        data_list = sorted(data_list)



    # 判断是否有top_n
    if top_n is not None:
        data_list = data_list[:top_n]

    # 返回结果
    return data_list


print(filter_data(5, 2, 9, 1, 7, 3, 8, 2, 9, 4, threshold=5, unique=True, sort_order="desc"))

print(filter_data(3, 5, 1, 8, 6, top_n=3))
