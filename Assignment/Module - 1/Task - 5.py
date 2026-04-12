# Question - 5
# Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing' then add 'ly' instead If the string length of the 
# given string is less than 3, leave it unchanged

    # Check string length first    
    # Check string ends with 'ing' 
    # Apply Conditions

str = input("Enter any word : ")    # str = go, str = Play, str = Playing

if len(str) < 3:                    # Step 1 : Check length of word
    result = str
elif str.endswith("ing"):           # Step 2 : Check our string endswith 'ing'. If yes then add 'ly'.
    result = str + "ly"
else:                               # Step 3 : as per Step 2 if not so apply else and add 'ing'
    result = str + "ing"
print("Final out-put : ",result)

