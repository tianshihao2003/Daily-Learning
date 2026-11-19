# num1=100
#
# def print_num():
#     num1=200
#     print(num1)
#
# print_num()
# print(num1)
#
num2=100
num1=100
def print_num1():
    global num1
    num1=200
    print(num1)
    print(num2)
print_num1()
print(num1)
