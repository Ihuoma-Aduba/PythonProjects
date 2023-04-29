#In python we need to write down a certain line of code in order to give access to all math function

from math import*

print(10 + 10)

print(10 + 10 * 3)

print((10 + 10) * 3)

print(((10 + 10) * 3)/2)

print(((10 + 10) * 3)//2)

print((((10 + 10) * 3)/2)-5)

print("200 + 20")

#print("200" + 20)

age = 19
print("My age is 19")

#print("My age is" + age)

age = "19"
print("My age is " + age)

#But if we wish to work with the variable later on as a number and not a string then we will not add the "". We will
#do this instead

age = 19
print("My age is " + str(age))

age = 19 + 10
print("My age is " + str(age))
