import asyncio
import time

async def delay(delay_seconds: int) -> int:
		print(f'going to sleep{delay_seconds} ')
		await asyncio.sleep(delay_seconds)
		print(f'сmy sleep  {delay_seconds} is over ')
		return delay_seconds

async def main():
    t1 = time.time()

    tasks = []
    for i in range(1, 6):
        tasks.append(asyncio.create_task(delay(i)))

    await asyncio.wait(tasks)

    print('-------------------------------------------')
    for task in tasks:
        print(task.result())
    print('-------------------------------------------')

    t2 = time.time()
    print(t2 - t1)


asyncio.run(main())