import csv


class File:
    def __init__(self, filename: str, fieldname: list = None):
        self.filename = filename
        self.fieldname = fieldname

    def write(self, data: dict):
        with open(self.filename, "a") as f:
            writer = csv.DictWriter(f, self.fieldname)
            writer.writerow(data)

    def read(self):
        with open(self.filename, "r") as f:
            re = []
            datas = csv.DictReader(f)
            for data in datas:
                re.append(data)
            return re

    def clear(self):
        with open(self.filename, "w") as f:
            writer = csv.writer(f)
            writer.writerow(self.fieldname)

    def delete(self, index):
        data = self.read()
        if len(data) > 0:
            del data[0]
            with open(self.filename, "w") as f:
                writer = csv.DictWriter(f, self.fieldname)
                writer.writeheader()
                writer.writerows(data)
                print("Muvaffaqiyatli o'chirildi ✅")


def main():
    menu = """
    1) Add books
    2) Update books
    3) Delete books
    4) Show books
    5) Exit
    >>>"""
    key = input(menu)
    match key:
        case "1":
            f = File("books.csv", ["id", "name", "author", "category"])
            book = {"id": input("Id: "),
                    "name": input("Name: "),
                    "author": input("Author: "),
                    "category": input("Category: ")}
            f.write(book)
            print("Kitob muvaffaqiyatli qo'shildi ✅")
            main()

        case "2":
            fields = """
            1) Update Name
            2) Update Author
            3) Update Category
            4) Exit
            >>>"""
            key = input(fields)
            match key:
                case "1":
                    id = input("Id books: ")
                    new_value = input("New value: ")
                    f = File("books.csv", ["id", "name", "author", "category"])
                    books = f.read()
                    for i, book in enumerate(books):
                        if book.get("id") == id:
                            books[i]["name"] = new_value
                            break
                    f.clear()
                    for i in books:
                        f.write(i)
                    print("Kitob nomi yangilandi ✅")
                    main()

                case "2":
                    id = input("Id book: ")
                    new_value = input("New value: ")
                    f = File("books.csv", ["id", "name", "author", "category"])
                    books = f.read()
                    for i, book in enumerate(books):
                        if book.get("id") == id:
                            books[i]["author"] = new_value
                            break
                    f.clear()
                    for i in books:
                        f.write(i)
                    print("Kitob muallifi muvaffaqiyatli yangilandi✅")
                    main()

                case "3":
                    id = input("Id book: ")
                    new_value = input("New value: ")
                    f = File("books.csv", ["id", "name", "author", "category"])
                    books = f.read()
                    for i, book in enumerate(books):
                        if book.get("id") == id:
                            books[i]["category"] = new_value
                            break
                    f.clear()
                    for i in books:
                        f.write(i)
                    print("Kitob toifasi muvaffaqiyatli yangilandi✅")
                    main()

                case "4":
                    main()

        case "3":
            id = input("Id: ")
            f = File("books.csv", ["id", "name", "author", "category"])
            delete = f.read()
            for i, user in enumerate(delete):
                if user.get("id") == id:
                    del [i]
                    break
            f.delete(f)
            main()

        case "4":
            f = File("books.csv", ["id", "name", "author", "category"])
            for i in f.read():
                print(i)
            main()

        case "5":
            main()
main()