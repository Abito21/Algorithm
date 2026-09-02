"""
Problem:
If you can't sleep, just count sheeps!!

Task:
Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.

Link : https://www.codewars.com/kata/5b077ebdaf15be5c7f000077/train/python
"""

# Solution:
def count_sheep(n):
    result = ""
    i = 1
    while i <= n:
        result += str(i) + " sheep..."
        i += 1
    
    return result
