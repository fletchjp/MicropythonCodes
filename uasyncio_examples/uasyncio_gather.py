# uasyncio_gather.py
# See Section 2.2.3
# https://github.com/peterhinch/micropython-async/blob/master/v3/docs/TUTORIAL.md

import uasyncio as asyncio

async def bar(n):
    for count in range(n):
        await asyncio.sleep_ms(200 * n)  # Pause by varying amounts
    print('Instance {} stops with count = {}'.format(n, count))
    return count * count

async def main():
    tasks = (bar(2), bar(3), bar(4))
    print('Waiting for gather...')
    res = await asyncio.gather(*tasks)
    print(res)

asyncio.run(main())