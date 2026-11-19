def is_triangle_type(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b and b == c:
            return "等边三角形"
        elif a == b or b == c or a == c:
            return "腰三角形"
        else:
            return "普通三角形"
    else:
        return "不是三角形"

print(is_triangle_type(3,3,30))
