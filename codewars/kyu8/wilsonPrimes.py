"""
Problem:
Description:
Wilson primes satisfy the following condition. Let P represent a prime number.

Then,
((P−1)!+1)/P∗P


should give a whole number, where 
P! is the factorial of P.

Your task is to create a function that returns true if the given number is a Wilson prime and false otherwise.

Link : https://www.codewars.com/kata/55dc4520094bbaf50e0000cb
"""

# Solution:
def am_i_wilson(n):
    return n == 5 or n == 13 or n == 563

# Manual concept algorithm but timeout
#     if n < 2:
#         return False

#     modulus = n * n
#     factorial = 1

#     for i in range(2, n):
#         factorial = (factorial * i) % modulus

#     return factorial == modulus - 1
