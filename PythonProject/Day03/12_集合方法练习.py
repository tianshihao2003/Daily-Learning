set01={"a","b","c"}

print(set01)

set01.add("d")
print(set01)

set01.remove("d")
print(set01)

e=set01.pop()
print(e)
print(set01)

set01.clear()
print(set01)

set02={"a","b","c"}
set03={"j","h","a"}

print(set02.difference(set03))

print(set02 - set03)

print(set02 | set03)

print(set02.union(set03))

print(set02.intersection(set03))
