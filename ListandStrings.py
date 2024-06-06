#split operations
name="  Shashi dhar papishetty  "
print(name.split())

# we can also split any string at specific character
name2="S,h,a,s,hi,i"
print(name2.split(","))

# we can also split based a charcter occurs
a="Shashidhar Papishetty"
print(a.split("a"))

# we can also print the same by using the join operator
new_list=a.split("a")
print(new_list)
new_list="a".join(new_list)
print(new_list)

# we must make sure that sequene should not contin any non string values
'''list_a = list(range(4))
string_a = ",".join(list_a)
print(string_a)'''


# Negative indexing
# we can also access the string by using negative indexing
list_a=[1,2,3,4,5]
print(list_a[::-1])

# we can also access the items from the reverese by providing the negative index

list_a=[1,2,3,4,5,6]
print(list_a[-2])
print(list_a[-3])


#slicing with negative index

print(list_a[-5:-1])


#negative step index [start index should be greater than end index and range value shoudl be in negative]

print(list_a[4:1:-1])
print(list_a[2:4:-1]) #rrturns empty 

name="Shashidhar Papishetty"
name=name.upper()
print(name[::-1])
