import asyncio
import time

async def delay(delay_seconds: int) -> int:
    print(f'i`m for {delay_seconds} seconds starting')
    await asyncio.sleep(delay_seconds)
    print(f'i`m for {delay_seconds} seconds ending')
    return delay_seconds

async def main() -> None:
    t1 = time.time()

    sleep_for_three = asyncio.create_task(delay(3))
    sleep_again = asyncio.create_task(delay(3))
    sleep_once_more = asyncio.create_task(delay(3))
    await sleep_for_three
    await sleep_again
    await sleep_once_more
    t2 = time.time()
    print(t2-t1)

asyncio.run(main())