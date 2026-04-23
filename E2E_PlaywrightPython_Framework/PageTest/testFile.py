A = [{"a" : "list1", "b" : "list2", "c" : 10}, {"a": "list1", "b" : "list2", "c": 20}, {"a" : "list1", "b" : "list2", "c": 30}]
print(A)
print(type(A))

check = lambda x : x * 2
print(check(2))

check = lambda x : "Positive" if x > 0 else "Negative" if x < 0 else "ZERO"
print(check(5))

list_name = [1, 2, 3, 41, 5]
Numbers = list(map(lambda x : x * 2, list_name))
print(Numbers)

list_name = [1, 2, 3, 41, 5]
Numbers = list(filter(lambda x : x % 2 == 0, list_name))
print(Numbers)