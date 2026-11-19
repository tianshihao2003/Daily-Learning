def student_score(list_score):
    """
    计算学生成绩的最高分、最低分和平均分

    :param list_score: 学生成绩列表
    :type list_score: list[int]
    :return: 最高分、最低分和平均分
    :rtype: tuple[int, int, float]
    """

    max_score = max(list_score)
    min_score = min(list_score)
    avg_score = round(sum(list_score)/len(list_score),2)

    return max_score,min_score,avg_score

student_score([1,2,3,4,5,6])
print(student_score([1,2,3,4,5,6]))


