import json

count = [] # Список, куда собираем данные

a = 'string'
b = {'key': 'value', 'nums': [1, 2, 3], 'words': ['text', 'text', 'text']}
c = [10, 11, 12]

count.append(a)
count.append(b)
count.append(c)

data_save = json.dumps(count, indent=2) # Записываем данные в строку формата json

data_load = json.loads(data_save) # Загружаем данные из строки json в обьект python

print(data_load)
