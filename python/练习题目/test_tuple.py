# - [ ] **7. 元组操作练习**
#   创建文件 `test_tuple.py`，完成以下操作：
#   - 创建元组 `colors = ("红", "绿", "蓝", "黄")`
#   - 打印第一个元素和索引 1 到 3 的切片
#   - 尝试修改元组的某个元素，观察报错信息
#   - 创建只有一个元素的元组 `single = (42,)`，注意逗号

#   **参考答案：**
#   ```python
#   colors = ("红", "绿", "蓝", "黄")

#   print(f"第一个: {colors[0]}")      # 红
#   print(f"切片 [1:3]: {colors[1:3]}")  # ('绿', '蓝')

#   # 尝试修改会报错：TypeError: 'tuple' object does not support item assignment
#   # colors[0] = "紫"

#   single = (42,)
#   print(f"单元素元组: {single}")  # (42,)
#   ```
colors = ("红", "绿", "蓝", "黄")
print(f"第一个：{colors[0]}")
print(colors[1:3])
# colors[0] = '紫'
# TypeError: 'tuple' object does not support item assignment
single = [42,]
print(single)

