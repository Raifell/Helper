import random

b = [random.randint(0, 10) for x in range(10)]
print(b)

a = [z for z in [random.randint(0, 10) for x in range(10)] if z % 2 == 0] if random.randint(0, 10) > 5 else \
    [z for z in [random.randint(0, 10) for x in range(10)] if z % 2 == 1]
print(a)
