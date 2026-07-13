"""
Problem:
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

Link : https://www.codewars.com/kata/545cedaa9943f7fe7b000048/python
"""

# Solution:
import string

def is_pangram(st):
    letters = set()
    for ch in st.lower():
      if ch.isalpha():
        letters.add(ch)

    return len(letters) == 26

"""
# Solution 2 (hardcode alphabet):
def is_pangram(st):
  st = st.lower()
  for char in 'abcdefghijklmnopqrstuvwxyz':
    if char not in st:
      return False
  return True

# Solution 3 (Alphabet ASCII):
import string
def is_pangram(st):
  alphabet = set(string.ascii_lowercase)
  return alphabet.issubset(set(st.lower()))
"""
