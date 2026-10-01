"""
Problem: 
Description:
Classy Classes
This kata is aimed at teaching basics about classes.

Task
Your task is to complete the Person class. It should have a constructor that accepts a person's name as string and a person's age as integer.

It should also have an info / Info (C#) property/getter/accessor/field (depending on your language) which should evaluate to a formatted string like "johns age is 34", using the person's age and name.

Reference: https://docs.python.org/3/tutorial/classes.html

Link : https://www.codewars.com/kata/55a144eff5124e546400005a
"""

# Solution:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def info(self):
        return self.name + "s age is " + str(self.age)
