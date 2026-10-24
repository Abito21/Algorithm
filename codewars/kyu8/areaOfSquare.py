"""
Problem:
Description:
Complete the function that calculates the area of the red square, when the length of the circular arc A is given as the input.

Note: use the π value provided in your language (Math::PI, M_PI, math.pi, etc)

Link : https://www.codewars.com/kata/5748838ce2fab90b86001b1a
"""

# Solution:
import math

def square_area(a):
    side = (2 * a) / math.pi
    return side * side
