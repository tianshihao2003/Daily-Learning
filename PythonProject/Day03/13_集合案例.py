# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}

# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁","王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}

# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子",  "红蝶", "厉飞雨", "韩立", "曾牛"}

# 选修艺术学生名单
art_set = { "遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}

print(f"同时选修了法语和艺术的学生有：{french_set.intersection(art_set)}")

print(f"同时选修了所有课程的学生有：{french_set.intersection(art_set).difference(football_set).difference(basketball_set)}")


print(f"选修了足球，但是没有选修篮球的学生有：{football_set.difference(basketball_set)})")

# 去重

new_set = football_set | basketball_set | art_set

# 没去重
new_list = [*art_set,*football_set,*basketball_set,french_set]


for name in new_set:
    num_name = new_list.count(name)
    print(f"{name}选了{num_name}门课程！")