"""
Problem:
Task
Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

Mind the input validation.

Example
{ 6, 2, 1, 8, 10 } => 16
{ 1, 1, 11, 2, 3 } => 6
Input validation
If an empty value ( null, None, Nothing, nil etc. ) is given instead of an array, or the given array is an empty list or a list with only 1 element, return 0.

Link : https://www.codewars.com/kata/576b93db1129fcf2200001e6
"""

# Solution:
def sum_array(arr):
    if arr is None:
        return 0

    if len(arr) <= 1:
        return 0

    total = 0
    lowest = arr[0]
    highest = arr[0]

    for num in arr:
        total += num

        if num < lowest:
            lowest = num

        if num > highest:
            highest = num

    return total - lowest - highest
