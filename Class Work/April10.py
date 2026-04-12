############################################################################################
# DSA - Data Structure & Algorithm
############################################################################################

# Complexity : There are 2 types of it.
        # --> SPACE COMPLEXITY  -- Space executed in memory
        # --> TIME COMPLEXITY   -- Time executed in code

#       BEST                  AVERAGE                     WORST
#    --------------------------------------------------------------------
#      Alpha                   Omega                 Big Notation "o"  

# Time Complexity :-
""" if we run loop 1st time - Its called o(1) like... (1, 10): - o(1)
    if we run loop 2nd time - Its called o(2) like... (11, 20): - o(2)
    if we run loop 4th time - Its called o(4) like... (31, 40): - o(4)

Same way if our n variable is user defined so our loop run 1 ... n
    like... (1....n) -- Its called o(n)
    like... (2....n) -- Its called o(n)2
    like... (3....n) -- Its called o(n)3

If our loop run more then o(n)3 time so its 'WORST' 
"""

# Space Complexity :-
""" a = 10          ------  o(1)
    b = 20          ------  o(2)

    add = a+b       ------  o(n)    - We use another variable - its required more space.
                                    - Here we directly print it also.

"""

###############################################################################################
""" Exampel - 1 : WAP to reverse my list.(Without using inbuilt methord)"""

l = [12,23,36,42,21]

for i in range(0, len(l)):
    for j in range (i+1, len(l)):
        l[j],l[i] = l[i],l[j]
print(l)

# Another Way :

l = [12,23,36,42,21]

left = 0
right = len(l)-1

while (left < right):
    l[right],l[left] = l[left],l[right]
    left += 1
    right -= 1

print(l)


###############################################################################################
# WAP if our list is palindrom or not.(only use one variable) - DO YOUR SELF
# l = [10,20,30,20,10]
# left = 0
# right = len(l)-1
# rev = l

# while (left < right):
#     l[right],l[left] = l[left],l[right]
#     left += 1
#     right -=1

# if rev == l:
#     print("Its palindrom : ",l)
# else:
#     print("Its not palindrom : ",l)

""" Direct Way """

# l = [10,20,30,20,10]
# left = 0
# right = len(l)-1
# ans = "yes"

# while (left < right):
#     if l[left]==l[right]:
#         left += 1
#         right -= 1
#         continue
#         ans = "No"
#         break
# print(ans)

###############################################################################################




