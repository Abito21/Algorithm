"""
Problem:
Description:
Write a function to split a string and convert it into an array of words.

Examples (Input ==> Output):
"Robin Singh" ==> ["Robin", "Singh"]

"I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]

Link : https://www.codewars.com/kata/57e76bc428d6fbc2d500036d
"""

# Solution:
def string_to_array(s):
    if s == "":
        return [""]
    
    result = []
    word = ""

    for char in s:
        if char == " ":
            if word != "":
                result.append(word)
                word = ""
        else:
            word += char

    if word != "":
        result.append(word)

    return result
