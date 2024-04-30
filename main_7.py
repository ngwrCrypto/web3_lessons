import asyncio


async def delay(delay_seconds: int) -> int:
    print(f'Sleeping for {delay_seconds} seconds...')
    await asyncio.sleep(delay_seconds)
    print(f'Done sleeping for {delay_seconds} seconds')
    return delay_seconds


async def main() -> None:
    one_plus_one = await delay(1)
    two_plus_one = await delay(2)
    print(one_plus_one)
    print(two_plus_one)


asyncio.run(main())