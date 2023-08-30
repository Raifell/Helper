s = [['one', 1, 2, 3], ['two', 2, 3, 4], ['three', 3, 4, 5]]
v = {x[0]: x[1:] for x in s}

print(v)
