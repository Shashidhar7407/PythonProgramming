print("hello")
#data types in python
# String, Integer, Float,boolean

#defining the variable in python
age=20 #we can define directly by the varible name
#by default the user input will be as string and if we need to consider the input as int then int(input())
# x=int(input()) #helps in converting the code into integer
#spacing is very important in python

a="hello"
b="print"
print(a+" "+b)
print(b  * 10)

# we also know indexing starts from 0
#String sclicing 
message="Hishashi"
print(message[:3])
print(message[3:]) #we can see th [startindex:endindex]
print(message[1:5]) #we can also print the range what we required
print(message[1:5:2])#the above makes the changes in the index alternate value it prints

#Typeconversion
#int to string  
i="5"
print(type(i))
i=int(i)
print(type(i)) #type conversion is done from string to int

#we can conver to int(),float(),str(),bool() we can convert to any of following data type based on the given input type

#relational operators

# >	Is greater than
# <	Is less than
# ==	Is equal to
# <=	Is less than or equal to
# >=	Is greater than or equal to
# !=	Is not equal to

#logical operators
# and
# or
# not


#conditonal statements
# if statement condition:
    #  code
#else:
   # code


# more operators in python
# print(6%2) prints modulo operator
# print( 2**3) it's an exponent oerator
# print( 2//3) it's a floor division operator
print(3//2)
print(2//2)
print(4//2)
print(3/2)
# we can calculate the square root of of any number by x ** 0.5
print(int(16**0.5))

#nested block
if(3==2):
    if(3<2):
        print("hello world")
    print("hello world2")
print("not equal")

#types of loops
i=0;
while(i<10):
    print(int(i))
    i+=1;

# advanced for loop
a="Shashi"
for i in a:
    print(i) # where it can be used for passing the string

a=90
for i in range(50,a):
    print(i) # where it can be used for passing the

#string methods
# String Methods

# isdigit() check whether it is a digit
# strip() removes the empty spaces from the string or Strip(",") removes semicolon from the string u can also stripp multi character strip(",./") removes all character from the string u can also
# lower() converts string to lowercase
# upper() converts the string to uppercase
# startswith() check with starting character
# endswith() checks end with character
# replace() and more... replace(oldcharcter,newcharacter)
a="Shashi"
a=a.replace("Shashi","Manoj")
print(a)

# Classification Methods
# isalpha() checks if all the characters in the string are alphabets
# isdecimal() checks if all the characters in the string are decimal
# islower() checks if all the characters in the string are in lowercase
# isupper() checks if all the characters in the string are in uppercase
# isalnum() checks if all the characters in the string are alphanumeric

# Case Conversion Methods
# capitalize() converts the first character to uppercase and the rest to lowercase
# title() converts the first character of each word to uppercase and the rest to lowercase
# swapcase() swaps the case of the characters in the string
# Counting and Searching Methods
# count() returns the number of occurrences of a substring in the string
# index() returns the index of the first occurrence of a substring in the string
# rindex() returns the index of the last occurrence of a substring in the string
# find() returns the index of the first occurrence of a substring in the string
# rfind() returns the index of the last occurrence of a substring in the string


 