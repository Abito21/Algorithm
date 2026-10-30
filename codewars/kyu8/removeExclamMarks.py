"""
Problem:
Description:
Write function RemoveExclamationMarks which removes all exclamation marks from a given string.

Link : https://www.codewars.com/kata/57a0885cbb9944e24c00008e
"""

# Solution:
def remove_exclamation_marks(s):
    result = []

    for char in s:
        if char != "!":
            result.append(char)

    return "".join(result)
