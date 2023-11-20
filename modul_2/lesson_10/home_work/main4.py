import json


class File:
    def __init__(self, filename: str):
        self.filename = filename

    def read(self):
        with open(self.filename, "r") as f:
            return json.load(f)

    def write(self, data: dict):
        datas = self.read()
        datas.append(data)
        with open(self.filename, "w") as f:
            json.dump(datas, f, indent=3)

    def show(self):
        films = self.read()
        for i, film in enumerate(films, start=1):
            for key, value in film.items():
                print(f"{key}: {value}")
            print()

    def search(self):
        pass


while True:
    menu = """
    1. ADD 
    2. SHOW 
    3. DELETE
    4. SEARCH
    4. Exit
    --------> """
    key = input(menu)
    match key:
        case "1":
            car = {"id": input("ID: "),
                   "Nomi": input("Nomi : "),
                   "Mamlakat": input("Mamlakat : "),
                   "Janr": input("Janr : "),
                   "Yili": input("Yili:")}
            f = File("film.json")
            f.write(car)

        case "2":
            f = File("film.json")
            f.show()
        case "3":
            pass
        case "4":
            break
