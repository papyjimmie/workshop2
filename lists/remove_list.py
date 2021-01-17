# EX 1

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)  # Output: ['apple', 'cherry']

# EX 2

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)  # Output: ['apple', 'cherry']

# EX 3

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)  # Output: ['apple', 'banana']

# EX 4

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)  # Output: ['banana', 'cherry']

# EX 5

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)  # Output: []
