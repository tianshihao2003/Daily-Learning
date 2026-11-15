dict1 = {"小智": 675, "李思": 608, "李琪": 478, "小黑": 545, "温韬": 429}

dict1["王林"]=999
print(dict1)

re = dict1.pop("小智")
print(dict1)
print(re)

del dict1["李思"]
print(dict1)

dict1["小黑"]=888
print(dict1)

print(dict1["小黑"])

print(dict1.get("小黑"))
print(dict1.keys())
print(dict1.values())
print(dict1.items())


