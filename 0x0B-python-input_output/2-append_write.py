#!/usr/bin/python3
"""
append text
"""

def append_write(filename="", text=""):
"""
append text
"""

    with open(filename, mode="a+", encoding="utf-8") as f:
        return f.write(text)
