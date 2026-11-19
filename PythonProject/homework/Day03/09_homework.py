# 1. 找出同时参加了所有四个小组的学生（四重交集）
# 2. 找出参加了书法组，但既没有参加绘画组也没有参加音乐组的学生
# 3. 使用集合推导式找出参加了书法组，但没有参加体育组的学生
# 4. 求出所有参赛学生名单（四组并集），并统计总人数
# 5. 统计每位学生在四个小组中总共出现的次数, 并输出(形式为: xxx 参加了 xxx 个小组)

# 书法组
calligraphy_set = {"王林", "曾牛", "天运子", "韩立", "厉飞雨", "紫灵", "徐立国"}
# 绘画组
painting_set    = {"张铁", "王林", "曾牛", "王蝉", "韩立", "厉飞雨", "云露", "李化元"}
# 音乐组
music_set       = {"许木", "红蝶", "韩立", "天运子", "厉飞雨", "曾牛", "虎咆"}
# 体育组
sports_set      = {"遁天", "天运子", "韩立", "姜老道", "紫灵", "云露", "虎咆"}

print(f"同时参加了所有小组的同学有{calligraphy_set & painting_set & music_set & sports_set}")
print(f"同时参加了所有小组的同学有{calligraphy_set.intersection(painting_set).intersection(sports_set).intersection(music_set)}")


print(f"参加了书法组，但既没有参加绘画组也没有参加音乐组的学生:{calligraphy_set.difference(painting_set).difference(music_set)}")


calligraphy_set.difference(music_set)

list01=[i for i in calligraphy_set if i not in sports_set]

print(f"参加了书法组，但没有参加体育组的学生:{list01}")

# 重复名单
list02=*calligraphy_set,*painting_set,*music_set,*sports_set

print(f"重复名单:{list02}")

# 不重复名单
list03=calligraphy_set | painting_set | music_set | sports_set

print(f"不重复名单:{list03}")

# 4. 求出所有参赛学生名单（四组并集），并统计总人数

times = 0
for i in list03:
    times+=1

print(f"总人数：{times}")
# 5. 统计每位学生在四个小组中总共出现的次数, 并输出(形式为: xxx 参加了 xxx 个小组)

for i in list03:
    print(f"{i}参加了{list02.count(i)}个小组")
