"""
Problem:
Description:
You own a box-making company that can produce boxes in the shape of any regular polygon.
Many customers use these boxes to transport circular objects - such as tin cans, glasses, tyres, or CDs.

To assist them, you decided to print on every box the diameter of the largest circle that can fit inside the box.

Input
The number of equal sides of the regular polygon (sides ≥ 3),
The length of each side of the polygon.
Output
Return the diameter of the largest circular item that can fit inside the polygon, accurate up to 0.001.

Examples
A box of 4 sides and a side length of 10 can hold a circular item of diameter 10.
A box of 8 sides and a side length of 9 can hold a circular item of diameter approx. 21.72792206.

Link : https://www.codewars.com/kata/5a026a9cffe75fbace00007f/train/python
"""

# Solution:
def circle_diameter(sides, side_length): 
    pi = 3.141592653589793
    x = pi / sides

    sin_x = x
    cos_x = 1.0

    sin_term = x
    cos_term = 1.0

    for i in range(1, 12):
        sin_term *= -x * x / ((2 * i) * (2 * i + 1))
        cos_term *= -x * x / ((2 * i - 1) * (2 * i))

        sin_x += sin_term
        cos_x += cos_term

    return side_length * cos_x / sin_x
