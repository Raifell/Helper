from functools import reduce

myList=[[[1, 2, 3], [4, 5, 6]], [[2, 3, 4], [3, 4, 5]], [[4, 6, 7], [5, 7, 9]]]
print(reduce(lambda x, y: x+y, myList))

result = [[1, 2, 3], [4, 5, 6], [2, 3, 4], [3, 4, 5], [4, 6, 7], [5, 7, 9]]

a = [[[x for x in range(5)] for _ in range(3)] for _ in range(2)]

