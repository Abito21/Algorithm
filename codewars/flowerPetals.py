"""
Problem:
Description:
Who remembers back to their time in the schoolyard, when girls would take a flower and tear its petals, saying each of the following phrases each time a petal was torn:

"I love you"
"a little"
"a lot"
"passionately"
"madly"
"not at all"
If there are more than 6 petals, you start over with "I love you" for 7 petals, "a little" for 8 petals and so on.

When the last petal was torn there were cries of excitement, dreams, surging thoughts and emotions.

Your goal in this kata is to determine which phrase the girls would say at the last petal for a flower of a given number of petals. The number of petals is always greater than 0.

Link : https://www.codewars.com/kata/57f24e6a18e9fad8eb000296
"""

# Solution:
def how_much_i_love_you(nb_petals):
    phrases = [
        "I love you",
        "a little",
        "a lot",
        "passionately",
        "madly",
        "not at all"
    ]
    
    remainder = nb_petals
    
    while remainder > 6:
        remainder = remainder - 6
        
    if remainder == 1:
        return phrases[0]
    elif remainder == 2:
        return phrases[1]
    elif remainder == 3:
        return phrases[2]
    elif remainder == 4:
        return phrases[3]
    elif remainder == 5:
        return phrases[4]
    else:
        return phrases[5]
