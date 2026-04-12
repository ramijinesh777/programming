""" Questation : 7 -->
WAP to find Greatest Common Divisor of two numbers. For example, the GCD of 20 and 
28 is 4 and GCD of 98 and 56 is 14.
"""
# a = 20 , b = 28 , GCD = 4
# a1 = 98 , b2 = 56 , GCD = 14

a = int(input("Enter first number : "))     # 20 - 1,2,4,5,10,20
b = int(input("Enter second number : "))    # 28 - 1,2,4,7,14,28 
                                            # Common divisor are : 1 , 2 , 4
                                            # Greatest common dividor : 4


# Find smaller number
if a < b:
    small = a
else:
    small = b

# Now we run loop for backwards (we need largest GCD) 
# If we need smallest GCD so loop run (0, small+1):
for i in range (small, 0, -1):
    if a % i == 0 and b % i == 0: # its check my "a" divides by "i" and got remainder 0. Its checks both a & b.
        print("GCD is : ",i)
        break

