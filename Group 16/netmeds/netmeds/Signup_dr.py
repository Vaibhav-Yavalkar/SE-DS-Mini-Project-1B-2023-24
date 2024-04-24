import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import subprocess
import mysql.connector

class SignupApp:
    def __init__(self, master):
        self.master = master
        master.geometry("1100x800")
        master.title('SIGNUP')

        self.toolbar = Frame(master, bg='TEAL', bd=5)
        self.toolbar.pack(side=TOP, fill=X)

        self.new_button = Button(self.toolbar, text='BACK', bg='White', fg='Teal', height=1, width=10, font="times 12 bold", command=self.open_LOGIN_PAGE)
        self.new_button.pack(side=RIGHT, padx=5, pady=50)

        self.toolbar2 = Frame(master, bg='silver', bd=5)
        self.toolbar2.pack(pady=50, fill=X)

        self.new_button2 = Button(self.toolbar2, text='PROFILE', bg='White', fg='Teal', height=1, width=10, font="times 12 bold")
        self.new_button2.pack(side=LEFT, padx=100, pady=300)

        self.login_label = Label(master, text="SIGNUP", font="times 50 bold", foreground="White", bg='TEAL')
        self.login_label.place(x=400, y=25)

        self.create_label = Label(master, text="CREATE  ACCOUNT", font="MSSerif 20 bold ", foreground="black")
        self.create_label.place(x=400, y=150)

        self.email_label = Label(master, text=" Email ID :", font="MSSerif 15 ", foreground="TEAL", background='silver')
        self.email_label.place(x=100, y=200)

        self.email_var = StringVar()
        self.email_entry = Entry(master, textvariable=self.email_var, font="times 20 ", foreground="Black")
        self.email_entry.place(x=100, y=230)

        self.name_label = Label(master, text=" Name :", font="MSSerif 15 ", foreground="TEAL", background='silver')
        self.name_label.place(x=100, y=280)

        self.name_var = StringVar()
        self.name_entry = Entry(master, textvariable=self.name_var, font="times 20 ", foreground="Black")
        self.name_entry.place(x=100, y=310)

        self.passw_label = Label(master, text="Set Password :", font="MSSerif 15 ", foreground="TEAL", background='silver')
        self.passw_label.place(x=100, y=360)

        self.passw_var = StringVar()
        self.passw_entry = Entry(master, textvariable=self.passw_var, font="times 20 ", foreground="Black", show='*')
        self.passw_entry.place(x=100, y=390)

        self.phone_label = Label(master, text=" Phone no :", font="MSSerif 15 ", foreground="TEAL", background='silver')
        self.phone_label.place(x=100, y=440)

        self.phone_var = StringVar()
        self.phone_entry = Entry(master, textvariable=self.phone_var, font="times 20 ", foreground="Black")
        self.phone_entry.place(x=100, y=470)

        self.specialization_label = Label(master, text=" Specialization  :", font="MSSerif 15 ", foreground="TEAL", background='silver')
        self.specialization_label.place(x=100, y=520)

        self.specialization_var = StringVar()
        self.specialization_entry = Entry(master, textvariable=self.specialization_var, font="times 20 ", foreground="Black")
        self.specialization_entry.place(x=100, y=550)

        self.Experience_label = Label(master, text=" Experience  :", font="MSSerif 15 ", foreground="TEAL", background='silver')
        self.Experience_label.place(x=500, y=200)
        self.Experience_var = StringVar()
        self.Experience_entry = Entry(master, textvariable=self.Experience_var, font="times 20 ", foreground="Black")
        self.Experience_entry.place(x=500, y=230)

        self.medical_license_number_label = Label(master, text=" Medical license number  :", font="MSSerif 15 ", foreground="TEAL", background='silver')
        self.medical_license_number_label.place(x=500, y=280)
        self.medical_license_number_var = StringVar()
        self.medical_license_number_entry = Entry(master, textvariable=self.medical_license_number_var, font="times 20 ", foreground="Black")
        self.medical_license_number_entry.place(x=500, y=310)

        self.Affiliations_label = Label(master, text="Professional Affiliations :", font="MSSerif 15 ", foreground="TEAL", background='silver')
        self.Affiliations_label.place(x=500, y=360)
        self.Affiliations_var = StringVar()
        self.Affiliations_entry = Entry(master, textvariable=self.Affiliations_var, font="times 20 ", foreground="Black")
        self.Affiliations_entry.place(x=500, y=390)

        self.Hospi_name_label = Label(master, text="Hospital/Clinic Name :", font="MSSerif 15 ", foreground="TEAL", background='silver')
        self.Hospi_name_label.place(x=500, y=440)
        self.Hospi_name_var = StringVar()
        self.Hospi_name_entry = Entry(master, textvariable=self.Hospi_name_var, font="times 20 ", foreground="Black")
        self.Hospi_name_entry.place(x=500, y=470)

        self.Certifications_label = Label(master, text="Certifications :", font="MSSerif 15 ", foreground="TEAL", background='silver')
        self.Certifications_label.place(x=500, y=520)
        self.Certifications_var = StringVar()
        self.Certifications_entry = Entry(master, textvariable=self.Certifications_var, font="times 20 ", foreground="Black")
        self.Certifications_entry.place(x=500, y=550)

        self.Signupbtn = Button(master, text="Create Account", foreground="WHITE", background="purple", font="times 15", bg='TEAL', command=self.create_account)
        self.Signupbtn.place(x=400, y=655)

    def create_account(self):
        # Retrieve user input
        email = self.email_var.get()
        name = self.name_var.get()
        passw = self.passw_var.get()
        phone = self.phone_var.get()
        special = self.specialization_var.get()
        exp = self.Experience_var.get()
        lic = self.medical_license_number_var.get()
        affil = self.Affiliations_var.get()
        hosname = self.Hospi_name_var.get()
        certi = self.Certifications_var.get()

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
        sql = "INSERT INTO signup_dr (email, name, pass, phone,special,exp,licence,affil,hospname,certi) VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s)"
        val = (email, name, passw, phone, special, exp, lic, affil, hosname, certi)
        mycursor.execute(sql, val)

        # Commit the transaction
        mydb.commit()

        # Display a success message
        messagebox.showinfo("Success", "Account created successfully!")

    def open_LOGIN_PAGE(self):
        self.master.destroy()
        subprocess.Popen(["python", "login.py"])


def main():
    root = Tk()
    app = SignupApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
