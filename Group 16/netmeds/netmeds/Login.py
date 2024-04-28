import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

class Loginhome(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1100x700")
        self.title('LOGIN')
        self.create_widgets()

    def open_new_page(self):
        try:
            self.destroy()
            from Medicine_Home import HomePage
            new_root = tk.Tk()
            app = HomePage(new_root)
            new_root.geometry("1100x600")
            new_root.title('NEW_PAGE')
            new_root.mainloop()
        except ImportError:
            print("Error importing HomePage from Medicine_Home")



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
        sql = "SELECT * FROM signup_user WHERE name = %s AND pass = %s"
        val = (username, password)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()

        if result:
            messagebox.showinfo("Success", "Login successful!")
            self.open_new_page()
        elif result is None:
            messagebox.showinfo("Error", "Please enter username or password")
        else:
            messagebox.showinfo("Error", "Invalid username or password!")

    def create_widgets(self):
        toolbar1 = Frame(self, bg='TEAL', bd=5)
        new_button = Button(toolbar1, text='BACK', bg='White', fg='Teal', height=1, width=10, font="times 12 bold",command=self.back)
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

        login_btn = Button(self, text="Login", foreground="WHITE", background="purple", font="times 18 bold ", bg='TEAL', command=self.login)
        login_btn.place(x=675, y=460)

        signup_btn = Button(self, text="Sign Up", foreground="WHITE", background="purple", font="times 18 bold", bg='TEAL',command=self.open_Signup_user)
        signup_btn.place(x=900, y=460)

        image_path = r"C:\New folder\pro\log.jpg"
        original_image = Image.open(image_path)
        resized_image = original_image.resize((455, 455), Image.BILINEAR)  # Resize image to 200x200
        self.tkinter_image = ImageTk.PhotoImage(resized_image)

        # Display resized image
        self.image_label = Label(self, image=self.tkinter_image)
        self.image_label.place(x=100, y=192)

        login_as = Label(self, text="------------------------------login as------------------------------", font="times 15 bold", foreground="black", background='silver')
        login_as.place(x=575, y=525)

        ADMIN = Button(self, text="ADMIN", foreground="WHITE", background="purple", font="times 16 bold", bg='TEAL',command=self.login_admin)
        ADMIN.place(x=660, y=575)

        DOCTOR = Button(self, text="DOCTOR", foreground="WHITE", background="purple", font="times 16 bold", bg='TEAL',command=self.login_dr)
        DOCTOR.place(x=795, y=575)

        LAB = Button(self, text="LAB", foreground="WHITE", background="purple", font="times 16 bold", bg='TEAL',command=self.lab)
        LAB.place(x=950, y=575)




    def back(self):
        self.destroy()

    def lab(self):
        try:
            self.destroy()
            from Login_lab import Loginlab
            #new_root = tk.Tk()
            app = Loginlab()
            #new_root.geometry("1100x600")
            #new_root.title('NEW_PAGE')
            new_root.mainloop()
        except ImportError:
            print("Error importing Loginlab from Login")
        except Exception as e:
            print("An error occurred:", str(e))

    def login_dr(self):
        self.destroy()
        from login_dr import Loginhomedr
        # new_root = tk.Tk()
        app = Loginhomedr()
        # new_root.geometry("1100x600")
        # new_root.title('NEW_PAGE')
        app.mainloop()

    def login_admin(self):
        self.destroy()
        from Login_admin import login_admin
        # new_root = tk.Tk()
        app = login_admin()
        # new_root.geometry("1100x600")
        # new_root.title('NEW_PAGE')

    def open_Signup_user(self):
        try:
            self.destroy()
            from Signup_user import SignupPage
            new_root = tk.Tk()
            app = SignupPage(new_root)
            new_root.geometry("1100x600")
            new_root.title('NEW_PAGE')
            new_root.mainloop()
        except ImportError:
            print("Error importing SignupPage from Signup_user")
        except Exception as e:
            print("An error occurred:", str(e))



if __name__ == "__main__":
    app = Loginhome()
    app.mainloop()
