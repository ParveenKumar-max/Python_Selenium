list = [123, 123, 'abc', 'abc']
list.append(456)
list.remove('abc')
print(list)

tuple = (123, 123, 'abc', 'abc')
#tuple.append(123)
#tuple.remove('abc')  # Give no option to add and remove the tuple list
print(tuple)

set = {123, 123, 'abc', 'abc'}
set.add(678)
set.add('def')
set.remove('abc')
print(set)

dict = {'a' : 123, 'b' : 123, 'c' : 'abc', 'd' : 'def'}
dict['e'] = 'def'
dict['a'] = '456'
dict.update({'b' : '4569'})
del dict['b']
print(dict)


a = 1223
print(a)
a = "232132"
print(a)
a = 123456
print(a)
print(a + a)