import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector

class lab_appointment:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x700")
        self.root.title('LOGIN')

        self.create_toolbar()
        self.create_labels_buttons()
        self.create_treeviews()
        # Create new tables in the database
        self.create_new_tables()

    def create_toolbar(self):
        toolbar = Frame(self.root, bg='TEAL', bd=5)
        new_button = Button(toolbar, text='BACK', bg='White', fg='Teal', height=1, width=10, font="times 12 bold",command=self.back)
        new_button.pack(side=RIGHT, padx=5, pady=50)
        toolbar.pack(side=TOP, fill=X)

    def create_labels_buttons(self):
        Appointment = Label(self.root, text="Patient's appointment & patients details", font="times 30 bold", foreground="White", bg='TEAL')
        Appointment.place(x=225, y=30)

        Appointment2 = Label(self.root, text="patients  details :", font="times 20 bold", foreground="teal")
        Appointment2.place(x=50, y=390)

        lab = Label(self.root, text="Lab Appointment details :", font="times 20 bold", foreground="teal")
        lab.place(x=50, y=150)

        show = Button(self.root, text="SHOW", foreground="WHITE", background="purple", font="times 10 bold", bg='TEAL',
                      width=10, command=self.fetch_lab_data)
        show.place(x=500, y=365)

        show2 = Button(self.root, text="SHOW", foreground="WHITE", background="purple", font="times 10 bold", bg='TEAL',
                      width=10, command=self.fetch_lab_data2)
        show2.place(x=500, y=625)

    def create_treeviews(self):
        self.lab_tree = ttk.Treeview(self.root, columns=(
            "Name", "phone", "medihistory", "address", "test", "package", "time", "Date"), show="headings")

        self.lab_tree.heading("Name", text="Name")
        self.lab_tree.heading("phone", text="phone")
        self.lab_tree.heading("medihistory", text="medihistory")
        self.lab_tree.heading("address", text="address")
        self.lab_tree.heading("test", text="test")
        self.lab_tree.heading("package", text="package")
        self.lab_tree.heading("time", text="time")
        self.lab_tree.heading("Date", text="Date")

        self.lab_tree.column("Name", width=100)
        self.lab_tree.column("phone", width=50)
        self.lab_tree.column("medihistory", width=80)
        self.lab_tree.column("address", width=80)
        self.lab_tree.column("test", width=150)
        self.lab_tree.column("package", width=80)
        self.lab_tree.column("time", width=80)
        self.lab_tree.column("Date", width=100)

        self.lab_tree.place(x=50, y=200, height=150, width=1000)

        self.doctor_tree = ttk.Treeview(self.root, columns=(
            "name", "medihistory", "address", "blood_group", "gender", "age", "height", "weight",), show="headings")

        self.doctor_tree.heading("name", text="Name")
        self.doctor_tree.heading("medihistory", text="medihistory")
        self.doctor_tree.heading("address", text="Address")  # Add this line for the address column
        self.doctor_tree.heading("blood_group", text="blood_group")
        self.doctor_tree.heading("gender", text="gender")
        self.doctor_tree.heading("age", text="age")
        self.doctor_tree.heading("height", text="height")
        self.doctor_tree.heading("weight", text="weight")

        self.doctor_tree.column("name", width=100)
        self.doctor_tree.column("medihistory", width=100)
        self.doctor_tree.column("address", width=100)
        self.doctor_tree.column("blood_group", width=100)
        self.doctor_tree.column("gender", width=100)
        self.doctor_tree.column("age", width=100)
        self.doctor_tree.column("height", width=100)
        self.doctor_tree.column("weight", width=100)





        self.doctor_tree.place(x=50, y=450, height=150, width=1000)

    def create_new_tables(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Mane2004@",
                database="hospital"
            )

            mycursor = mydb.cursor()

            # Create a new table for lab appointments with the specified columns
            mycursor.execute("CREATE TABLE IF NOT EXISTS lab (Name VARCHAR(255), phone VARCHAR(20), medihistory VARCHAR(255), address VARCHAR(255), test VARCHAR(255), package VARCHAR(255), time VARCHAR(255), Date VARCHAR(255))")

            # Create a new table for doctor appointments with the specified columns
            mycursor.execute("CREATE TABLE IF NOT EXISTS doctors (name VARCHAR(255), email VARCHAR(255), phone VARCHAR(20), specialization VARCHAR(255), experience INT, medical_license VARCHAR(255), clinic_name VARCHAR(255))")

            mydb.commit()
        except mysql.connector.Error as error:
            print("Failed to create new tables:", error)
        finally:
            if mydb.is_connected():
                mycursor.close()
                mydb.close()

    def fetch_lab_data(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Mane2004@",
                database="hospital"
            )

            mycursor = mydb.cursor()

            mycursor.execute("SELECT * FROM lab")

            rows = mycursor.fetchall()

            for record in self.lab_tree.get_children():
                self.lab_tree.delete(record)

            for row in rows:
                self.lab_tree.insert('', 'end', values=row)
        except mysql.connector.Error as error:
            print("Failed to fetch lab data from MySQL table:", error)
        finally:
            if mydb.is_connected():
                mycursor.close()
                mydb.close()

    def fetch_lab_data2(self):  # Corrected indentation and method name
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Mane2004@",
                database="hospital"
            )

            mycursor = mydb.cursor()

            mycursor.execute("SELECT * FROM profile_user")

            rows = mycursor.fetchall()

            for record in self.doctor_tree.get_children():  # Changed treeview name
                self.doctor_tree.delete(record)

            for row in rows:
                self.doctor_tree.insert('', 'end', values=row)
        except mysql.connector.Error as error:
            print("Failed to fetch lab data from MySQL table:", error)
        finally:
            if mydb.is_connected():
                mycursor.close()
                mydb.close()


    def back(self):
        self.root.destroy()
        from Login_admin import login_admin
        #new_root = tk.Tk()
        app = login_admin()
        #new_root.geometry("1100x600")
        #new_root.title('NEW_PAGE')
        new_root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = lab_appointment(root)
    root.mainloop()
