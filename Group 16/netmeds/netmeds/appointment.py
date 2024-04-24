import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

class HospitalManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x700")
        self.root.title('LOGIN')

        self.create_toolbar()
        self.create_labels_buttons()
        self.create_treeview()

    def create_toolbar(self):
        toolbar = Frame(self.root, bg='TEAL', bd=5)
        new_button = Button(toolbar, text='BACK', bg='White', fg='Teal', height=1, width=10, font="times 12 bold",command=self.back)
        new_button.pack(side=RIGHT, padx=5, pady=50)
        toolbar.pack(side=TOP, fill=X)

    def create_labels_buttons(self):
        Appointment = Label(self.root, text="Dr's Appointment and patient details", font="times 25 bold", foreground="White", bg='TEAL')
        Appointment.place(x=300, y=35)

        patient = Label(self.root, text=" Patient's detail :", font="times 20 bold", foreground="Teal")
        patient.place(x=50, y=150)

        appoint = Label(self.root, text=" Appointment details :", font="times 20 bold", foreground="Teal")
        appoint.place(x=50, y=380)

        appoint = Label(self.root, text=" Doctor Name :", font="times 15 bold", foreground="Teal")
        appoint.place(x=450, y=400)

        self.name_var = StringVar()
        name_entry = Entry(self.root, textvariable=self.name_var, font="times 15 ", foreground="Black", width=20)
        name_entry.place(x=600, y=400)



        show = Button(self.root, text="SHOW", foreground="WHITE", background="purple", font="times 10 bold", bg='TEAL',
                      width=10, command=self.fetch_data)
        show.place(x=500, y=360)

        show2 = Button(self.root, text="SHOW", foreground="WHITE", background="purple", font="times 10 bold", bg='TEAL',
                      width=10, command=self.fetch_data2)
        show2.place(x=500, y=600)

    def create_treeview(self):
        self.doctors_tree = ttk.Treeview(self.root, columns=(
            "name", "medical_history", "address", "blood_group", "gender", "age", "height", "weight"), show="headings")

        self.doctors_tree.heading("name", text="Name")
        self.doctors_tree.heading("medical_history", text="Medical History")
        self.doctors_tree.heading("address", text="Address")
        self.doctors_tree.heading("blood_group", text="Blood Group")
        self.doctors_tree.heading("gender", text="Gender")
        self.doctors_tree.heading("age", text="Age")
        self.doctors_tree.heading("height", text="Height")
        self.doctors_tree.heading("weight", text="Weight")

        self.doctors_tree.column("name", width=100)
        self.doctors_tree.column("medical_history", width=150)
        self.doctors_tree.column("address", width=100)
        self.doctors_tree.column("blood_group", width=80)
        self.doctors_tree.column("gender", width=80)
        self.doctors_tree.column("age", width=50)
        self.doctors_tree.column("height", width=50)
        self.doctors_tree.column("weight", width=50)

        self.doctors_tree.place(x=50, y=200, height=150, width=1000)

        self.doctor_tree = ttk.Treeview(self.root, columns=(
            "name", "time", "date", "phone", "gender","doctor_name"), show="headings")

        self.doctor_tree.heading("name", text="Name")
        self.doctor_tree.heading("time", text="Time")
        self.doctor_tree.heading("date", text="Date")
        self.doctor_tree.heading("phone", text="Phone")
        self.doctor_tree.heading("gender", text="Gender")
        self.doctor_tree.heading("doctor_name", text="Doctor's Name")

        self.doctor_tree.column("name", width=100)

        self.doctor_tree.column("time", width=100)
        self.doctor_tree.column("date", width=100)
        self.doctor_tree.column("phone", width=100)
        self.doctor_tree.column("gender", width=100)
        self.doctor_tree.column("doctor_name", width=150)

        self.doctor_tree.place(x=50, y=430, height=150, width=1000)

    def fetch_data(self):
        try:
            # Connect to the database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Mane2004@",  # Enter your MySQL password here
                database="hospital"
            )

            # Create a cursor object
            mycursor = mydb.cursor()

            # Execute the SQL query to fetch data
            mycursor.execute("SELECT * FROM profile_user")  # Replace 'your_table' with your actual table name

            # Fetch all rows from the result
            rows = mycursor.fetchall()

            # Clear the treeview
            for record in self.doctors_tree.get_children():
                self.doctors_tree.delete(record)

            # Insert fetched data into the treeview
            for row in rows:
                self.doctors_tree.insert('', 'end', values=row)
        except mysql.connector.Error as error:
            print("Failed to fetch data from MySQL table:", error)
        finally:
            # Close the database connection
            if mydb.is_connected():
                mycursor.close()
                mydb.close()

    def fetch_data2(self):
        try:
            # Connect to the database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Mane2004@",  # Enter your MySQL password here
                database="hospital"
            )

            # Create a cursor object
            mycursor = mydb.cursor()

            # Get the doctor's name entered in the Entry widget
            doctor_name = self.name_var.get()

            # Execute the SQL query to fetch data for appointments with the specified doctor's name
            query = "SELECT * FROM dr_appoint WHERE doctor_name = %s"
            mycursor.execute(query, (doctor_name,))

            # Fetch all rows from the result
            rows = mycursor.fetchall()

            # Clear the treeview
            for record in self.doctor_tree.get_children():
                self.doctor_tree.delete(record)

            # Insert fetched data into the treeview
            for row in rows:
                self.doctor_tree.insert('', 'end', values=row)
        except mysql.connector.Error as error:
            print("Failed to fetch data from MySQL table:", error)
        finally:
            # Close the database connection
            if mydb.is_connected():
                mycursor.close()
                mydb.close()

    def back(self):
        self.root.destroy()
        from login_dr import Loginhomedr
        #new_root = tk.Tk()
        app = Loginhomedr()
        #new_root.geometry("1100x600")
        #new_root.title('NEW_PAGE')
        new_root.mainloop()

if __name__ == "__main__":
    root = Tk()
    app = HospitalManagementSystem(root)
    root.mainloop()
