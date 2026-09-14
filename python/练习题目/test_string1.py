# - [ ] **5. 字符串操作练习**
#   创建文件 `test_string.py`，完成以下操作：
#   - 定义字符串 `s = "Hello Python"`
#   - 打印第一个字符、最后一个字符
#   - 打印索引 0 到 5 的切片
#   - 打印字符串重复 3 次的结果
#   - 用 `+` 拼接字符串 `" World"`

#   **参考答案：**
#   ```python
#   s = "Hello Python"

#   print(f"第一个字符: {s[0]}")    # H
#   print(f"最后一个字符: {s[-1]}") # n
#   print(f"切片 [0:5]: {s[0:5]}") # Hello
#   print(f"重复3次: {s * 3}")     # Hello PythonHello PythonHello Python
#   print(f"拼接: {s + ' World'}") # Hello Python World
#   ```
s = "Hello Python"

print(f"第一个字符：{s[0]}")
print(f"最后一个字符：{s[-1]}")
print(f"打印索引0到5的切片：{s[0:5]}")
print(f"打印字符串重复三次的结果：{s * 3}")
print(f"用 + 拼接字符串：{s + 'word'}")
