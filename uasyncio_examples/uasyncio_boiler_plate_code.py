# uasyncio boiler plate.
# This is NOT working code.
# See Section 2.2.4
# https://github.com/peterhinch/micropython-async/blob/master/v3/docs/TUTORIAL.md

import uasyncio as asyncio
from my_app import MyClass

def set_global_exception():
    def handle_exception(loop, context):
        import sys
        sys.print_exception(context["exception"])
        sys.exit()
    loop = asyncio.get_event_loop()
    loop.set_exception_handler(handle_exception)

async def main():
    set_global_exception()  # Debug aid
    my_class = MyClass()  # Constructor might create tasks
    asyncio.create_task(my_class.foo())  # Or you might do this
    await my_class.run_forever()  # Non-terminating method
try:
    asyncio.run(main())
finally:
    asyncio.new_event_loop()  # Clear retained state
