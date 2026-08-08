"""
Problem:
Description:
Given three integers a, b, and c, return the largest number obtained after inserting the operators +, *, and parentheses (). In other words, try every combination of a, b, and c with the operators, without reordering the operands, and return the maximum value.

Example
With the numbers 1, 2, and 3, here are some possible expressions:

1 * (2 + 3) = 5
1 * 2 * 3 = 6
1 + 2 * 3 = 7
(1 + 2) * 3 = 9
The maximum value that can be obtained is 9.

Notes
The numbers are always positive, in the range 1 ≤ a, b, c ≤ 10.
You can use the same operation more than once.
It is not necessary to use all the operators or parentheses.
You cannot swap the operands. For example, with the given numbers, you cannot get the expression (1 + 3) * 2 = 8.
Input and Output Examples
expressionsMatter(1, 2, 3) ==> 9, because (1 + 2) * 3 = 9.
expressionsMatter(1, 1, 1) ==> 3, because 1 + 1 + 1 = 3.
expressionsMatter(9, 1, 1) ==> 18, because 9 * (1 + 1) = 18.

Link : https://www.codewars.com/kata/5ae62fcf252e66d44d00008e
"""

# Solution:
def expression_matter(a, b, c):
    result1 = a + b + c
    result2 = a + b * c
    result3 = a * b + c
    result4 = a * b * c
    result5 = (a + b) * c
    result6 = a * (b + c)

    largest = result1

    if result2 > largest:
        largest = result2

    if result3 > largest:
        largest = result3

    if result4 > largest:
        largest = result4

    if result5 > largest:
        largest = result5

    if result6 > largest:
        largest = result6

    return largest
                
