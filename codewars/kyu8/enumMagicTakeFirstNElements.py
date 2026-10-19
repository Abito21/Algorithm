"""
Problem:
Description:
Create a function that accepts a sequence and a non-negative integer n, and returns a sequence of the first n elements from it.

If the sequence has fewer than n elements, return all of them.

Examples
[0, 1, 2, 3, 5, 8, 13], n = 3  =>  [0, 1, 2]
[0, 1, 2, 3, 5, 8, 13], n = 0  =>  []
                    [], n = 3  =>  []
If you need help, here's a reference:

https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range

Link : https://www.codewars.com/kata/545afd0761aa4c3055001386
"""

# Solution:
def take(arr,n):
    newArr = []
    
    for i in range(0, len(arr)):
        if i < n:
            newArr.append(arr[i])
    
    return newArr
