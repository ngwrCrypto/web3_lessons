import asyncio
import time

async def delay(delay_seconds: int) -> int:
    print(f'i`m sleeping on {delay} seconds')
    await asyncio.sleep(delay_seconds)

    if delay_seconds == 2:
        raise ValueError('i`m raising an error')

    print(f'my sleep time {delay_seconds} seconds ended')
    return delay_seconds


async def main() -> None:
    t1 = time.time()

    await asyncio.wait([
        asyncio.create_task(delay(1)),
        asyncio.create_task(delay(2)),
        asyncio.create_task(delay(3)),
    ])
    t2 = time.time()
    print(t2-t1)

asyncio.run(main())


