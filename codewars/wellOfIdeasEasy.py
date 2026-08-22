"""
Problem:
Description:
For every good kata idea there seem to be quite a few bad ones!

In this kata you need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'. If there are one or two good ideas, return 'Publish!', if there are more than 2 return 'I smell a series!'. If there are no good ideas, as is often the case, return 'Fail!'.

Link : https://www.codewars.com/kata/57f222ce69e09c3630000212
"""

# Solution:
def well(x):
    goodIdea = []
    for idea in x:
        if idea == 'good':
            goodIdea.append(idea)
    
    if len(goodIdea) > 2:
        return 'I smell a series!'
    elif len(goodIdea) == 1 or len(goodIdea) == 2:
        return 'Publish!'
    return 'Fail!'
