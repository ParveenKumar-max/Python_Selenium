# Dictionary works with key value pair

dict_01 = {"a":123,"b":456,"c":789}
dict_02 = {"d":123,"e":222,"f":333}

Dict_03 = {**dict_01, **dict_02}
print(Dict_03)

#  Because ** tells Python:
#
# “Unpack this dictionary into separate key–value pairs.”

