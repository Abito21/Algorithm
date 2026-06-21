"""
Problem:
Complete the solution so that it splits the string into strings of two characters in a list/array (depending on the language you use). If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
"""

# Solution:
def solution(s):
  if len(s) % 2 == 1:
    s += '_'
  arrChar = []
  for char in range(0, len(s), 2):
    arrChar.append(s[char:char+2])
  return arrChar

"""
# Solution Using Recursion:
def solution(s):
  if len(s) == 0:
    return []
  elif len(s):
    return [s + '_']
  else:
    return [s[:2]] + solution(s[2:])
"""
