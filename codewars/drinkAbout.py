"""
Problem:
Kids drink toddy.
Teens drink coke.
Young adults drink beer.
Adults drink whisky.
Write a function that receives age, and returns what they drink.

Rules:

Children under 14 old.
Teens under 18 old.
Young under 21 old.
Adults have 21 or more.
Examples: (Input --> Output)

13 --> "drink toddy"
17 --> "drink coke"
18 --> "drink beer"
20 --> "drink beer"
30 --> "drink whisky"

Link : https://www.codewars.com/kata/56170e844da7c6f647000063
"""

# Solution:

def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    elif age < 18:
        return "drink coke"
    elif age < 21:
        return "drink beer"
    elif age >= 21:
        return "drink whisky"
