# - [ ] **9. 字典操作练习**
#   创建文件 `test_dict.py`，完成以下操作：
#   - 创建字典 `student = {"name": "小明", "age": 18, "score": 95}`
#   - 打印 `name` 的值
#   - 添加一个键值对 `"class": "一班"`
#   - 修改 `score` 为 `100`
#   - 打印所有键和所有值

#   **参考答案：**
#   ```python
#   student = {"name": "小明", "age": 18, "score": 95}

#   print(f"name: {student['name']}")  # 小明
#   student["class"] = "一班"
#   student["score"] = 100
#   print(f"所有键: {list(student.keys())}")  # ['name', 'age', 'score', 'class']
#   print(f"所有值: {list(student.values())}")  # ['小明', 18, 100, '一班']
#   ```
student = {"name": "小明", "age": "18", "score": 95}
print(student["name"])
student["class"] = "一班"
student["score"] = 100
print(list(student.keys()))
print(list(student.values()))
