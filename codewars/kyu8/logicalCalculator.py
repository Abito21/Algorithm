"""
Problem:
Description:
Your Task
Given an array of Boolean values and a logical operator, return a Boolean result based on sequentially applying the operator to the values in the array.

Examples
booleans = [True, True, False], operator = "AND"
True AND True -> True
True AND False -> False
return False
booleans = [True, True, False], operator = "OR"
True OR True -> True
True OR False -> True
return True
booleans = [True, True, False], operator = "XOR"
True XOR True -> False
False XOR False -> False
return False
Input
an array of Boolean values (1 <= array_length <= 50)
a string specifying a logical operator: "AND", "OR", "XOR"
Output
A Boolean value (True or False).

Link : https://www.codewars.com/kata/57096af70dad013aa200007b
"""

# Solution:
def logical_calc(array, op):
    result = array[0]

    for value in array[1:]:
        if op == "AND":
            result = result and value
        elif op == "OR":
            result = result or value
        else:
            result = result != value

    return result
