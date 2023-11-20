Date = []
to_do = []


def delete_to_do(index):
    to_do.pop(index)


def add_to_do(title, day, time):
    to_do1 = []
    to_do1.append(title)
    to_do1.append(day)
    to_do1.append(time)
    to_do.append(to_do1)


def chek_email(email):
    for i in Date:
        if i.get("email") == email:
            return False
    return True


def Register(user: dict):
    Date.append(user)


def Login(login, password):
    for i in Date:
        if i.get("Email") == login and i.get("Pasword") == password:
            break
        else:
            print("account not found ")
            return
    a = True
    while a:
        menu = """
        1 : add to do 
        2 : delete to do 
        3 : update to do 
        4 : to do list 
        5 : log out 
        >>>"""

        key = input(menu)

        if not key.isdigit() or not 1 <= int(key) <= 5:
            print(" Wrong buutom ")
            continue

        if key == "1":
            print(" add Title = ")
            title = input(">>")
            print("add day =  ")
            day = input(">>")
            print("add time  =  ")
            time = input(">>")
            add_to_do(title, day, time)

        elif key == "2":
            for index, do in enumerate(to_do):
                print(f"{index + 1} : ish")
                print(f" {' '.join(do)} ")
                print("Enter ish id ")


        elif key == "3":
            pass

        elif key == "4":

            for index, do in enumerate(to_do):
                print(f"{index + 1} : ish")
                print(f" {' '.join(do)} ")


        elif key == "5":
            a = False


while True:

    main = """
        1. Register
        2. login
        3. Exit
        4. Data
     Enter The buutom  >>> """

    key = input(main)

    if not key.isdigit() or not 1 <= int(key) <= 5:
        print(" Wrong buutom ")
        continue

    if key == "1":

        user = {
            "Name": input("Name >>>"),
            "Surname": input("Surname >>>"),
            "Age": input("Age >>>"),
            "Email": input("Email Adres >>>"),
            "Pasword": input("Pasword >>>")
        }

        Register(user)

        isvalid = chek_email(user.get("email"))
        if isvalid:
            Register(user)
        else:
            print("Already email exists !")
            continue




    elif key == "2":
        print("Enter The Email Adrees >> ")
        login = input(" ")
        print("Enter The Psword Adrees >> ")
        password = input(" ")
        Login(login, password)

    elif key == "3":
        print(" THANK YOU FOR  USING  TO DO PLATFORM ! ")
        break
    elif key == "4":
        print(Date)
