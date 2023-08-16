import asyncio


async def fn():

    task = asyncio.create_task(fn2())
    print('one')
    await asyncio.sleep(3)
    print('four')
    await asyncio.sleep(1)
    print('five')


async def fn2():

    print('two')
    await asyncio.sleep(2)
    print('three')


asyncio.run(fn())
