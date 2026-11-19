def print_organize(*args,**kwargs):
    float_round=kwargs.get("float_round",2)\

    p=kwargs.get("p")

    max_num=max(args)
    min_num=min(args)
    avg_score=sum(args)/len(args)

    if float_round:
        avg_score=round(avg_score,float_round)

    if p:
        print(args)

    return max_num,min_num,avg_score

# print(print_organize(100,200,300,400,500))
#
# print(print_organize(10.10,20.220,300,400,500,float_round=1))

print(print_organize(10.10,20.220,300,400,500,float_round=1,p="print"))
