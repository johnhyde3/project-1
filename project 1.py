''' Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:'''

a=(input("enter first value:"))
b=(input("enter second value"))
a=float(a)
b=float(b)
c=(a+b)
d=(a-b)
e=(a*b)
f=(a/b)
print("addition:        ",c)
print("subtraction:     ",d)
print("multiplication:  ",e)
print("division:        ",f)


''' Personalized Greeting
Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.'''

a=(input("enter first name:"))
b=(input("enter last name:"))
a=str(a)
b=str(b)
c=(a + b)
print("hello ",(c),"!Welcome to python program.")
