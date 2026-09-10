"""
Problem:
Complete the function that takes two integers (a, b, where a < b) and return an array of all integers between the input parameters, including them.

For example:

a = 1
b = 4
--> [1, 2, 3, 4]

Link : https://www.codewars.com/kata/55ecd718f46fba02e5000029
"""

# Solution:
def between(a,b):
    arr = []
    distance = b - a
    num = a
    
    for i in range(0, distance + 1):
        arr.append(num)
        num = num + 1
        
    return arr
