import random

b = [random.randint(0, 10) for x in range(10)]
print(b)

a = [z for z in [random.randint(0, 10) for x in range(10)] if z % 2 == 0] if random.randint(0, 10) > 5 else \
    [z for z in [random.randint(0, 10) for x in range(10)] if z % 2 == 1]
print(a)

vir = ['int', *[random.randint(1, 10) for _ in range(10)]]
print(' '.join([str(x) for x in vir]))

print(' '.join([str(x) for x in ['int', *[random.randint(1, 10) for _ in range(10)]]]))
