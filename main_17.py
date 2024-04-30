import asyncio
import time

async def delay(delay_seconds: int) -> int:
		print(f'sleep for  {delay_seconds} ')
		await asyncio.sleep(delay_seconds)
		print(f'slepp for {delay_seconds} ended')
		return delay_seconds

async def main():
    t1 = time.time()
    tasks = []
    for i in range(1, 6):
        tasks.append(asyncio.create_task(delay(i)))

    results = await asyncio.gather(*tasks)

    print('-------------------------------------------')
    for result in results:
        print(result)
    print('-------------------------------------------')

    t2 = time.time()
    print(t2 - t1)


asyncio.run(main())