"""
Problem:
Description:
Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty ( zero length ).

Hint for R users:

The length of string is not always the same as the number of characters
For example: (Input1, Input2) --> output

("1", "22") --> "1221"
("22", "1") --> "1221"

Link : https://www.codewars.com/kata/50654ddff44f800200000007
"""

# Solution:
def solution(a, b):
    panjang_a = 0
    panjang_b = 0

    for karakter in a:
        panjang_a = panjang_a + 1

    for karakter in b:
        panjang_b = panjang_b + 1

    if panjang_a < panjang_b:
        short = a
        long = b

    else:
        short = b
        long = a
    hasil = short + long + short

    return hasil
