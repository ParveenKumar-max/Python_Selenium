print("**************************** List ( IN & NOT IN )*********************")

my_list = [1, 2.12, "Parveen", True , [1, 2, 3]]
one_more_list = list("Parveen")
print("e" in one_more_list)
print("a" not in one_more_list)

print("**************************** List - Indexing *********************")

my_list_value = [[0, 2], [4, 6], [8, 10], [12, 14]]
print(my_list_value[0])
print(my_list_value[3][1])

my_list_value_01 = ["chair", "table", "desk", "lamp", "bed"]
print(my_list_value_01[-5])
print("Most people own at least 2 chairs" + str(my_list_value[0][1]) + " " +str(my_list_value_01[0]) + "s.")

my_list_value_02 = [0.98, 8.76, 6.54, 4.32]
print(my_list_value_02[1:])  # it will print all value from index 1 to the end of the list
print(my_list_value_02[1:3])
print(my_list_value_02[:2])

print("**************************** List - Delete & Remove *********************")

arctic_animals = ["elephant", "penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer","tiger"]
del arctic_animals[2] # it will delete the value of index 1, which is elephant
print(arctic_animals)
arctic_animals.remove("tiger") 
# it will remove the value of "tiger" from the list, and if there are multiple "tiger" in the list,
#  it will remove the first one it finds  
print(arctic_animals)
arctic_animals.append("arctic fox")
print(arctic_animals)
arctic_animals.insert(1, "snowy owl")
print(arctic_animals)
print(arctic_animals.pop())
print(arctic_animals.pop(2))

print("**************************** Dictionary ********************* \n")
Dict_01 = {"a" : "apple", "b" : "ball", "c" : "cat", "d" : "dog", "e" : "elephant"}
print(Dict_01["c"])
print(Dict_01.keys())
print("a" in Dict_01)
print("b" not in Dict_01)

print("*************** Dictionary -- Keys(), Values(), items(), get() ******************* \n")

Dict_02 = {"Queen": "Bohemian Rhapsody",
            "Bee Gees": "Stayin' Alive",
            "U2": "One",
            "Michael Jackson": "Billie Jean",
            "The Beatles": "Hey Jude",
            "Bob Dylan": "Like A Rolling Stone"}
print("The length f the dictionary is :" , len(Dict_02))
print(Dict_02.keys())
print(Dict_02.values())
print(Dict_02.items()) 

# it will return key-value pair from the dictionary
for keys in Dict_02.keys():
    print(keys)

if Dict_02.get("Promise of the Real"):
    print(Dict_02.values)
else:
    print("The key is not found in the dictionary.")

print("*************** Dictionary -- .fromkeys(), .pop(), .popitem() ******************* \n")


for key, value in {}.fromkeys("bcdfghjklmnpqrstvwxyz", "consonant").items():
    print(key, value)
fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}
print(fast_food_items.pop("McDonald's")) # it will remove the key "McDonald's" and its corresponding value "Big Mac" from the dictionary, and it will return the value "Big Mac"

fast_food_items.popitem() # it will remove the last key-value pair from the dictionary, and it will return the removed key-value pair as a tuple
print(fast_food_items)


print("*************** Dictionary -- .clear(), .copy(), .update() ******************* \n")

Dict_03 = {"a" : "apple", "b" : "ball", "c" : "cat", "d" : "dog", "e" : "elephant"}
print(Dict_03)
Dict_03.clear() # it will remove all key-value pairs from the dictionary, and it will return an empty dictionary
print(Dict_03)

internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
print(internet_celebrities)
another_one = {"shroud": "Twitch"}
internet_celebrities.update(another_one) # it will add the key-value pair from another_one to internet_celebrities, and if there are any duplicate keys, it will update the value of the existing key in internet_celebrities with the value from another_one
print(internet_celebrities)

Another_Dict = internet_celebrities.copy()
Another_Dict["shroud"] = "YouTube"  # it will change the value of the key "shroud" in Another_Dict to "YouTube", but it will not affect the value of the key "shroud" in internet_celebrities, because we have created a copy of internet_celebrities and assigned it to Another_Dict, so they are two different dictionaries in memory, and changing one dictionary will not affect the other dictionary
print(Another_Dict)

print(internet_celebrities.clear()) # it will remove all key-value pairs from the dictionary, and it will return an empty dictionary
print(Another_Dict)

print("*************** Dictionary -- .setdefault() ******************* \n")

