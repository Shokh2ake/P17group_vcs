import asyncio


async def factorial(n):
    result = 1
    async for i in factorial(n):
        result *= i
    return result

n = int(input("n: "))
asyncio.run(factorial(n))

# import asyncio
# import json
#
#
# class File:
#     def __init__(self, filename):
#         self.filname = filename
#
#     async def write(self):
#         async with open(self.filname, "w") as f:
#             data = json.dumps([1, 2, 3], indent=3)
#             await f.write(data)
#
#     async def read(self):
#         async with open(self.filname, "r") as f:
#             data = await f.read(f)
#         return data
#
# asyncio.run(File.write([1, 2, 3]))


import asyncio
import time
# import response


async def main():
    urls = [
        'https://www.example.com',
        'https://www.google.com',
        'https://www.github.com'
    ]
    l = []
    for i in urls:
        l.append(asyncio.create_task(response(i)))
    for i in l:
        res = await i
        print(len(res))

start = time.time()
asyncio.run(main())
print(time.time()- start)
