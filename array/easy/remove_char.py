#!/usr/bin/env python3


def filter_list(l):
    new_list = []
    for char in l:
        if isinstance(char, int) or type(char) == int:
            new_list.append(char)
    return new_list

print(filter_list(l= [1, 5, 6, "bode", "dirac", "123", "programming", 10]))