# This script demonstrates a simple asynchronous function using asyncio.
# It prints "Hello", waits for 1 second without blocking, then prints "World".

import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

asyncio.run(say_hello())
