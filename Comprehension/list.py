a = [[[x for x in range(5)] for _ in range(3)] for _ in range(2)]
b = [x for z in a for x in z]
print(a)
print(b)
