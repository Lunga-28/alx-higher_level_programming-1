#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    try:
        resu = fct(*args)
        return resu
    except Exception as e:
        print("Exception:", str(e), file=sys.stderr)
        return None

