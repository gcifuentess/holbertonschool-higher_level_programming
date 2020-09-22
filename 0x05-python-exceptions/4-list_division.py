#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_result = []
    for i in range(list_length):
        try:
            my_result.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            my_result.append(0)
    return my_result
