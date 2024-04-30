import asyncio
import time

async def delay(delay_seconds: int) -> int:
    print(f'i`m sleeping on {delay_seconds} seconds')
    await asyncio.sleep(delay_seconds)
    print(f'my sleep time {delay_seconds} seconds ended')
    return delay_seconds


async def main() -> None:
    t1 = time.time()

    tasks = [
        asyncio.create_task(delay(1)),
        asyncio.create_task(delay(2)),
        asyncio.create_task(delay(3)),
    ]

    done, pending = await asyncio.wait(tasks)
    print('*******************************************')
    for task in tasks:
        print(task.result())
    print('*******************************************')

    t2 = time.time()
    print(t2 - t1)

asyncio.run(main())