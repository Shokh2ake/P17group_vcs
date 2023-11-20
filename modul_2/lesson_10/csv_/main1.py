#
# import csv
#
#
# with open("cars.csv" , "w") as f:
#     writer = csv.writer(f)
#
#     writer.writerow(["GM","chevrolet","gentra"])

# import csv
#
# with open('names.csv', 'w') as csvfile:
#     fieldnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#     writer.writeheader()
#     writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})


# import csv
#
#
# # with open("names.csv" , "x") as f:
# #     data = csv.DictReader(f)
# #     for i in data:
# #         print(i)
# import csv
#
# with open("cars.csv", "a") as f:
#     fieldname = ["id", "company", "model", "name"]
#     writer = csv.DictWriter(f, fieldnames=fieldname)
#     writer.writeheader()
#     # while True:
#     company = input("Company: ")
#     model = input("Model: ")
#     name = input("Name: ")
#     writer.writerow({"id": 1, company": company, "model": model, "name": name})

# json, txt, csv

# import csv
#
# with open("cars.csv", "r") as f:
#     datas = csv.DictReader(f)
#     for data in datas:
#         print(data)
# import csv
#
#
# class File:
#     def __init__(self, filename: str, fieldname=None):
#         self.filename = filename
#         self.fieldname = fieldname
#
#     def read(self):
#         with open(self.filename, "r") as f:
#             rezult = []
#             datas = csv.DictReader(f)
#             for data in datas:
#                 rezult.append(data)
#             return rezult
#
#     def write(self, data: dict):
#         if not self.read():
#             with open(self.filename, "a") as f:
#                 writer = csv.DictWriter(f, self.fieldname)
#                 writer.writeheader()
#                 writer.writerow(data)
#
#         else:
#             with open(self.filename, "a") as f:
#                 writer = csv.DictWriter(f, self.fieldname)
#                 writer.writerow(data)
#
#
# def main():
#     menu = """
#     1) read
#     2) write
#     3) edit
#     4) exit
#     >>>"""
#     key = input(menu)
#     match key:
#         case "1":
#             f = File("users.csv", ["id", "name", "age", "phone"])
#             for i in f.read():
#                 print(i)
#             main()
#         case "2":
#             f = File("users.csv", ["id", "name", "age", "phone"])
#             user = {"id": input("Id: "),
#                     "name": input("Name: "),
#                     "age": input("Age: "),
#                     "phone": input("Phone: ")}
#             f.write(user)
#             main()
#         case "3":
#             fields = """
#             1) name
#             2) age
#             3) phone
#             >>>"""
#             key = input(fields)
#
# main()


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
            result = []
            datas = csv.DictReader(f)
            for data in datas:
                result.append(data)
            return result

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
                print("Deleted successfully ✅")


def main():
    menu = """
    1. Add books
    2. Update books
    3. Delete books
    4. Show books
    5. Exit
    -------> """
    key = input(menu)
    match key:
        case "1":
            f = File("booksCRUD.csv", ["id", "name", "author", "category"])
            book = {"id": input("ID: "),
                    "name": input("NAME: "),
                    "author": input("AUTHOR: "),
                    "category": input("CATEGORY: ")}
            f.write(book)
            print("Book added successfully ✅")
            main()
        case "2":
            fields = """
            1. UPDATE name
            2. UPDATE author
            3. UPDATE category
            4. Exit
            ------------------> """
            key = input(fields)
            match key:
                case "1":
                    id = input("ID book: ")
                    new_value = input("NEW value: ")
                    f = File("booksCRUD.csv", ["id", "name", "author", "category"])
                    books = f.read()
                    for i, book in enumerate(books):
                        if book.get("id") == id:
                            books[i]["name"] = new_value
                            break
                    f.clear()
                    for i in books:
                        f.write(i)
                    print("Book name updated ✅")
                    main()
                case "2":
                    id = input("ID book: ")
                    new_value = input("NEW value: ")
                    f = File("booksCRUD.csv", ["id", "name", "author", "category"])
                    books = f.read()
                    for i, book in enumerate(books):
                        if book.get("id") == id:
                            books[i]["author"] = new_value
                            break
                    f.clear()
                    for i in books:
                        f.write(i)
                    print("Book author successfully updated ✅")
                    main()
                case "3":
                    id = input("ID book: ")
                    new_value = input("NEW value: ")
                    f = File("booksCRUD.csv", ["id", "name", "author", "category"])
                    books = f.read()
                    for i, book in enumerate(books):
                        if book.get("id") == id:
                            books[i]["category"] = new_value
                            break
                    f.clear()
                    for i in books:
                        f.write(i)
                    print("Book category successfully updated ✅")
                    main()
                case "4":
                    main()
        case "3":
            id = input("ID: ")
            f = File("booksCRUD.csv", ["id", "name", "author", "category"])
            delete = f.read()
            for i, user in enumerate(delete):
                if user.get("id") == id:
                    del [i]
                    break
            f.delete(f)
            main()
        case "5":
            main()

main()
