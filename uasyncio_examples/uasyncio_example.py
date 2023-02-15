# uasyncio example
# See Section 2.2
# https://github.com/peterhinch/micropython-async/blob/master/v3/docs/TUTORIAL.md

import time
import uasyncio as asyncio

async def bar(t):
    print ('Bar started: waiting {:.2f} secs'.format(t))
    await asyncio.sleep(t)
    print ('Bar done')

async def main():
    await bar(1)
    task = asyncio.create_task(bar(5))
    await asyncio.sleep(0)
    print ('Got here: bar running')
    await task
    print ('All done')
start = time.time()
asyncio.run(main())    
end = time.time()
# Two different ways to print the same thing.
print('Time: {:.2f} secs'.format(end-start))
print(f'Time: {end-start:.2f} secs')
