#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):  # Loop from 1 to 3 (exclusive)
        try:
            if i > a:
                raise Exception("Too far")
            else:
                result += (a ** b) / i
        except Exception:  # Catch the specific exception
            result = b + a  # Set result to b + a
            break
    return result
