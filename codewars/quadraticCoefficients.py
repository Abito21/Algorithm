"""
Problem:
In this Kata you are expected to find the coefficients of quadratic equation of the given two roots (x1 and x2).

Equation will be the form of ax^2 + bx + c = 0

Return type is a Vector (tuple in Rust, Array in Ruby) containing coefficients of the equations in the order (a, b, c).

Since there are infinitely many solutions to this problem, we fix a = 1.

Remember, the roots can be written like (x-x1) * (x-x2) = 0

Example
quadratic(1,2) = (1, -3, 2)
This means (x-1) * (x-2) = 0; when we do the multiplication this becomes x^2 - 3x + 2 = 0

Example 2
quadratic(0,1) = (1, -1, 0)
This means (x-0) * (x-1) = 0; when we do the multiplication this becomes x^2 - x + 0 = 0

Notes
Inputs will be integers.
When x1 == x2, this means the root has the multiplicity of two

Link : https://www.codewars.com/kata/5d59576768ba810001f1f8d6
"""

# Solution:
def quadratic(x1, x2):
  return (1, -(x1+x2), x1*x2)


"""
Step by step
(x−x1​)(x−x2​)
= x^2 - x2​x - x1​x + x1*​x2
= (x^2) - (x2​x+x1​x) + (x1*​x2)​
= (x^2) − (x1​+x2​)x + (x1*​x2) => sebagai acuan logic​
Compare dengan, harusnya sesuai
ax2+bx+c=0

Jadi
a = 1​
b = -(x1+x2)
c = x1*x2
"""
