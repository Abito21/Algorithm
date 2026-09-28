"""
Problem:
Description:
Implement the function generateRange which takes three arguments (start, stop, step) and returns the range of integers from start to stop (inclusive) in increments of step.

Examples
(1, 10, 1) -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
(-10, 1, 1) -> [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1]
(1, 15, 20) -> [1]
Note
start < stop
step > 0

Link : https://www.codewars.com/kata/55eca815d0d20962e1000106
"""

# Solution:
def generate_range(start, stop, step):
    result = []
    current = start

    while current <= stop:
        result.append(current)
        current += step

    return result
