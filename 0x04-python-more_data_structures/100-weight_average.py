#!/usr/bin/python3
def weight_average(my_list=[]):
    num = 0
    denum = 0
    for i in range(len(my_list)):
        num += my_list[i][0] * my_list[i][1]
        denum += my_list[i][1]
    if denum != 0:
        result = num / denum
    else:
        result = 0
    return result
