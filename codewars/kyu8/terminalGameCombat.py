"""
Problem:
Description:
Create a combat function that takes the player's current health and the amount of damage received, and returns the player's new health. Health can't be less than 0.

Link : https://www.codewars.com/kata/586c1cf4b98de0399300001d
"""

# Solution:
def combat(health, damage):
    return 0 if health - damage < 0 else health - damage
