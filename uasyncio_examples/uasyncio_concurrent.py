# uasyncio_concurrent.py
# See Section 2.2
# https://github.com/peterhinch/micropython-async/blob/master/v3/docs/TUTORIAL.md

import time
import uasyncio as asyncio

async def bar(x):
    count = 0
    while True:
        count += 1
        print('Instance: {} count: {}'.format(x, count))
        await asyncio.sleep(1)
        
async def main():
    for x in range(3):
        asyncio.create_task(bar(x))
    print('Tasks are running')
    await asyncio.sleep(10)
    
start = time.time()
asyncio.run(main())
end = time.time()
# Two different ways to print the same thing.
print('Time: {:.2f} secs'.format(end-start))
print(f'Time: {end-start:.2f} secs')

