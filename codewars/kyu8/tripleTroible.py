"""
Problem:
Description:
Triple Trouble
Create a function that will return a string that combines all of the letters of the three inputed strings in groups. Taking the first letter of all of the inputs and grouping them next to each other. Do this for every letter, see example below!

E.g. Input: "aa", "bb" , "cc" => Output: "abcabc"

Note: You can expect all of the inputs to be the same length.

Link : https://www.codewars.com/kata/5704aea738428f4d30000914
"""

# Solution:
def triple_trouble(one, two, three):
    new_word = ""
    
    for i in range(0, len(one)):
        new_word += one[i]
        new_word += two[i]
        new_word += three[i]
    
    return new_word
