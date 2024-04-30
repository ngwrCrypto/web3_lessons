import asyncio
import time


async def delay(delay_seconds: int) -> int:
		print(f'going sleep {delay_seconds} ')
		await asyncio.sleep(delay_seconds)
		print(f'my sleep time {delay_seconds}ended')
		return delay_seconds

async def main():
    t1 = time.time()
    results = await asyncio.gather(
        asyncio.create_task(delay(1)),
        asyncio.create_task(delay(2)),
        asyncio.create_task(delay(3)),
    )

    print('-------------------------------------------')
    print(results)
    for result in results:
        print(result)
    print('-------------------------------------------')

    t2 = time.time()
    print(t2 - t1)


asyncio.run(main())