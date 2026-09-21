"""
Problem:
Description:
Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

Return your answer as a number.

Link : https://www.codewars.com/kata/57eaeb9578748ff92a000009
"""
# Solution:
def sum_mix(arr):
    sum_num = 0
    
    for i in arr:
        if type(i) == str:
            sum_num += int(i)
        else:
            sum_num += i
    
    return sum_num
