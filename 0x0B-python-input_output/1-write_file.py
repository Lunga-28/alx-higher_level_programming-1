#!/usr/bin/python3
"""
function that writes a string to text file
"""


def write_file(filename="", text=""):
    """
    write to files
    """
  
    with open(filename, mode="w", encoding="utf-8") as myFile:
        return (myFile.write(str(text)))
