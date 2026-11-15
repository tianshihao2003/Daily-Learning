year = input("请输入一个月份(阿拉伯数字):\n")

match year:
    case "3" | "4" | "5" :
        print("所在季节为春季!!")
    case "6" | "7" | "8" :
        print("所在季节为夏季!!")
    case "9" | "10" | "11" :
        print("所在季节为秋季!!")
    case "12" | "1" | "2" :
        print("所在季节为冬季!!")
    case _:
        print("输入季节非法!!")