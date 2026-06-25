"""
Problem:
Give you a number array numbers and a number c.

Find out a pair of numbers(we called them number a and number b) from the array numbers, let a*b=c, result format is an array [a,b]

The array numbers is a sorted array, value range: -100...100

The result will be the first pair of numbers, for example,findAB([1,2,3,4,5,6],6) should return [1,6], instead of [2,3]

Please see more example in testcases.

Link : https://www.codewars.com/kata/5714803d2817ffce17000a35
"""

# Solution:
def find_a_b(numbers, c):
    for a in numbers:
        if a == 0:
            if c == 0:
                for b in numbers:
                    if b == 0 and numbers.count(0) < 2:
                        continue
                    return [a, b]
            continue

        if c % a == 0:
            b = c // a

            if b in numbers:
                if a == b and numbers.count(a) < 2:
                    continue

                return [a, b]

    return None

"""
Test Case:
import codewars_test as test
from solution import find_a_b

@test.describe("Basic tests")
def basic():
    @test.it("Basic test cases")
    def f():
        test.assert_equals(find_a_b([1,2,3],3), [1,3])
        test.assert_equals(find_a_b([1,2,3],6), [2,3])
        test.assert_equals(find_a_b([1,2,3],7), None)
        test.assert_equals(find_a_b([1,2,3,6],6), [1,6])
        test.assert_equals(find_a_b([1,2,3,4,5,6],15), [3,5])
        test.assert_equals(find_a_b([0,0,2],4), None)
        test.assert_equals(find_a_b([0,0,2,2],4), [2,2])
        test.assert_equals(find_a_b([-3,-2,-2,-1,0,1,2,3,4],4), [-2,-2])
        test.assert_equals(find_a_b([-3,-2,-2,-1,0,1,2,3,4],0), [-3,0])
        test.assert_equals(find_a_b([-3,-2,-1,0,1,2,3,4],4), [1,4])
        test.assert_equals(find_a_b([0,1,2,3],0), [0,1])
        test.assert_equals(find_a_b([0,0,2,3],0), [0,0])
"""
