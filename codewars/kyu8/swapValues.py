"""
Problem:
Description:
I would like to be able to pass an array with two elements to my function to swap the values. However it appears that the values aren't changing.

Can you figure out what's wrong here?

Link : https://www.codewars.com/kata/5388f0e00b24c5635e000fc6
"""

# Solution:
def swap_values(pair: list) -> None: 
    temp = pair[1]
    pair[1] = pair[0]
    pair[0] = temp
    return pair
