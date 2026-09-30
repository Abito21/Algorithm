"""
Problem:
Description:
Implement a function that returns true when a given string only contains a single digit (0-9), false otherwise.

Link : https://www.codewars.com/kata/567bf4f7ee34510f69000032
"""

# Solution:
def is_digit(n):
    if len(n) != 1:
        return False

    if ord(n) >= 48 and ord(n) <= 57:
        return True

    return False
