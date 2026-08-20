"""
Problem:
Description:
Write a method, that will get an integer array as parameter and will process every number from this array.

Return a new array with processing every number of the input-array like this:

If the number has an integer square root, take this, otherwise square the number.

Example
[4,3,9,7,2,1] -> [2,9,3,49,4,1]
Notes
The input array will always contain only positive numbers, and will never be empty or null.

Link : https://www.codewars.com/kata/57f6ad55cca6e045d2000627
"""

# Solution:
def square_or_square_root(arr):
    result = []
    
    for num in arr:
        root = 1
        
        while root * root < num:
            root += 1
        
        if root * root == num:
            result.append(root)
        else:
            result.append(num * num)
    
    return result
