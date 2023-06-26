#!/usr/bin/python3

def magic_calculation(a, b):
    resu = 0
    
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            resu += (a ** b) / i
        except:
            resu = b + a
            break
    
    return resu

