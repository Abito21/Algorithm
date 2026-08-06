"""
Problem:
Description:
Given a string of arbitrary length with any ascii characters. Write a function to determine whether the string contains the whole word "English".

The order of characters is important -- a string "abcEnglishdef" is correct but "abcnEglishsef" is not correct.

Upper or lower case letter does not matter -- "eNglisH" is also correct.

Return value as boolean values, true for the string to contains "English", false for it does not.

Link : https://www.codewars.com/kata/58dbdccee5ee8fa2f9000058
"""

# Solution:
def sp_eng(sentence):
    target = 'english'
    target_len = len(target)
    sentence_len = len(sentence)
    
    if sentence_len < target_len:
        return False
    
    for i in range(sentence_len - target_len + 1):
        match_found = True
        
        for j in range(target_len):
            char_sentence = sentence[i + j]
            char_target = target[j]
            
            if 'A' <= char_sentence <= 'Z':
                char_sentence_lower = chr(ord(char_sentence) + 32)
            else:
                char_sentence_lower = char_sentence
            
            if char_sentence_lower != char_target:
                match_found = False
                break
        
        if match_found:
            return True
    return False
