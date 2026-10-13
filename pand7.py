#asynchronous
import asyncio
async def task (name):
    print("starting",name)
    await asyncio.sleep(2)
    print("finished",name)
async def main():
    await asyncio.gather(task("Task A"),task("Task B"),task("Task C"))
asyncio.run(main())
