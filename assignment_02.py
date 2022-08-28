# Q1) Write a python script to add comments and print “Learning Python” on screen

# ----  This is single line comment ---- 
"""
This is multiline comment

"""




print("Learning Python")

# Q2) Write a python script to add multi line comments and print values of four variables,each in a new line. Variable contains any values
"""
This is a multiline comment
"""
a,b,c,d= 4,5,7,2
print( a, "\n" , b , "\n", c , "\n", d)

# Q3) Write a python script to print types of variables. Create 5 variables each of them containing different types of data. (like 35, True, “MySirG”,5.46, 3+4j, etc)
a,b,c,d,e= 35, True, "MySirG", 5.46, 3+4j
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# Q4) Write a python script to print the id of two variables containing the same integer values
a,b = 4,4
print(id(a))
print(id(a))

# Q5) Create four variables in a Python script and assign values of different data types to them. Write a Python script to print value, its type and id of each variable
a,b,c,d= "akash", 7, 7.66, False
# printing values
print(a,b,c, d)

# printing types of variables
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# printing id of variables
print(id(a))
print(id(b))
print(id(c))
print(id(d))


# Q6) Write a python script to print all the keywords
import keyword
print(keyword.kwlist)

# Q7) On Python shell use help() function and display the list of keywords
"""
False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not
"""

# Q8) Create two Python files A0.py and A1.py. Create a variable in A1.py and assign some value to it. Write a python script to import A1 module in A0 and print value of the variable created in A0.py
import A1
print(A1.x)

# Q9) Name the keywords, used as data in the Python script.
# ----> python keywords used as data:  True , False 

# Q10)  Write a python script to display the current date and time. First create variables to store date and time, then display date and time in proper format (like: 13-8-2022 and 9:00 PM)
import datetime   
dt = datetime.datetime.now()  
print( "Display the current date of the system: ") 
print (str (dt) ) 