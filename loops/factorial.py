#!/usr/bin/env python3


# factorial n
def fac(n):
    '''
    factorial of number n function
    '''


    if n == 1:
        return n
    


    else:
        return (n * fac(n-1))

print(fac(8))
