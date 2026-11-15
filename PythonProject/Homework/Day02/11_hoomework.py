str1="akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd"

quantity_a=0
quantity_k=0

for i in str1:
    if i=="a":
        quantity_a=quantity_a+1

    if i=="k":
        quantity_k=quantity_k+1
print(f"有{quantity_a}个a和{quantity_k}个k")


