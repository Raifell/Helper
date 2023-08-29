import numpy as np

a = np.zeros(10, 'int')
print(a) # Простой массив с нулями

a = np.arange(0, 10, 2)
print(a) # Массив возрастающий диапазон, шаг 2

a = np.arange(12, 0, -3)
print(a) # Массив убывающий диапазон, шаг -3

a = [x*x for x in np.arange(0, 10)]
print(a) # Массив возрастающий диапазон, по квадрату элемента

b = [np.arange(0, 10)[i] for i in range(len(np.arange(0, 10))) if i % 2 == 0]
print(b) # Массив, только значения имеющие четный индекс
print(sum(b)) # Сумма значений
