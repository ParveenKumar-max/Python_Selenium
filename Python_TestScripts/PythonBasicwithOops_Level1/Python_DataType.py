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
print(d +" | ",  e)
#print(f + " | ", e)
print("Value of int {} + {}".format(f, e))

# List
g = [1,2,3,4,5,6] # List has start with 0 index
print(g)
print(g[4])
h = ["Goat","Sheep","Cow","Lion","Tiger", 24, 56]
l = ('wewe','wewe','ewewe','wewe', 45, 45)   # we can add string as well as int but () treated as tuple
print(h)
print(h[2])
h[2] = "Buffalo"
print(h)
h.append("Bear")
print(h)
print(l)
print(l[1:3])  # It will print the value starting from index 1 and end with 3-1.
#l[1] = "Change After Creating List column"
print(l)



# Tuple
i = ['Apple','Orange','Banana','Ananas','Pineapple', 78, 89] # Tuple has start with 0
j = ('qwerty','asdfgh','zxcvb')
print(i)
print(i[3])
i[0] = "AppleApple"
print(i)

print(j)
#j[2] = "Change zxcvb to Busy"

# Dictionary --> Works as Key : Value pair
k = {4 : "abc", 2 : "xyz", 3 : "jkl", "o" : "uiop"}
print(k)
print(k[2])
print(k["o"])
k[4] = "tip"
print(k)

# How to create a dictionary at run time

dict = {}
dict["Username"] = "Parveen"
dict["Password"] = "Chaudhary"
dict["RollNumber"] = 789456123

print(dict)
print(dict["Username"])
