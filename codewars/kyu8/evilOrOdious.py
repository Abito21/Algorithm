"""
Problem:
Description:
An integer is Evil if it has an even number of 1's in its binary representation.
The first few Evil numbers: 3, 5, 6, 9, 10, 12, 15, 17, 18, 20
An integer is Odious if it has an odd number of 1's in its binary representation.
The first few Odious numbers: 1, 2, 4, 7, 8, 11, 13, 14, 16, 19
You have to write a function that determine if an integer is Evil of Odious, the function should return the string "It's Evil!" in case of evil number, and the string "It's Odious!" in case of odious number.

good luck :)

Link : https://www.codewars.com/kata/56fcfad9c7e1fa2472000034
"""

# Solution:
def evil(n):
    count = 0

    while n > 0:
        if n & 1:
            count += 1

        n >>= 1

    if count % 2 == 0:
        return "It's Evil!"

    return "It's Odious!"
