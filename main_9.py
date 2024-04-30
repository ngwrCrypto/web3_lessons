import asyncio
import time
async def delay(delay_seconds: int) -> int:
    print(f'i`m sleeping on {delay_seconds} seconds')
    await asyncio.sleep(delay_seconds)
    print(f'my sleep time {delay_seconds} seconds ended')
    return delay_seconds


async def hello_every_second() -> None:
    for i in range(2):
        await asyncio.sleep(1)
        print('while i wait, doing another code')


# async def hello_every_second() -> None:
#     i = 0
#     while i < 2:
#         await asyncio.sleep(1)
#         print('while i wait, doing another code')
#         i += 1

async def main() -> None:
    t1 = time.time()

    first_delay = asyncio.create_task(delay(3))
    second_delay = asyncio.create_task(delay(3))
    await hello_every_second()
    await first_delay
    await second_delay
    t2 = time.time()
    print(t2-t1)


asyncio.run(main())