#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    if my_list_1 is None or my_list_2 is None:
        pass
    i = 0
    new_list = []
    while i < list_length:
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            result = 0
            pass
        except IndexError:
            print("out of range")
            result = 0
            pass
        except ZeroDivisionError:
            print("division by 0")
            result = 0
            pass
        finally:
            new_list.append(result)
        i += 1

    return new_list
