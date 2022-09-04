#1. Write a python script to add comments and print “Learning Python” on screen

print("\"Learning Python\"")

#2. Write a python script to add multi line comments and print values of four variables,
#   each in a new line. Variable contains any values.

"""
first line for name
second line for age
third line for mobile number
forth line for roll number
"""
name=input("Please enter your name -")
age=int(input("Please enter your age -"))
mob=int(input("Please enter your mobile-number -"))
roll=int(input("Please enter your roll-number -"))
print("Your name is-",name,"\n","Your age is-",age,"\n","Your mobile-number is-",mob,"\n","Your roll-number is-",roll)

#3. Write a python script to print types of variables. Create 5 variables each of them
#   containing different types of data. (like 35, True, “MySirG”,5.46, 3+4j, etc)

a=35
print(type(a))
b=True
print(type(b))
a="MySirG"
print(type(a))
c=5.46
print(type(c))
a=3+4j
print(type(a))

#4. Write a python script to print the id of two variables containing the same integer
#   values.

a=4
print(id(a))
b=4
print(id(b))

#5. Create four variables in a Python script and assign values of different data types to
#   them. Write a Python script to print value, its type and id of each variable

a=4
print(a)
print(type(a))
print(id(a))
b=4.67
print(b)
print(type(b))
print(id(b))
c="shahzad"
print(c)
print(type(c))
print(id(c))
d=4+4j
print(d)
print(type(d))
print(id(d))

#6. Write a python script to print all the keywords

import keyword
print(keyword.kwlist)

#7. On Python shell use help() function and display the list of keywords

help()
'keyword'

#10. Write a python script to display the current date and time. First create variables to
#    store date and time, then display date and time in proper format (like: 13-8-2022 and
#    9:00 PM)

from datetime import datetime
now=datetime.now()
date=now.strftime("%d-%m-%Y and %H-%M")
print(date)
