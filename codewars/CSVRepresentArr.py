"""
Problem:
Description:
Create a function that returns the CSV representation of a two-dimensional numeric array.

Example:

input:
   [[ 0, 1, 2, 3, 4 ],
    [ 10,11,12,13,14 ],
    [ 20,21,22,23,24 ],
    [ 30,31,32,33,34 ]] 
    
output:
     '0,1,2,3,4\n'
    +'10,11,12,13,14\n'
    +'20,21,22,23,24\n'
    +'30,31,32,33,34'
Array's length > 2.

More details here: https://en.wikipedia.org/wiki/Comma-separated_values

Note: you shouldn't escape the \n, it should work as a new line.

Link : https://www.codewars.com/kata/5a34af40e1ce0eb1f5000036
"""

# Solution:
def to_csv_text(array):
    result = ""
    
    for i in range(len(array)):
        for j in range(len(array[i])):
            result += str(array[i][j])
            
            if j < len(array[i]) - 1:
                result += ","
        if i < len(array) - 1:
            result += "\n"
    
    return result
