

import json
#
import requests
#
# # with open("users.json", "r") as f:
#
#
#
data = requests.get("https://jsonplaceholder.typicode.com/users")


with open("users.json", "w") as f:
    json.dump(data.json(), f, indent=3)









