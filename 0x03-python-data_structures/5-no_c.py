#!/usr/bin/python3
def no_c(my_string):
    new_strng = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_strng += char
    return new_strng
