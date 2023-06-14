#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for srt in sorted(a_dictionary.keys()):
print("{}: {}".format(srt, a_dictionary[srt]))
