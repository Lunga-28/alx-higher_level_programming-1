#!/usr/bin/python3

a = 1
b = 2
add_0 = __import__('add_0')
add_result = add_0.add(a, b)
print("{} + {} = {}".format(a, b, add_result))

