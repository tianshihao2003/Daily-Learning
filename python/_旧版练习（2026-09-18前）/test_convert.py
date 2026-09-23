# - [ ] **10. 类型转换练习**
#   创建文件 `test_convert.py`，完成以下操作：
#   - 将字符串 `"123"` 转换为整数
#   - 将整数 `100` 转换为字符串
#   - 将列表 `[1, 2, 3]` 转换为元组
#   - 将字符串 `"hello"` 转换为 bytes 类型

#   **参考答案：**
#   ```python
#   num = int("123")
#   print(f"字符串转整数: {num}, 类型: {type(num)}")  # 123, <class 'int'>

#   text = str(100)
#   print(f"整数转字符串: {text}, 类型: {type(text)}")  # 100, <class 'str'>

#   t = tuple([1, 2, 3])
#   print(f"列表转元组: {t}")  # (1, 2, 3)

#   b = bytes("hello", encoding="utf-8")
#   print(f"字符串转bytes: {b}")  # b'hello'
#   ```
a = int("123")
text = str(100)
t = tuple([1, 3, 2, 4])
c = bytes("hello", encoding="utf-8")
print(a, text, t, c)
