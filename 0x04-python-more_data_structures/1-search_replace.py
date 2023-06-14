#!/usr/bin/python3
def search_replace(my_list, search, replace):
    resul = []
    for item in my_list:
        if item == search:
            resul.append(replace)
        else:
            resul.append(item)

    return resul
