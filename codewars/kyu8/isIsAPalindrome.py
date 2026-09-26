"""
Problem:
Description:
Write a function that checks if a given string (case insensitive) is a palindrome.

A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards, such as madam or racecar.

Link : https://www.codewars.com/kata/57a1fd2ce298a731b20006a4
"""

# Solution:
def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        left_char = s[left]
        right_char = s[right]

        if 'A' <= left_char <= 'Z':
            left_char = chr(ord(left_char) + 32)

        if 'A' <= right_char <= 'Z':
            right_char = chr(ord(right_char) + 32)

        if left_char != right_char:
            return False

        left += 1
        right -= 1

    return True
