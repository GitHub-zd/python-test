def math_func(maths):
    if 0 <= maths <= 100:
        if maths < 75:
            print("数学的评价为：bad")
        elif 75 <= maths <85:
            print("数学评价为：good")
        else:
            print("数学评价为：great")
    else:
        print("分数输入错误，请重新输入")

def english_func(english):
    if 0 <= english <= 100:
        if english < 80:
            print("英语的评价为：bad")
        elif 80 <= english < 90:
            print("英语评价为：good")
        else:
            print("英语评价为：great")
    else:
        print("分数输入错误，请重新输入")

def history_func(history):
    if 0 <= history <= 100:
        if history < 70:
            print("历史的评价为：bad")
        elif 70 <= history <78:
            print("历史评价为：good")
        else:
            print("历史评价为：great")
    else:
        print("分数输入错误，请重新输入")

def zhesuan_func(maths,english,history):
    new_maths = maths * 1.1
    new_english = english * 1.1
    new_history = history * 0.8
    new_total = new_maths+new_english+new_history
    print("折算完总分数为：",new_total)
    return new_total

def total_func(new_total):
    if new_total >= 270:
        print("分数等级为A+")
    elif new_total >= 240:
        print("分数等级为A")
    elif new_total >= 210:
        print("分数等级为B+")
    elif new_total >= 190:
        print("分数等级为：B")
    else:
        print("分数等级为C")



if __name__ == '__main__':
    maths = int(input("请输入数学的分数："))
    english = int(input("请输入英语的分数："))
    history = int(input("请输入历史的分数："))
    math_func(maths)
    english_func(english)
    history_func(history)
    r = zhesuan_func(maths,english,history)
    total_func(r)







