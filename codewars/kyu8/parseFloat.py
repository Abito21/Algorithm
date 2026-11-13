"""
Problem:
Description:
Write function parse_float which takes a string/list and returns a number or 'none' if conversion is not possible.

Link : https://www.codewars.com/kata/57a386117cb1f31890000039
"""

# Solution:
def parse_float(string):
    try:
        return float(string)
    except (ValueError, TypeError):
        return None
