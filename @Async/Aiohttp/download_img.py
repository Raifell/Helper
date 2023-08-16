import requests
import asyncio
import aiohttp
from os import makedirs
ind = 1


def save_file(data, i):
    global ind
    if i == 1:
        makedirs('Aiohttp', exist_ok=True)
        path = f'Aiohttp/file-{ind}.jpg'
        print('download: file-{} with aiohttp'.format(ind))
    else:
        makedirs('Requests', exist_ok=True)
        path = f'Requests/file-{ind}.jpg'
        print('download: file-{} with requests'.format(ind))
    with open(path, 'wb') as f:
        f.write(data)

    ind += 1


async def connect(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, allow_redirects=True) as response:
            data = await response.read()
            save_file(data, 1)


async def main1():
    url = 'https://loremflickr.com/320/240'
    count = [asyncio.create_task(connect(url)) for _ in range(10)]
    await asyncio.gather(*count)


#----------------------------------------------------------------#


def connection(url):
    session = requests.session()
    response = session.get(url, allow_redirects=True).content
    save_file(response, 0)


def main2():
    url = 'https://loremflickr.com/320/240'
    count = [connection(url) for _ in range(10)]
    del count


if __name__ == '__main__':
    asyncio.run(main1())
    main2()
