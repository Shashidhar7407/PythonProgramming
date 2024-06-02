# Data Structures
# Data Structures allow us to store and organize data efficiently.
# This will allow us to easily access and perform operations on the data.

# In Python, there are four built-in data structures

# List
# Tuple
# Set
# Dictionary

#List
# A list is a collection which is ordered and changeable. In Python lists are written with square
# example of a list os
sample_list = [4,"shashi",567,8.2,"ppshetty"]
print(sample_list)
print(sample_list[2]) # we can also print the list value by using the index values
print(sample_list[1:3]) # we can also print the list value by using the index
print(sample_list[1:]) # we can also print the list value by using the index
print(sample_list[:5])
list_a=[5,"shashi",sample_list]
print(list_a) #we can also print list inside the list
print(len(sample_list))
print(len(list_a))

#iterating over the list values
for i in list_a:
    print(i)

list_c=sample_list+list_a
print(list_c)

color=" shashi,,,, is good,,,, boy"
mewString=color.strip(",")
print(mewString)
new_list=list(color)
print(new_list)

#lsits are mutable and we can update any value in place of other values
sample_list[1]="ppshetty"
print(sample_list)
sample_list[1]="python programming"
print(sample_list)

# we should not that stringd are immutable which means we cannot modify the value of strings in
Name_String="Shashidhar Papishetty"
# Name_String[2]="L"
# print(Name_String) if we run this statement we will get the error because the strings are immutable

# object concept
#------------------------------------------------------------------------------
# object is a real world entity and in python anything or any variable assigned is considered as an object
# whenever an object is declared then it will be intialized with the unique identifier

#Exx:
a=5
print(id(a))
b=a
print(id(b))

#here we can clearly see the id is assigned to variable not to the value'
# so we can say that the variable is an object and the value is an attribute of the object
#we have assigned a to b and checked the id we can see the id didn't change because we are assigned to an existing object


list_a=[1,2,3,4]
list_b=list_a
print(id(list_a))
print(id(list_b))
list_b[3]="shashi"
print(id(list_b))
list_a=["give","me","some","money"]
print(id(list_a))
print(id(list_b))