import random
from tkinter import *

from modul_3.lesson_4.auth_.main import User


def random_card_number():
    codes = ["9860", "8600", "6262", "5656", "6767", "5555"]
    return f"{random.choice(codes)}{str(random.randint(1, 10000)).zfill(4)}{str(random.randint(1, 10000)).zfill(4)}{str(random.randint(1, 10000)).zfill(4)}"


class UI:
    win = Tk()

    def show_card_number(self):
        self.win.destroy()
        self.win = Tk()
        self.win.geometry("800x500")

        Label(self.win, text=f"Your card number: {self.card_number}", font=(None, 20, "bold")).pack(expand=True)
        Button(self.win, text="OKEY", bg="green", command=self.back_main).pack(expand=True)
        self.win.mainloop()

    def approve_code_with_email(self):
        self.win.destroy()
        self.win = Tk()
        self.win.geometry("500x300")
        self.code = StringVar()

        Label(self.win, text="Email pochtaga yuborilghan code kiriting", font=(None, 20, "bold")).pack(expand=True)
        Entry(self.win, textvariable=self.code, font=(None, 15, "bold")).pack(expand=True)
        Button(self.win, text="OKEY", bg="green", command=self.show_card_number).pack(expand=True)
        self.win.mainloop()

    def register_submit(self):
        try:
            self.card_number = random_card_number()
            user = {
                "fullname": self.fullname.get(),
                "email": self.email.get(),
                "password": self.password.get(),
                "card_number": self.card_number,
                "balance": 50000
            }

            user = User(**user)
            user.create_id()
            user.is_valid()
            user.save()
            self.show_card_number()
        except Exception as e:
            Label(self.win, text=e, fg="red").place(x=250, y=0)

    def register(self):
        self.win.destroy()
        self.win = Tk()
        self.win.geometry("600x600")
        self.win.title("Register")
        self.fullname = StringVar()
        self.email = StringVar()
        self.password = StringVar()

        Label(self.win, text='REGISTER', font=(None, 30, "bold")).pack(expand=True)

        Label(self.win, text='Full Name', font=(None, 20, "bold")).pack(expand=True)
        Entry(self.win, textvariable=self.fullname, font=(None, 20, "bold")).pack(expand=True)
        Label(self.win, text='Email', font=(None, 20, "bold")).pack(expand=True)
        Entry(self.win, textvariable=self.email, font=(None, 20, "bold")).pack(expand=True)
        Label(self.win, text='Password', font=(None, 20, "bold")).pack(expand=True)
        Entry(self.win, textvariable=self.password, font=(None, 20, "bold")).pack(expand=True)
        Button(self.win, text="Submit", font=(None, 14, "bold"), bg="green", command=self.register_submit).pack(
            expand=True)

        self.win.mainloop()

    def login(self):
        self.win.destroy()
        self.win = Tk()
        self.win.geometry("500x500")
        self.win.title("Login")
        self.email = StringVar()
        self.password = StringVar()

        Label(self.win, text='Email', font=(None, 20, "bold")).pack(expand=True)
        Entry(self.win, textvariable=self.email, font=(None, 20, "bold")).pack(expand=True)
        Label(self.win, text='Password', font=(None, 20, "bold")).pack(expand=True)
        Entry(self.win, textvariable=self.password, font=(None, 20, "bold")).pack(expand=True)

        Button(self.win, text="Submit", font=(None, 14, "bold"), bg="green", command=self.register_submit).pack(
            expand=True)

        self.win.mainloop()

    def main(self):
        self.win.geometry("500x400")
        Label(self.win, text="BANKOMAT", font=(None, 25, "bold")).pack(pady=80)
        Button(self.win, text="Register", bg="green", font=(None, 14, "bold"), width=7, fg="white",
               command=self.register).place(x=180, y=150)
        Button(self.win, text="Login", bg="blue", font=(None, 14, "bold"), width=7, fg="white",
               command=self.login).place(x=180, y=200)
        Button(self.win, text="Exit", bg="red", font=(None, 14, "bold"), width=7, fg="white",
               command=lambda: self.win.destroy()).place(x=180, y=250)
        self.win.mainloop()

    def back_main(self):
        self.win.destroy()
        self.win = Tk()
        self.win.geometry("500x400")

        Label(self.win, text="BANKOMAT", font=(None, 25, "bold")).pack(pady=80)
        Button(self.win, text="Register", bg="green", font=(None, 14, "bold"), width=7, fg="white",
               command=self.register).place(x=180, y=150)
        Button(self.win, text="Login", bg="blue", font=(None, 14, "bold"), width=7, fg="white",
               command=self.login).place(x=180, y=200)
        Button(self.win, text="Exit", bg="red", font=(None, 14, "bold"), width=7, fg="white",
               command=lambda: self.win.destroy()).place(x=180, y=250)
        self.win.mainloop()


if __name__ == '__main__':
    UI().main()
