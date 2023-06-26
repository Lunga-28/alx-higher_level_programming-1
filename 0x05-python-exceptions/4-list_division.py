#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:
        for i in range(list_length):
            try:
                a = my_list_1[i]
                b = my_list_2[i]
                if isinstance(a, (int, float)) and isinstance(b, (int, float)):
                    try:
                        result = a / b
                        new_list.append(result)
                    except ZeroDivisionError:
                        new_list.append(0)
                        print("division by 0")
                else:
                    new_list.append(0)
                    print("wrong type")
            except IndexError:
                new_list.append(0)
                print("out of range")
    except:
        print("An error occurred.")
    finally:
        return new_list

