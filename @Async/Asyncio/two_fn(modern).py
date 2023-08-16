import asyncio
a = 0


async def fn1():
    global a
    print('a = ', a)
    await asyncio.sleep(5)
    a = 10
    print('a = ', a)
    await asyncio.sleep(5)
    a = 20
    print('a = ', a)


async def fn2():
    global a
    await asyncio.sleep(2.5)
    a = 5
    print('a = ', a)
    await asyncio.sleep(5)
    a = 15
    print('a = ', a)


async def main():
    task1 = asyncio.create_task(fn1())
    task2 = asyncio.create_task(fn2())

    await asyncio.gather(task1, task2)


if __name__ == '__main__':
    asyncio.run(main())
