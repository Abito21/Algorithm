"""
Problem:
Description:
Return a new array consisting of elements which are multiple of their own index in input array (length > 1).

Some cases:
[22, -6, 32, 82, 9, 25] =>  [-6, 32, 25]
[68, -1, 1, -7, 10, 10] => [-1, 10]
[-56,-85,72,-26,-14,76,-27,72,35,-21,-67,87,0,21,59,27,-92,68] => [-85, 72, 0, 68]

Link : https://www.codewars.com/kata/5a34b80155519e1a00000009
"""

# Solution:
def multiple_of_index(arr):
    newArr = []
    for i in range(len(arr)):
        if i == 0:
            if arr[0] == 0:
                newArr.append(arr[i])
        elif arr[i] % i == 0:
            newArr.append(arr[i])
    return newArr
