""" Questation : 3 --> 
WAP to count the occurrences of each word in a given sentence.
"""
# sentence = "hello python hello world"
sentence = input("Enter a sentence: ")      # Take input from user

words = sentence.split()                    # Convet sentence into list. Breaks it in word.
list = []                                   # Create empty list 
                                            
for i in range(len(words)):                 # Loop run through each word by its index
    if words[i] not in list:                # Check word if its peinted or not.
        count = 0                           # Start counting from 0.
        
        for j in range(len(words)):         # Second loop run to compare each words.
            if words[i] == words[j]:        # if 'i' and 'j' are same increase count.
                count += 1                  # Increase count by 1
        
        print(words[i], ":", count)         # Print word & how many time its count
        list.append(words[i])               # add word to list.