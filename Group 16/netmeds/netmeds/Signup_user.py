import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class SignupPage:
    def __init__(self, master):
        self.master = master
        master.geometry("1100x700")
        master.title('SIGNUP')

        self.toolbar = tk.Frame(master, bg='TEAL', bd=5)
        self.new_button = tk.Button(self.toolbar, text='BACK', bg='White', fg='Teal', height=1, width=10, font="times 12 bold",command=self.back)
        self.new_button.pack(side=tk.RIGHT, padx=5, pady=50)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        self.toolbar = tk.Frame(master, bg='silver', bd=5)
        self.new_button = tk.Button(self.toolbar, text='PROFILE', bg='White', fg='Teal', height=1, width=10, font="times 12 bold")
        self.new_button.pack(side=tk.LEFT, padx=100, pady=250)
        self.toolbar.pack(pady=50, fill=tk.X)

        self.login_label = Label(master, text="SIGNUP - User", font="times 50 bold", foreground="White", bg='TEAL')
        self.login_label.place(x=300, y=25)

        self.Create = Label(master, text="CREATE ACCOUNT", font="MSSerif 20 bold", foreground="black")
        self.Create.place(x=400, y=150)

        self.email = Label(master, text="Email ID :", font="MSSerif 15", foreground="TEAL", background='silver')
        self.email.place(x=400, y=220)

        self.email_var = StringVar()
        self.email_entry = Entry(master, textvariable=self.email_var, font="times 20", foreground="Black")
        self.email_entry.place(x=400, y=250)

        self.Name = Label(master, text="Enter Name :", font="MSSerif 15", foreground="TEAL", background='silver')
        self.Name.place(x=400, y=300)

        self.name_var = StringVar()
        self.name_entry = Entry(master, textvariable=self.name_var, font="times 20", foreground="Black")
        self.name_entry.place(x=400, y=330)

        self.passw = Label(master, text="Enter Password :", font="MSSerif 15", foreground="TEAL", background='silver')
        self.passw.place(x=400, y=380)

        self.passw_var = StringVar()
        self.passw_entry = Entry(master, textvariable=self.passw_var, font="times 20", foreground="Black", show='*')
        self.passw_entry.place(x=400, y=410)

        self.phone = Label(master, text="Enter Phone no :", font="MSSerif 15", foreground="TEAL", background='silver')
        self.phone.place(x=400, y=460)

        self.phone_var = StringVar()
        self.phone_entry = Entry(master, textvariable=self.phone_var, font="times 20", foreground="Black")
        self.phone_entry.place(x=400, y=490)

        self.Signupbtn = Button(master, text="Create Account", foreground="WHITE", background="purple", font="times 20 bold", bg='TEAL', command=self.create_account)
        self.Signupbtn.place(x=430, y=550)



    def create_account(self):
        # Retrieve user input
        email = self.email_var.get()
        name = self.name_var.get()
        password = self.passw_var.get()
        phone = self.phone_var.get()

        # Connect to the database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mane2004@",
            database="hospital"
        )

        # Create a cursor object
        mycursor = mydb.cursor()

        # Insert user data into the database
        sql = "INSERT INTO signup_user (email, name, pass, phone) VALUES (%s, %s, %s, %s)"
        val = (email, name, password, phone)
        mycursor.execute(sql, val)

        # Commit the transaction
        mydb.commit()

        # Display a success message
        messagebox.showinfo("Success", "Account created successfully!")

    def back(self):
        self.master.destroy()
        from Login import Loginhome
        app = Loginhome()


root = tk.Tk()
app = SignupPage(root)
root.mainloop()