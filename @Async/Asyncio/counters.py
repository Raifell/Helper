import asyncio


async def p_nums():
    num = 1
    while num < 40:
        print(num)
        num += 1
        await asyncio.sleep(0.5)


async def p_time():
    count = 0
    while count < 20:
        if count % 3 == 0:
            print('{} seconds left'.format(count))
        count += 1
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(p_nums())
    task2 = asyncio.create_task(p_time())

    await asyncio.gather(task1, task2)


if __name__ == '__main__':
    asyncio.run(main())