import asyncio
import aiohttp

# Вариант 1 - одна функция


async def main1():
    url = "https://www.google.com"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            status = resp.status
            data = await resp.read()
            print(status)
            print(data)


if __name__ == '__main__':
    asyncio.run(main1())


# Вариант 2 - две, переходные функции


async def connect(url, session):
    async with session.get(url) as resp:
        status = resp.status
        data = await resp.read()
        print(status)
        print(data)


async def main2():
    url = "https://www.google.com"

    async with aiohttp.ClientSession() as session:
        task = asyncio.create_task(connect(url, session))

        await task


if __name__ == '__main__':
    asyncio.run(main2())
