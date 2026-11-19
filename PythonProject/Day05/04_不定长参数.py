def print_organize(*args):
    max_num=max(args)
    min_num=min(args)
    avg_score=sum(args)/len(args)
    return max_num,min_num,avg_score

print(print_organize(100,200,300,400,500))
