import requests


def get_file(url):
    response = requests.get(url=url, allow_redirect=True) # Разрешает изменение ссылки для перехода
    return response


def write_file(response):
    filename = response.url.split('/')[-1]
    with open(filename, 'wb') as file:
        file.write(response.content)


def main():
    url = 'http://...'
    for i in range(10):
        write_file(get_file(url))


if __name__ == '__main__':
    main()
