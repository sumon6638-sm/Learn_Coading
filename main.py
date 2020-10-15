print("Hello World")
print('\n\n')

#Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.

#Python is used for: 1.web development (server-side),  2.software development,  3.mathematics,  4.system scripting.


#1

'''
#1-Python Identation
if 5 > 2:
  print("Five is greater than two!") 
    #print("Five is greater than two!")
'''

"""
#2-Comment
This is a comment
written in
more than just one line
"""

'''
#3-Variable
x = "Python is "
y = "awesome"
z =  x + y
print("The " + z)

x = 'Md'
y = 'SuMon'
print('My name is ' + x + ' ' + y)
'''

'''
#4-Global_Varial
x = "awesome" #it's a global variable

def myfunc():
  x = "fantastic" #It's a variable as the same name as global variable but it's not a global variable.
  print("Python is " + x)

myfunc()

print("Python is " + x)
'''

'''
#5-Global_Keyword
def myfunc():
  global x
  x = "fantastic" #It's became global variable by using global keyword.

myfunc()

print("Python is " + x) 
'''

'''
#6-Python Data Type
"""
Data Type in python.
1.Text Type:        str
2.Numeric Types: 	int, float, complex
3.Sequence Types: 	list, tuple, range
4.Mapping Type: 	dict
5.Set Types:    	set, frozenset
6.Boolean Type: 	bool
7.Binary Types: 	bytes, bytearray, memoryview
"""

#To get data type.
x = 5.3j
print(type(x))
'''

'''
#7-Python Number
x = 1    # int
y = 2.8  # float
y2= 35e3 # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(y2))
print(type(z))
'''

'''
#8-Type conversion
x = 1    # int
y = 2.8  # float
z = 1j   # complex

print("Before Converting")
print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print("\n\nAfter Converting")
print(a)
print(b)
print(c)

print
print(type(a))
print(type(b))
print(type(c))
'''

'''
#9-Random Number
import random

print(random.randrange(1, 10))
'''

'''
#10-Python Casting
#int()
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

#float()
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

#str()
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
'''

"""
#11-Python String
#Value_assign
a = "Hello"
print(a)
print(a[1]) #String are arrays

#Multiple_String
b = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print("\n\n" + b)

#Slicing
c = "Hello, World!"
print("\n\n" + c[2:5])#(Starting from index (2) to before (5))
print("\n" + c[-5:-2])#Negative Indexing(Starting from index (-5) to before (-2))

#String Length
print("\n\n")
print(len(c))

#String Methods_The strip() method removes any whitespace from the beginning or the end:
d = " Hello, World! "
print(d.strip()) # returns "Hello, World!" and remove whitespace from Begining & Ending.

print(d.lower())
print(d.upper())
print(d.replace("H", "J"))
print(d.split(",")) # returns ['Hello', ' World!'] #The split() method splits the string into substrings if it finds instances of the separator:

#Check String
txt = "The rain in Spain stays mainly in the plain"

x = "ain" in txt
print("\n\n")
print(x) #True

y = "ain" not in txt
print(y) #False

#String Concatenation
a = "Hello"
b = "World"
print(a + " " + b + "!")
c = a + " " + b
print(c)
print("\n\n")

#String Format_As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
print("\n\n")

age = 23
name = "SuMon"
txt = "My name is {}, I am {}"
print(txt.format(name, age))

txt2 = "My name is {1}, I am {0}"
print(txt2.format(age, name))
print('\n\n')

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
print("\n\n")

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
print("\n\n")

txt = "We are the so-called \"Vikings\" from the north."
print(txt)
print("\n")

txt1 = 'We are the so-called "Vikings" from the north.'
print(txt1)
print("\n\n")
"""

'''
#12-Python Booleans_Booleans represent one of two values: True or False.
print("Booleans represent one of two values: True or False.")

print(10 > 9)
print(10 == 9)
print(10 < 9)
print("----------------1\n\n")

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
print("----------------2\n\n")

#Evaluate Values_The bool() function allows you to evaluate any value, and give you True or False in return,
print(bool("Hello"))
print(bool(15))
print("----------------3")

#Evaluate Variables
x = "Hello"
y = 15

print(bool(x))
print(bool(y))
print("----------------4")

#Which value is true or false
m = """Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones."""
print(m)
print("\n\n")

n = """In fact, there are not many values that evaluates to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False."""
print(n)
print("\n\n")

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
print("\n\n")

print("The following will return False:")
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
print("\n\n")
print("----------------5\n\n")

o = """One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:"""
print(o)
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
print("----------------6")
print("\n\n")

#Functions can Return a Boolean
def myFunction() :
  return True

print(myFunction())
print("_________7\n\n")

#Question: Print "YES!" if the function returns True, otherwise print "NO!":
def myFunction() :
  return False

if myFunction():
  print("YES!")
else:
  print("NO!")

#Python also has many built-in functions that returns a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:

p = 200
print(isinstance(p, int))
print(isinstance(p, float))
'''

'''
#13-Python Operator
x = 5
y = 2
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)   #1_____Residue Part
print(x ** y)  #25____x to the power y
print(x // y)  #2_____How many time it can be devided.

#For more details: https://www.w3schools.com/python/python_operators.asp
'''

'''
#14-Python List
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist)

print("\n\nAccess Items:")
print(thislist[1])

print("\n\nNegative Indexing:")
print(thislist[-1])

print("\n\nRange of Indexes:")
print(thislist[2:5])
print(thislist[:4]) #index 0 to before 4
print(thislist[2:]) #index 2 to last

print("\n\nRange of Negative Indexes:")
print(thislist[-4:-1])

print("\n\nChange Item Value:")
thislist[1] = "blackcurrant"
print(thislist)

print("\n\nLoop through a list:")
for x in thislist:
  print(x)

print("\n\nCheck if Item Exists:")
if "appl" in thislist:
  print("Yes, 'apple' is in the fruits list")
else:
    print("No, It is not in this list")

"""
a = input("Enter your Item : ")
if a in thislist:
  print("Yes " + a + " is in thislist")
else:
  print("No " + a + " is not in thislist")
"""

print("\n\nList Length:")
print(len(thislist))

print("\n\nAdd Items:")
thislist.append("strawberry")
print(thislist)

print("\n\nAdd Items in Specific Index:")
thislist.insert(1, "strawberry")
print(thislist)

print("\n\nRemove Items:")
thislist.remove("kiwi")
print(thislist)

print("\n\npop Method:")
#The pop() method removes the specified index, (or the last item if index is not specified):
thislist.pop()
print(thislist)

print("\n\ndel keyword remove a specific index:")
del thislist[0]
print(thislist)

print("\n\nMethod of Copy a List:")
mylist = thislist.copy()
print(mylist)
mylist1 = list(thislist)
print(mylist1)

print("\n\nclear method empty the list")
thislist.clear()
print(thislist)

print("\n\nJoin Two Lists:")
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

print("\n\nAppend list2 into list1:")
for x in list2:
  list1.append(x)

print(list1)

print("\n\nUse the extend() method to add list2 at the end of list1:")
list1.extend(list2)
print(list1)

print("\n\nThe list() Constructor:")
thislist1 = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist1)
'''

'''
#15-Python Tuples
#Same as list, But tuples are written with round brackets.

print("Method of Indexes: ")
thistuple = ("apple", "banana", "cherry")
print(thistuple)

print(thistuple[1])

print(thistuple[-1])

print(thistuple[2:5])

print(thistuple[-4:-1])

print("\n\nChange Tuple Values: ")
x = ("apple", "banana", "cherry")
print(x)
y = list(x)
print(y)
y[1] = "kiwi"
x = tuple(y)

print(x)

print("\n\nLoop Through a Tuple: ")
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

print("\n\nCheck if Item Exists: ")
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

print("\n\nTuple Length: ")
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

"""
print("Add Item is not support in tuple: ")
thistuple[3] = "orange" # This will raise an error
print(thistuple)
"""

print("\n\nCreate Tuple With One Item: ")
thistuple1 = ("apple",) #use comma after value is necessary.
print(type(thistuple1))
tl1 = list(thistuple1)
print(tl1)

#NOT a tuple
thistuple2 = ("apple")
print(type(thistuple2))
tl2 = list(thistuple2)
print(tl2)
print("Because it was a string")

"""
print("\n\nRemove Items: ")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists
"""

print("\n\nJoin Two Tuples: ")
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

print("\n\nThe tuple() Constructor: ")
#It is also possible to use the tuple() constructor to make a tuple.
# Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
'''


#16-Python Sets
#Sets are unordered.
#A set is a collection which is unordered and unindexed.
#In Python sets are written with curly brackets.

thisset = {"apple", "banana", "cherry"}
print(thisset)

print("\n\nAccess Item: ")
for x in thisset:
  print(x)

print('\n\nCheck if "banana" is present in the set:')
print("banana" in thisset)

print("\n\nChange Items: ")
print("Once a set is created, you cannot change its items, but you can add new items.")

print("\n\nAdd Items: ")
print("Add an item to a set, using the add() method:")
thisset.add("orange") #It will be assign in any index of the set. Index will change again and again when we print.
print(thisset)

print("\nAdd multiple items to a set, using the update() method: ")
thisset.update(["pineapple", "mango", "grapes"]) #It will be assign in any index of the set. Index will change again and again when we print.
print(thisset)

print("\n\nGet the Length of a Set: ")
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

print("\n\nRemove Item: ")
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
print("If the item to remove does not exist, remove() will raise an error.")

print("\nRemove Item by using discard: ")
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
print("If the item to remove does not exist, discard() will NOT raise an error.")

print("\nRemove the last item by using the pop() method: ")
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
#Sets are unordered, so when using the pop() method, you will not know which item that gets removed.

print("\nThe clear() method empties the set: ")
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

"""
print("\nThe del keyword will delete the set completely: ")
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)
"""

print("\n\nJoin Two Sets: ")
print("You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:" )

print("\nThe union() method returns a new set with all items from both sets: ")
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

print("\nThe update() method inserts the items in set2 into set1: ")
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
print("Both union() and update() will exclude any duplicate items.")

print("\n\nThe set() Constructor: ")
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)


'''
#17-Python Dictionaries
print("A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.")

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

print("\n\nAccessing Items: ")
x = thisdict["model"]
x = thisdict.get("model")

print("\n\nChange Values: ")
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2020
print(thisdict)

print("\n\nLoop Through a Dictionary: ")
for x in thisdict:
  print(x)
  print(thisdict[x])

print("\n\nAnother format: ")
for x in thisdict:
  print(x + " " + str(thisdict[(x)]))

print("\n\nYou can also use the values() method to return values of a dictionary:")
for x in thisdict.values():
  print(x)

print("\n\nLoop through both keys and values, by using the items() method:")
for x, y in thisdict.items():
  print(x, y)

print("\n\nCheck if Key Exists: ")
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

print("\n\nDictionary Length: ")
print(len(thisdict))

print("\n\nAdding Items: ")
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

print("\n\nRemoving Items: ")

#The pop() method removes the item with the specified key name:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#The del keyword removes the item with the specified key name:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

#The del keyword can also delete the dictionary completely:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
#print(thisdict) #this will cause an error because "thisdict" no longer exists.

#The clear() method empties the dictionary:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

print("\n\nCopy a Dictionary: ")
#Make a copy of a dictionary with the copy() method:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#Another way to make a copy is to use the built-in function dict().
#Make a copy of a dictionary with the dict() function:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

print("\n\nNested Dictionaries: ")
print("A dictionary can also contain many dictionaries, this is called nested dictionaries.")
print("Create a dictionary that contain three dictionaries:")
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print("\nAnother Way: ")
print("Create three dictionaries, then create one dictionary that will contain the other three dictionaries:")
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print("\n\nThe dict() Constructor: ")
thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)
'''

'''
#18-Python If ... Else
print("Python supports the usual logical conditions from mathematics: ")
print("Equals: a == b\nNot Equals: a != b\nLess than: a < b\nLess than or equal to: a <= b\nGreater than: a > b\nGreater than or equal to: a >= b")

print("\n\nIf_elif statement: ")
a = 33
b = 200
if b > a:
  print("b is greater than a")
elif a == b:  #The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
  print("a and b are equal")

print("\n\nElse Statement: ")
print("The else keyword catches anything which isn't caught by the preceding conditions.")
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

print("\n\nShort Hand If: ")
print("If you have only one statement to execute, you can put it on the same line as the if statement.")
print("\nOne line if statement:")
if a > b: print("a is greater than b")

print("\n\nShort Hand If ... Else: ")
print("If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:")
print("\nOne line if else statement: ")
a = 2
b = 330
print("A") if a > b else print("B")

print("\nOne line if else statement, with 3 conditions: ")
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

print("\n\nAnd: ")
print("Test if a is greater than b, AND if c is greater than a:")
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

print("\n\nOr: ")
print("Test if a is greater than b, OR if a is greater than c:")
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

print("\n\nNested If: ")
print("You can have if statements inside if statements, this is called nested if statements.")
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

print("\n\nThe pass Statement: ")
a = 33
b = 200

if b > a:
  pass
#pass statement to avoid getting an error.
'''

'''
#19-Python While Loops
"""Python Loops
Python has two primitive loop commands:
   while loops
   for loops"""

print("The while Loop: ")
print("With the while loop we can execute a set of statements as long as a condition is true.")

i = 1
while i < 6:
  print(i)
  i += 1

print("\n\nThe break Statement: ")
print("With the break statement we can stop the loop even if the while condition is true: ")
print("Exit the loop when i is 3: ")
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

print("\n\nThe continue Statement: ")
print("With the continue statement we can stop the current iteration, and continue with the next: ")
print("Continue to the next iteration if i is 3: ")
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

print("\n\nThe else Statement: ")
print("With the else statement we can run a block of code once when the condition no longer is true: ")
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
'''

'''
#20-Python For Loops
print("Print each fruit in a fruit list: ")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

print("\nLooping Through a String: ")
for x in "banana":
  print(x)

print("\nThe break Statement: ")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

print("Another way: ")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

print("\nThe continue Statement: ")
print("Do not print banana: ")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

print("\nThe range() Function")
for x in range(6):
  print(x)

print("Using the start parameter: ")
for x in range(2, 6):
  print(x)

print("Increment the sequence with 3 (default is 1): ")
for x in range(2, 30, 3):
  print(x)

print("\nElse in For Loop: ")
print("Print all numbers from 0 to 5, and print a message when the loop has ended: ")
for x in range(6):
  print(x)
else:
  print("Finally finished!")

print("\nNested Loops: ")
print("A nested loop is a loop inside a loop.")
print("Print each adjective for every fruit: ")
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

print("\nThe pass Statement: ")
for x in [0, 1, 2]:
  pass
'''

'''
#21-Python Functions
"""A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result."""

print("Creating a Function: ")
print("In Python a function is defined using the def keyword: ")
def my_function():
  print("Hello from a function")


print("\nCalling a Function: ")
print("To call a function, use the function name followed by parenthesis: ")
def my_function1():
  print("Hello from a function")

my_function1()


print("\nArguments: ")
print("Information can be passed into functions as arguments.")
def my_function2(fname):
  print(fname + " Refsnes")

my_function2("Emil")
my_function2("Tobias")
my_function2("Linus")

print("\nParameters or Arguments?")
print("The terms parameter and argument can be used for the same thing: information that are passed into a function.")

"""
From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called.
"""

print("\nNumber of Arguments: ")
#By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.
print("This function expects 2 arguments, and gets 2 arguments: ")

def my_function3(fname, lname):
  print(fname + " " + lname)

my_function3("Emil", "Refsnes")

#If you try to call the function with 1 or 3 arguments, you will get an error:

"""
print("This function expects 2 arguments, but gets only 1: ")
def my_function4(fname, lname):
  print(fname + " " + lname)

my_function4("Emil") #Error
"""

print("\nArbitrary Arguments, *args: ")
"""If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly: """
print("If the number of arguments is unknown, add a * before the parameter name: ")
def my_function4(*kids):
  print("The youngest child is " + kids[2])

my_function4("Emil", "Tobias", "Linus")

print("\nKeyword Arguments: ")
"""You can also send arguments with the key = value syntax.

This way the order of the arguments does not matter."""
def my_function5(child3, child2, child1):
  print("The youngest child is " + child3)

my_function5(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

print("\nArbitrary Keyword Arguments, **kwargs: ")
"""If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly: """
print("If the number of keyword arguments is unknown, add a double ** before the parameter name: ")
def my_function6(**kid):
  print("His last name is " + kid["lname"])

my_function6(fname = "Tobias", lname = "Refsnes")

print("\nDefault Parameter Value: ")
print("If we call the function without argument, it uses the default value: ")
def my_function7(country = "Norway"):
  print("I am from " + country)

my_function7("Sweden")
my_function7("India")
my_function7()
my_function7("Brazil")

print("\nPassing a List as an Argument: ")
def my_function8(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]
my_function8(fruits)

print("\nReturn Values: ")
print("To let a function return a value, use the return statement: ")
def my_function9(x):
  return 5 * x

print(my_function9(3))
print(my_function9(5))
print(my_function9(9))

print("\nThe pass Statement: ")
def myfunction():
  pass

print('\nRecursion: ')
print("Python also accepts function recursion, which means a defined function can call itself.")
"""Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it."""
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
'''

'''
#22-Python Lambda
print("A lambda function is a small anonymous function.")
print("A lambda function can take any number of arguments, but can only have one expression.")

print("\nSyntax: ")
print("lambda arguments : expression")
print("The expression is executed and the result is returned: ")

print('\nA lambda function that adds 10 to the number passed in as an argument, and print the result: ')
x = lambda a : a + 10
print(x(5))

print("Lambda functions can take any number of arguments: ")
print('A lambda function that multiplies argument a with argument b and print the result: ')
x = lambda a, b : a * b
print(x(5, 6))

print('A lambda function that sums argument a, b, and c and print the result: ')
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

print('\nWhy Use Lambda Functions?')
print('The power of lambda is better shown when you use them as an anonymous function inside another function.')

print('Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number: ')
def myfunc(n):
  return lambda a : a * n

print('Use that function definition to make a function that always doubles the number you send in: ')
def myfunc2(n):
  return lambda a : a * n

mydoubler = myfunc2(2)

print(mydoubler(11))

print('Or, use the same function definition to make a function that always triples the number you send in: ')
def myfunc3(n):
  return lambda a : a * n

mytripler = myfunc3(3)

print(mytripler(11))

print('Or, use the same function definition to make both functions, in the same program: ')
def myfunc4(n):
  return lambda a : a * n

mydoubler = myfunc4(2)
mytripler = myfunc4(3)

print(mydoubler(11))
print(mytripler(11))

print('Use lambda functions when an anonymous function is required for a short period of time.')
'''

'''
#23-Python Arrays

cars = ["Ford", "Volvo", "BMW"]

car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"

print('\n\nAccess the Elements of an Array: ')
x = cars[0]
print(x)

print('\n\nChange Element: ')
cars[0] = "Toyota"
print(cars)

print('\n\nThe Length of an Array: ')
x = len(cars)
print(x)

print('\n\nLooping Array Elements: ')
print('Print each item in the cars array:')
for x in cars:
  print(x)

print('\n\nAdding Array Elements: ')
cars.append("Honda")
print(cars)

print('\n\nRemoving Array Elements: ')
cars.pop(1)
print(cars)

cars.remove("Volvo")
print(cars)
'''

'''
#24-Python Classes and Objects
print('Python Classes/Objects: ')
"""Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects."""

print('Create a Class: ')
print('Create a class named MyClass, with a property named x:')
class MyClass:
  x = 5
print(MyClass)

print('\n\nCreate Object: ')
print('Create an object named p1, and print the value of x: ')
p1 = MyClass()
print(p1.x)

print('\n\nThe __init__() Function: ')
"""The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

To understand the meaning of classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:"""
print('Create a class named Person, use the __init__() function to assign values for name and age:')
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
print('Note: The __init__() function is called automatically every time the class is being used to create a new object.')

print('\n\nObject Methods: ')
print('Objects can also contain methods. Methods in objects are functions that belong to the object.')
print("Insert a function that prints a greeting, and execute it on the p1 object: ")
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
print('Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.')

print('\n\nThe self Parameter: ')
"""The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class: """
print('Use the words mysillyobject and abc instead of self:')
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc1(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc1()

print('\n\nModify Object Properties: ')
print('You can modify properties on objects like this: ')
print('Set the age of p1 to 40: ')
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc2(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

p1.age = 40
print(p1.age)

print('\n\nDelete Object Properties: ')
#del p1.age
#print(p1.age)

print('\n\nDelete Objects: ')
#del p1
#print(p1)

print('\n\nThe pass Statement: ')
class Person:
  pass
'''

'''
#25-Python Inheritance
print('Python Inheritance')
print('Inheritance allows us to define a class that inherits all the methods and properties from another class.')
print('Parent class is the class being inherited from, also called base class.\nChild class is the class that inherits from another class, also called derived class.')

print('\n\nCreate a Parent Class: ')
print('Any class can be a parent class, so the syntax is the same as creating any other class: ')
print('Create a class named Person, with firstname and lastname properties, and a printname method:')
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

print('\n\nCreate a Child Class: ')
"""To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class: """

print('Create a class named Student, which will inherit the properties and methods from the Person class:')
class Student(Person):
    pass
print('Note: Use the pass keyword when you do not want to add any other properties or methods to the class.')

print('\nNow the Student class has the same properties and methods as the Person class.')
print('Use the Student class to create an object, and then execute the printname method: ')
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student1(Person):
  pass

x = Student1("Mike", "Olsen")
x.printname()

print('\n\nAdd the __init__() Function')
"""So far we have created a child class that inherits the properties and methods from its parent.

We want to add the __init__() function to the child class (instead of the pass keyword).

Note: The __init__() function is called automatically every time the class is being used to create a new object."""

print("Add the __init__() function to the Student class: ")
class Student2(Person):
  def __init__(self, fname, lname):
    #add properties etc.
'''

