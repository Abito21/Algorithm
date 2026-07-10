"""
Problem:
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:
-231 <= x <= 231 - 1

Follow up: Could you solve it without converting the integer to a string?

Link : https://leetcode.com/problems/palindrome-number/description/
"""

# Solution:
class Solution:
    def isPalindrome(self, x: int) -> bool:
      if x < 0:
        return False
      
      original = x
      reverse = 0
      
      while x > 0:
        digit = x % 10
        reverse = reverse * 10 + digit
        x //= 10
        
      return original == reverse

"""
Another Solution

Solution 2 : Change into string
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]

Solution 3 : Change into string with manual step
class Solution:
    def isPalindrome(self, x: int) -> bool:
        left = 0
        right = len(x) - 1

        while left < right:
            if x[left] != x[right]:
                return False
            left += 1
            right -= 1
            
        return True

Solution 4 : From Leetcode
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0

        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        return x == reversed_half or x == reversed_half // 10
"""
