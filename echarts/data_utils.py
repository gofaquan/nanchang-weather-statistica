def spilt_flag(y):
    y_ = []
    for i in y:
        # 去掉 ° 这个符号以及元组中其他的标点和括号
        i = int(str(i).split('\'')[1].split('°')[0])
        y_.append(i)
        # print(i)

    return y_
