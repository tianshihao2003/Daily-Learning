dict1 = {"小智": 675, "李思": 608, "李琪": 478, "小黑": 545, "温韬": 429}

for key in dict1.keys():
    value=dict1[key]
    print(key,value)
print("="*20)
for key in dict1:
    value=dict1[key]
    print(key,value)
print("="*20)
for i in dict1.items():
    print(i[0],i[1])


