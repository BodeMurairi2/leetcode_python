#!/usr/bin/env python3


def is_square(n):
    result = n ** 0.5
    if result % 1 == 0:
        return True
    else:
        return False

print(is_square(9.5))
