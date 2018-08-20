#Question -1(   Reverse)
list1=[1,2,3,4,5,6,7]
print(list1[::-1])


#Questions-2 (To uppercase)
a=input("Enter a string :")
b=list(a)
l=len(a)
for i in range(0,1):
    if a[i].isupper():
        print(a[i])


#Question-3(Split)
a = input("Enter a string :")
a = list(map(int, a))
print(a)


#Question -4(Pallindrome)
a=input("Enter a string")
b=a[::-1]
b="".join(b)
if a==b:
    print("Is palindrome")
    else:
        print("Not a palindrome")


#Question-5(
import copy as cop
a=[1,2,3,[9,10],4,5]
b=cop.deepcopy(a)
a[3][0]='yes'
print(a)
print(b)


#Shallow copy =a reference of object is copied in other object(any changes made to a copy of object do reflect in the original object.)
#Deep copy = it creates a new compound object and then, recursively, inserts copies into it.
