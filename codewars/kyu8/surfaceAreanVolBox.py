"""
Problem:
Description:
Write a function that returns the total surface area and volume of a box.

The given input will be three positive non-zero integers: width, height, and depth.

The output will be language dependant, so please check sample tests for the corresponding data type, (list, tuple, struct, query, etcetera).

Link : https://www.codewars.com/kata/565f5825379664a26b00007c
"""

# Solution:
def get_size(w,h,d):
    surface_area = 2 * (
        (w * h) +
        (w * d) +
        (h * d)
    )

    volume = w * h * d

    return [surface_area, volume]
