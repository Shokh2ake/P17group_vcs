import json


class File:
    def __init__(self, filname):
        self.filename = filname

    def read(self):
        with open(self.filename, "r") as f:
            return json.load(f)

    def write(self, data):
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=3)
