from tkinter import *

users: list[dict] = []


def add_user():
    user = {
        "fullname": fullname.get(),
        "username": username.get(),
        "password": password.get(),
    }
    fullname.set("")
    username.set("")
    password.set("")
    users.append(user)
    Label(register_win, text="Successfully register", bg="green").pack()


def account():
    screen.destroy()
    account_win = Tk()
    account_win.geometry("500x500")
    account_win.title("Account")
    Label(account_win, text="WELCOME !", font=(None, 30)).pack()


def check_login():
    for user in users:
        if user.get("username") == login_username.get() and user.get("password") == login_password.get():
            account()
            return
    Label(login_win, text="Not Found Account", fg="red", font=(None, 30)).pack()


def register():
    global fullname, username, password, register_win
    register_win = Toplevel(screen)
    register_win.geometry("500x500")
    register_win.title("Register")
    fullname = StringVar()
    username = StringVar()
    password = StringVar()

    Label(register_win, text="Fullname *", font=(None, 15)).pack(pady=20)
    Entry(register_win, textvariable=fullname, width=20).pack()
    Label(register_win, text="Username *", font=(None, 15)).pack(pady=20)
    Entry(register_win, textvariable=username, width=20).pack()
    Label(register_win, text="Password *", font=(None, 15)).pack(pady=20)
    Entry(register_win, textvariable=password, show="*", width=20).pack()
    Button(register_win, text="Register", width=10, height=1, command=add_user).pack(pady=20)


def login():
    global login_username, login_password, login_win
    login_win = Toplevel(screen)
    login_win.geometry("500x500")
    login_win.title("Login")
    login_username = StringVar()
    login_password = StringVar()

    Label(login_win, text="Username *", font=(None, 15)).pack(pady=20)
    Entry(login_win, textvariable=login_username, width=20).pack()
    Label(login_win, text="Password *", font=(None, 15)).pack(pady=20)
    Entry(login_win, textvariable=login_password, width=20).pack()
    Button(login_win, text="Login", width=10, height=1, command=check_login).pack(pady=20)


def show_user():
    show_win = Toplevel(screen)
    for i in users:
        Label(show_win, text=f"{i}").pack()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x300")
    screen.title("My screen")
    Button(screen, text="Register", width=10, height=1, command=register).pack(pady=40)
    Button(screen, text="Login", width=10, height=1, command=login).pack()
    Button(screen, text="Users", width=10, height=1, command=show_user).pack()
    screen.mainloop()


main_screen()