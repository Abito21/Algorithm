"""
Problem:
Description:
Complete the solution so that it reverses all of the words within the string passed in.

Words are separated by exactly one space and there are no leading or trailing spaces.

Example(Input --> Output):

"The greatest victory is that which requires no battle" --> "battle no requires which that is victory greatest The"

Link : https://www.codewars.com/kata/51c8991dee245d7ddf00000e
"""

# Solution:
def reverse_words(s):
    arr = []
    newWord = ""

    for i in range(len(s)):
        if s[i] != " ":
            newWord += s[i]
        else:
            arr.append(newWord)
            newWord = ""

    arr.append(newWord)

    result = ""

    for i in range(len(arr) - 1, -1, -1):
        result += arr[i]

        if i != 0:
            result += " "

    return result
