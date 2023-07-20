import requests

im_data = requests.get('https://www.parsemachine.com/media/cache/90/ee/90eee0c6163a13b739ac70ffb6e7d65a.png')

with open('image_1.png', 'wb') as file: # Запись в байтовом формате 'wb'
    file.write(im_data.content) # По ссылке скачаиваем данные параметра .content
