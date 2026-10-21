"""
Problem:
Description:
Create a method that accepts a list and an item, and returns true if the item belongs to the list, otherwise false.

Link : https://www.codewars.com/kata/545991b4cbae2a5fda000158
"""

# Solution:
def include(arr, item):
    for i in arr:
        if i == item:
            return True
    return False
