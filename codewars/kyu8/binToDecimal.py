"""
Problem:
Description:
Complete the function which converts a binary number (given as a string) to a decimal number.

Link : https://www.codewars.com/kata/57a5c31ce298a7e6b7000334
"""

# Solution:
def bin_to_decimal(inp):
    decimal = 0

    for bit in inp:
        decimal = decimal * 2

        if bit == '1':
            decimal += 1

    return decimal
