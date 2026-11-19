def print_str(str1):
    if str1 == str1[::-1]:
        return True
    else:
        return False

print(print_str("sd"))

def is_palindrome(str1):
    return str1 == str1[::-1]
print(is_palindrome("黄山落叶松叶落山黄"))

