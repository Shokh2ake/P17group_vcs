# import time
# import asyncio
#
#
# async def tasck1():
#     print("tasck1 strat")
#     await asyncio.sleep(2)
#     print("tasck1 finish")
#
#
# async def tasck2():
#     print("tasck2 strat")
#     await asyncio.sleep(1)
#     print("tasck2 finish")
#
#
# async def main():
#     tasck1_var = asyncio.create_task(tasck1())
#     tasck2_var = asyncio.create_task(tasck2())
#     # await tasck1_var
#     # await tasck2_var
#     print("function strat")
#     await asyncio.sleep(2)
#     print("function finish")
#
#
# start = time.time()
# asyncio.run(main())
# print(time.time() - start)

# import requests
# import asyncio
# async def response():
#     pass
#
#
# async def main():
#     urls = [
#         'https://www.example.com',
#         'https://www.google.com',
#         'https://www.github.com'
#     ]
#     l = []
#     for i in urls:
#         l.append()
#
# asyncio.run(main())

import asyncio
import aiofiles

# async def main():
#     async with aiofiles.open("text.txt", "r") as f:
#         data = await f.read()
#     return data
#
#
# if __name__ == '__main__':
#     print(asyncio.run(main()))


import aiohttp


async def main():
    async with aiohttp.ClientSession as session:
        data = await session.get("https://www.example.com")
        print(data.text)


asyncio.run(main())
