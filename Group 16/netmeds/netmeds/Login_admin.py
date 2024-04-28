import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

class login_admin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1100x700")
        self.title('LOGIN')
        self.create_widgets()

    def admin_page(self):
        self.destroy()
        from admin import lab_appointment
        new_root = tk.Tk()
        app = lab_appointment(new_root)  # Pass the root argument here
        new_root.geometry("1100x600")
        new_root.title('NEW_PAGE')
        new_root.mainloop()

    def login(self):
        # Connect to the database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mane2004@",
            database="hospital"
        )

        mycursor = mydb.cursor()

        # Retrieve username and password from entry fields
        username = self.user_value.get()
        password = self.password_value.get()

        # Query to check if the username and password exist in the database
        sql = "SELECT * FROM login_admin WHERE username = %s AND password = %s"
        val = (username, password)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()

        if result:
            messagebox.showinfo("Success", "Login successful!")
            self.admin_page()
        elif result is None:
            messagebox.showinfo("Error", "Please enter username or password")
        else:
            messagebox.showinfo("Error", "Invalid username or password!")

    def create_widgets(self):
        toolbar1 = Frame(self, bg='TEAL', bd=5)
        new_button = Button(toolbar1, text='BACK', bg='White', fg='Teal', height=1, width=10, font="times 12 bold")
        new_button.pack(side=RIGHT, padx=5000, pady=50)
        toolbar1.pack(side=TOP, fill=X)

        toolbar2 = Frame(self, bg='silver', bd=5)
        new_button = Button(toolbar2, text='PROFILE', bg='White', fg='Teal', height=1, width=10, font="times 12 bold")
        new_button.pack(side=LEFT, padx=100, pady=250)
        toolbar2.pack(pady=50, fill=X)

        login_label = Label(self, text="Quickmeds ", font="times 50 bold", foreground="White", bg='TEAL')
        login_label.place(x=400, y=25)

        user_label = Label(self, text="UserName :", font="times 25 bold", foreground="black", background='silver')
        user_label.place(x=675, y=250)
        self.user_value = StringVar()
        user_entry = Entry(self, textvariable=self.user_value, font="times 20 ", foreground="Black",width=23)
        user_entry.place(x=675, y=300)

        password_label = Label(self, text="Password :", font="times 25 bold", foreground="black", background='silver')
        password_label.place(x=675, y=350)
        self.password_value = StringVar()
        password_entry = Entry(self, textvariable=self.password_value, font="times 20 ", foreground="Black", show="*",width=23)
        password_entry.place(x=675, y=400)

        admin = Label(self, text="ADMIN Login ", font="times 25 bold", foreground="black")
        admin.place(x=725, y=150)

        login_btn = Button(self, text="Back", foreground="Teal", background="purple", font="times 18 bold ", bg='White', command=self.back)
        login_btn.place(x=1000, y=50)

        login_btn = Button(self, text="Login", foreground="WHITE", background="purple", font="times 18 bold ", bg='TEAL', command=self.login)
        login_btn.place(x=800, y=460)



        # Load and resize the other image
        other_image_path = r"C:\New folder\pro\admin.jpg"
        original_other_image = Image.open(other_image_path)
        resized_other_image = original_other_image.resize((455, 455), Image.BILINEAR)
        self.other_image = ImageTk.PhotoImage(resized_other_image)

        # Display resized other image
        self.other_image_label = Label(self, image=self.other_image)
        self.other_image_label.place(x=100, y=192)

    def back(self):
        self.destroy()
        from Login import Loginhome
        #new_root = tk.Tk()
        app = Loginhome()
        #new_root.geometry("1100x600")
        #new_root.title('NEW_PAGE')
        new_root.mainloop()


if __name__ == "__main__":
    app = login_admin()
    app.mainloop()
