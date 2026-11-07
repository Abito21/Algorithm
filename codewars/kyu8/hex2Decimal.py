"""
Problem: 
Description:
Complete the function which converts hex number (given as a string) to a decimal number.

Link : 
"""

# Solution:
def hex_to_dec(s):
    result = 0

    for char in s:
        if '0' <= char <= '9':
            value = ord(char) - ord('0')
        elif 'A' <= char <= 'F':
            value = ord(char) - ord('A') + 10
        else:
            value = ord(char) - ord('a') + 10

        result = result * 16 + value

    return result
