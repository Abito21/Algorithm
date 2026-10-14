"""
Problem:
Description:
You will be given a list of strings. You must sort it alphabetically (case-sensitive, and based on the ASCII values of the chars) and then return the first value.

The returned value must be a string, and have "***" between each of its letters.

You should not remove or add elements from/to the array.

Link : https://www.codewars.com/kata/57cfdf34902f6ba3d300001e
"""

# Solution:
def two_sort(array):
    sorted_array = []

    for item in array:
        sorted_array.append(item)

    n = len(sorted_array)

    for i in range(n):
        for j in range(n - i - 1):
            if sorted_array[j] > sorted_array[j + 1]:
                sorted_array[j], sorted_array[j + 1] = sorted_array[j + 1], sorted_array[j]

    word = sorted_array[0]
    result = ""

    for i in range(len(word)):
        if i > 0:
            result += "***"
        result += word[i]

    return result
