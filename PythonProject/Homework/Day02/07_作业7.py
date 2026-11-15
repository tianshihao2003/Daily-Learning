while True:
    input_command=input("请输入游戏指令:\n")

    match input_command:
        case "w" | "W":
            print("角色向上移动了~")
            continue
        case "s" | "S":
            print("角色向下移动了~")
            continue
        case "a" | "A":
            print("角色向左移动了~")
            continue
        case "d" | "D":
            print("角色向右移动了~")
            continue
        case " ":
            print("角色跳跃了~")
            continue
        case "j" | "J":
            print("角色发起攻击了~")
            continue
        case "esc" | "ESC":
            print("角色退出游戏了~")
            break
        case _:
            print("你输入的指令不合法请重新输入")
            continue
