""" Questation : 11 --> WAP to unzip a list of tuples into individual lists."""
l = [(100,200), (300,400), (500,600),(700,800)]

list1 = [ ]                     # Create empty list1
list2 = [ ]                     # Create empty list2

for i in l:                     # Run loop in main l(list)
    list1.append(i[0])          # Its append [0,2,4,6] index value in list1
    list2.append(i[1])          # Its append [1,3,5,7] index value in list1

print("1st list : ",list1)      # print list1
print("2nd list : ",list2)      # print list2