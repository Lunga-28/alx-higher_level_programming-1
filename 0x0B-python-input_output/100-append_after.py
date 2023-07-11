#!/usr/bin/python3
"""
function that inserts a line of text to a file
"""

def append_after(filename="", search_string="", new_string=""):
    """
    function that inserts text
    after a specific line
    """
  
    string = ""
    with open(filename, encoding="utf-8") as myFile:
        for line in myFile:
            string += line
            if search_string in line:
                string += new_string

    with open(filename, mode="w") as myFile:
        myFile.write(string)
