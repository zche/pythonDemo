import time
import asyncio


async def helloworld():
    time.sleep(1)
    print("hello world!")


if __name__ == "__main__":
    # asyncio.run(helloworld())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(helloworld())
    print("yes")