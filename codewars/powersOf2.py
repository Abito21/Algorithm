"""
Problem:
Description:
Complete the function that takes a non-negative integer n as input, and returns a list of all the powers of 2 with the exponent ranging from 0 to n ( inclusive ).

Examples
n = 0  ==> [1]        # [2^0]
n = 1  ==> [1, 2]     # [2^0, 2^1]
n = 2  ==> [1, 2, 4]  # [2^0, 2^1, 2^2]

Link : https://www.codewars.com/kata/57a083a57cb1f31db7000028
"""

# Solution:
def powers_of_two(n):
    arr = []
    i = 0
    while i <= n:
        value = 2 ** i 
        arr.append(value)
        i += 1
    
    return arr
