""" Question : 6 -->
Write a Python program to find the first appearance of the substring 'not' 
and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 
'not'...'poor' substring with 'good'. Return the resulting string"""

                # Task Rules :
                                # Find first occurrence of "not" and "poor"
                                # If "poor" comes after "not"
                                # Replace the whole "not"... "poor" with "good"


s = input("Enter a sentence: ")
# s = "The student is not that poor in coding"
# s = "The student is poor in java but not bad in python" 

not_index = s.find("not")     # index - 15
poor_index = s.find("poor")   # index - 24
# print(not_index)
# print(poor_index)

if not_index != -1 and poor_index != -1 and poor_index > not_index: 
    result = s[:not_index] + "good" + s[poor_index+4:]
else:
    result = s

print("Result:", result)

""" 
not_index != -1         = "not" is available in string
poor_index != -1        = "poor" is available in string 
poor_index > not_index  = 24 > 15 (not comes befor the poor)
use and                 = its show if our all conditions are true

its replace [ : not_index] with "good: and ends after poor 
[poor_index+4 : ] - its skeep 4 words(poor) + after remain same 
""" 