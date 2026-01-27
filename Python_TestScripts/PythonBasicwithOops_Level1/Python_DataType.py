# define Numeric data types
# int
a = 45
print("Value of a is ", a, type(a))

# float
b = 10.23456789545645656775656756756757567567567
print("Value of b is :", b, type(b)) # Float will only take 15 decimal of places

# Complex
c = 100+45J
print("Value of c is :", c , type(c))

# String
d = "String can be used in double quote"
e = 'String can also be used in single quote'
f = 24
g = 45
h = f + g
print(d , " | ",  e)
#print(f + " | ", e)
print("Value of int {} + {} is: {}".format(f, g, h))

# List
g = [1,2,3,4,5,6] # List has start with 0 index
print(g)
print(g[4]) # it will print only single value.
g.append(8)
print(g)
g.remove(8)
print(g)
g[5]=88
print(g)

h = ["Goat","Sheep","Cow","Lion","Tiger", "Tiger", 24, 56]
print(h)
print(h[2]) # Calling single list item
h[2] = "Buffalo" # Updating item is added or not
print(h) # Checking item is updated
h.remove("Buffalo")
print(h) # Remove item is added


h.append("Bear") # Add item in list
print(h)
print(h[1:3])  # It will print the value starting from index 1 and end with 3-1.
#l[1] = "Change After Creating List column"




# Tuple
j = ('qwerty','asdfgh','zxcvb', "qwerty")
print(j)
print(j[1])
#j[0] = "AppleApple"


l = ('wewe','kewe','tewe','sewe', 45, 45)   # we can add string as well as int but () treated as tuple
print(l)
print(l[3]) # Calling single tuple item
#l[2] = "Buffalo" # Adding one item  , you will get # Tuples don't support item assignment


# Set

m = {23, "Test1", "Test1", "Test2",  "Test2"}
print(m)
m.add("Test3")
print(m)
m.remove("Test3")
print(m)
m.update(["Test3"])
print(m)

#Explanation:

#First print: {23, 'Test1', 'Test2'} - Sets automatically remove duplicates, so "Test1" and "Test2" appear once
#After m.add("Test3"): {23, 'Test1', 'Test2', 'Test3'} - add() accepts single hashable elements
#After m.remove("Test3"): {23, 'Test1', 'Test2'} - Removes the exact element
#Last line fails: m.update("Test3") raises TypeError because update() expects iterables (lists, tuples, sets), not single strings. Use m.update(["Test3"]) instead

# Dictionary --> Works as Key : Value pair
k = {4 : "abc", 2 : "xyz", 3 : "jkl", "o" : "uiop", "oo" : "uiop"}
print(k)
print(k[2])
print(k["o"])
k.update({"3":"TestRun"})  # It's updated or added the new key value pair in dictionary.
k[4] = "tip"   # it will update the existing key value.
print(k)
print(k.items())
print(k.keys())
print(k.values())


# How to create a dictionary at run time

dict = {}
dict["Username"] = "Parveen"
dict["Password"] = "Chaudhary"
dict["RollNumber"] = 789456123

print(dict)
print(dict["Username"]) # How to print dictionary key and its value.
