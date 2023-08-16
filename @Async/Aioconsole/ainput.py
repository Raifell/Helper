from aioconsole import ainput


async def some_coroutine():
    line = await ainput(">>> ")