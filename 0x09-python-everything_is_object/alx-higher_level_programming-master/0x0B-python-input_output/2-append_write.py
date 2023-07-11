#!/usr/bin/python3

"""
module: 2-append_write
resources: append_write() function
"""


def append_write(filename="", text=""):
    """
    The purpose of this function is to append
    some text to a specified file and returning
    the number o bytes appended
    """
    with open(filename, "a", encoding="utf-8") as file:
        count_appended = file.write(text)
    return count_appended
