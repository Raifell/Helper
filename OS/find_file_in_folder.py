from os import listdir
from os.path import isfile, join

# Вариант, через библиотеку OS, возвращает только файлы

onlyfiles = [f for f in listdir('Batch') if isfile(join('Batch', f))]

print(onlyfiles)

# Вариант, через библиотеку glob, возвращает все содержимое

import glob
print(glob.glob("Batch/*"))
