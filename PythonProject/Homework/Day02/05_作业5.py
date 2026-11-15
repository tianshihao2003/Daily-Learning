electricity=float(input("请输入你的用电度:\n"))

if electricity>4800:
    print(f"你的用电费用为:{electricity*0.7883}元")
elif electricity>=2880 and electricity<=4800:
    print(f"你的用电费用为:{electricity*0.5383}元")
elif electricity>=0:
    print(f"你的用电费用为:{electricity*0.4883}元")
else:
    print("你输入的价格不合法!!!")