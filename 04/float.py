#!/usr/bin/env python3
s = input("Give me a number: ")

try:
    n = float(s)
    if n.is_integer():
        print("This number is an integer: ", int(n))
    else:
        print("This number is a decimal:", n)
except ValueError:
    print("Not a valid number.")

