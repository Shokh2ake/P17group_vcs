products = ["Iphone14", "Iphone13", "Iphone12", "Olma"]


def add(product_name):
    products.append(product_name)


def delete(index: int):
    products.pop(index)


def update(index, new_name):
    products[index] = new_name
    print(f"Successfully update: ")


def show():
    for index, product in enumerate(products):
        print(f"{index}) {product}")


def search():
    query = input("Maxsulot nomini kiriting: ")
    harflar = []
    for index, product in enumerate(products):
        if query.lower() in product.lower():
            harflar.append(index)

    if not harflar:
        print("Maxsulot topilmadi!")
    else:
        print("Topilgan maxsulotlar:")
        for index in harflar:
            print(f"{index}) {products[index]}")


def clear():
    products.clear()
    print(f"Barchma maxsulotlar o'chirildi {products}")


def main():
    while True:
        menu = """
            1) Add product
            2) Delete product
            3) Update product
            4) Show product
            5) Search
            6) Clear
            7) Exit
            >>>"""

        key: str = input(menu)
        if not (key.isdigit() and 1 <= int(key) <= 7):
            print("key invalit!")
            continue

        if key == "1":
            product_name = input("Product name: ")
            add(product_name)

        elif key == "2":
            show()
            index = int(input("Index: "))
            delete(index)

        elif key == "3":
            show()
            index = int(input("Index: "))
            new_valu = input("New name: ")
            update(index, new_valu)

        elif key == "4":
            show()
        elif key == "5":
            search()
        elif key == "6":
            clear()
        else:
            break


main()

# 1

# s = input("So'z kiriting: ").split()
# k = int(input("kiriting:"))
# print(s[:k])

# 2

# a = input("So'z kiriting: ")
# print(a * 2)

# 3

# num = []
# n = int(input("Nechta element kiritiasiz: "))
# for i in range(1, n+1):
#     num.append(int(input(f"{i}: ")))
#
# num1 = []
# for i in num:
#     num1.append(num[i])
# print(num1)

# 4
#
# words = ["qwe", "asd", "edxc", "qaz"]
# num = []
#
# for i in words:
#     s = 0
#     for j in i:
#         if not j in "aeuio1234567890":
#             s += 1
#     num.append(s)
# print(num)

# 5
#
# a = input("So'z kiriting: ")
# print(a.count("."))









