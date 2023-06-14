#!/usr/bin/python3
def uniq_add(my_list=[]):
    
    unique_set = set()

    for num1 in my_list:
        unique_set.add(num1)

 total = sum(unique_set)

    return total
