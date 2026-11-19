def palindrome_time(second):
    hour = second // 3600
    minute = (second // 60) % 60
    second = second % 60
    return f"{hour}:{minute}:{second}"
print(palindrome_time(123))