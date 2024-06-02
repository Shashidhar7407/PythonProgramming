L = [1, "two", 9, 5.09, "Three", -558, "four", -93.7, "six"]

#Write your code here swapping of an element
# x=int(input())
# y=int(input())
# x=2
# y=6
# new_Value=L[x]
# new_Value2=L[y]
# print(new_Value,new_Value2)
# L[x]=new_Value2
# L[y]=new_Value
# print(L)

x=int(input())
New_List=[]
for i in range(x):
    y=int(input())
    New_List+=[y]
print(New_List[:2]+New_List[x-2:])
