"""
Problem:
Description:
The code provided is supposed replace all the dots . in the specified String str with dashes -

But it's not working properly.

Task
Fix the bug so we can all go home early.

Notes
String str will never be null.

Link : https://www.codewars.com/kata/596c6eb85b0f515834000049
"""

# Solution:
import re
def replace_dots(s):
#     return re.sub(r"\.", "-", s)
    results = ""
    
    for char in s:
        if char == ".":
            results += "-"
        else:
            results += char
    
    return results
