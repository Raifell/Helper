import os

# Вариант исполнения через try/except

try:
    os.makedirs("path/to/directory")
except FileExistsError:
    pass

# Строчный вариант исполнения

os.makedirs("path/to/directory", exist_ok=True)
