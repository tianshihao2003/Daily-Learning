s = [56, 90, 88, 65, 90, "A", "Hello", True]

print(s)

print(s[0:5:1])
print(type(s[0:5:1]))

s.append(100)
print(s)

s.insert(1, 100)
print(s)

s.remove(100)
print(s)

s.pop(1)
print(s)

L=[2,5,2,6,777,44,232]

L.sort()
print(L)

L.reverse()
print(L)