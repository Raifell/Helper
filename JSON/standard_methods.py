import json
import requests

URL = 'https://jsonplaceholder.typicode.com/todos'

str_json = requests.get(URL).text # Загрузка данных json в формате str

dict_json = json.loads(str_json) # Преобразование json в список со словарями (json.loads - для загрузки из строки)
new_dict_json = []

for x in dict_json: # Сортируем в новый список все данные где ключ ['userId'] == 1:
    if x['userId'] == 1:
        new_dict_json.append(x)

for x in new_dict_json: # Добавляем новый ключ/значение
    x['key'] = 'value'

for x in range(len(new_dict_json)): # Выводим информацию из нового списка
    for y, z in new_dict_json[x].items():
        print(y + ':', z)
    print()

with open('example.json', 'w') as file: # Сохраняем новый список в файл json (json.dump - для записи в файл)
    json.dump(new_dict_json, file, indent=2)

with open('example.json', 'r') as file: # Загрузка из файла (json.load - для загрузкииз файла)
    ax = json.load(file)

for x in ax: # Удаляем ключ
    x.pop('key', None)

bx = json.dumps(ax, indent=2) # Преобразуем словарь в объект json (json.dumps - для записи встроку)


