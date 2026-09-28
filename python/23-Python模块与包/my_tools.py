AUTHOR = "涛哥"

def print_hello():
    print("你好，我是自定义模块里的函数")

def print_jian():
    print("-"*30)

def print_jia():
    print("-"*30)

def print_xing():
    print("#"*30)

# 在 my_tools.py 里用模块级的特殊变量只放行其中 2 个功能，其余的不让通配导入拿到
__all__ = ["print_hello", "print_jian"]

if __name__ == "__main__":
    print("my_tools 被直接运行，当前模块名：", __name__)
    print_hello()
