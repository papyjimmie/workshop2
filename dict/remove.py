# EX 1

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.pop("model")
print(thisdict)
# Output: {'brand': 'Ford', 'year': 1964}

# EX 2

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.popitem()
print(thisdict)
# Output: {'brand': 'Ford', 'model': 'Mustang'}

# EX 3

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
del thisdict["model"]
print(thisdict)
# Output: {'brand': 'Ford', 'year': 1964}

# EX 4

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.clear()
print(thisdict)
# Output: {}