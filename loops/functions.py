#!/usr/bin/python3


a = 58

def honme():
    print("Hello, World!")

def add(a):
    global b
    b = 5
    c = 10
    print(a + b + c)

a = 5
add(a)
print(b)