# import requests
# import json
# import time
# import multiprocessing
# import threading
#
#
# """Home work - 1"""
# def append_data(data):
#     for i in data:
#         datas = requests.get(i)
#         with open("File.json", "a") as f:
#             json.dump(datas.json(), f, indent=3)
#
#
# start = time.time()
# datas = "https://jsonplaceholder.typicode.com/posts https://jsonplaceholder.typicode.com/comments https://jsonplaceholder.typicode.com/albums https://jsonplaceholder.typicode.com/photos https://jsonplaceholder.typicode.com/todos https://jsonplaceholder.typicode.com/users".split()
#
# append_data(datas)
# print(time.time())
"""Home work - 2"""
# def writer_data(url):
#     data = requests.get(url)
#     with open("File.json", "a") as f:
#         json.dump(data.json(), f, indent=3)
#
# start = time.time()
# datas = [
#     "https://jsonplaceholder.typicode.com/posts",
#     "https://jsonplaceholder.typicode.com/comments",
#     "https://jsonplaceholder.typicode.com/albums",
#     "https://jsonplaceholder.typicode.com/photos",
#     "https://jsonplaceholder.typicode.com/todos",
#     "https://jsonplaceholder.typicode.com/users"
# ]
#
# with multiprocessing.Pool(8) as p:
#     p.map(writer_data, datas)
#
# print("Ish bajarildi vaqt:", time.time() - start)
# =================================================================
# def writer_data(url):
#     data = requests.get(url)
#     with open("File.json", "a") as f:
#         json.dump(data.json(), f, indent=3)
#
#
# start = time.time()
# datas = [
#     "https://jsonplaceholder.typicode.com/posts",
#     "https://jsonplaceholder.typicode.com/comments",
#     "https://jsonplaceholder.typicode.com/albums",
#     "https://jsonplaceholder.typicode.com/photos",
#     "https://jsonplaceholder.typicode.com/todos",
#     "https://jsonplaceholder.typicode.com/users"
# ]
#
# threads = []
#
# for url in datas:
#     thread = threading.Thread(target=writer_data, args=(url,))
#     threads.append(thread)
#     thread.start()
#
# for thread in threads:
#     thread.join()
#
# print("Ish bajarildi vaqt:", time.time() - start)


