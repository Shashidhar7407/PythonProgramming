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