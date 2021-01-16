# EX 1

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict["year"] = 2020
print(thisdict)

# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

# EX 2

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.update({"year": 2020})

print(thisdict)

# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}