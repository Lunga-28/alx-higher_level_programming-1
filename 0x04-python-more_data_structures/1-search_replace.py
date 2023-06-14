#!/usr/bin/python3
def search_replace(my_list, search, replace):
    res = []
    
    for item in my_list:
        if item == search:
            
            res.append(replace)
        else:
            res.append(item)

    return res
