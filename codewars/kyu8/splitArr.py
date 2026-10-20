"""
Problem:
Description:
Create a method partition that accepts a list and a method/block. It should return two arrays: the first, with all the elements for which the given block returned true, and the second for the remaining elements.

Here's a simple Ruby example:

animals = ["cat", "dog", "duck", "cow", "donkey"]
partition(animals){|animal| animal.size == 3}
    #=> [["cat", "dog", "cow"], ["duck", "donkey"]]
The equivalent in Python would be:

animals = ['cat', 'dog', 'duck', 'cow', 'donkey']
partition(animals, lambda x: len(x) == 3)
    # (['cat', 'dog', 'cow'], ['duck', 'donkey'])
If you need help, here's a reference:

https://docs.ruby-lang.org/en/master/Enumerable.html#method-i-partition

Link : https://www.codewars.com/kata/545b342082e55dc9da000051
"""

# Solution:
def partition(arr, classifier_method):
    true_list = []
    false_list = []
    
    for item in arr:
        if classifier_method(item):
            true_list.append(item)
        else:
            false_list.append(item)
    
    return true_list, false_list
