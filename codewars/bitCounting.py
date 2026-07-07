"""
Problem:
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

Link : 
"""

# Solution:
def count_bits(n):
  if n == 0:
    return 0

  sum_bit = 0

  while n > 0:
    bit = n % 2
    sum_bit += bit
    n //= 2
    
  return sum_bit
