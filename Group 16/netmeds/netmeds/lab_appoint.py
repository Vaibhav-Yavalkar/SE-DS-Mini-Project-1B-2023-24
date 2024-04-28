import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

class lab_appointment:
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
        Appointment = Label(self.root, text="Patient's Health Package details", font="times 30 bold", foreground="White", bg='TEAL')
        Appointment.place(x=275, y=45)

        show = Button(self.root, text="SHOW", foreground="WHITE", background="purple", font="times 15 bold", bg='TEAL',
                      width=10, command=self.fetch_data)
        show.place(x=500, y=600)

    def create_treeview(self):
        self.doctors_tree = ttk.Treeview(self.root, columns=(
            "Name", "phone", "medihistory", "address", "test", "package", "time", "Date"), show="headings")

        self.doctors_tree.heading("Name", text="Name")
        self.doctors_tree.heading("phone", text="phone")
        self.doctors_tree.heading("medihistory", text="medihistory")
        self.doctors_tree.heading("address", text="address")
        self.doctors_tree.heading("test", text="test")
        self.doctors_tree.heading("package", text="package")
        self.doctors_tree.heading("time", text="time")  # Removed extra space
        self.doctors_tree.heading("Date", text="Date")

        self.doctors_tree.column("Name", width=100)
        self.doctors_tree.column("phone", width=50)
        self.doctors_tree.column("medihistory", width=80)
        self.doctors_tree.column("address", width=80)
        self.doctors_tree.column("test", width=150)
        self.doctors_tree.column("package", width=80)
        self.doctors_tree.column("time", width=80)
        self.doctors_tree.column("Date", width=100)

        self.doctors_tree.place(x=50, y=200, height=300, width=1000)

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
            mycursor.execute("SELECT * FROM lab")  # Replace 'your_table' with your actual table name

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

    def back(self):
        self.root.destroy()  # Destroy the main window
        from Login_lab import Loginlab
        #new_root = tk.Tk()
        app = Loginlab()  # Remove the 'new_root' argument here
        #new_root.geometry("1100x600")
        #new_root.title('NEW_PAGE')
        new_root.mainloop()


if __name__ == "__main__":
    root = Tk()
    app = lab_appointment(root)
    root.mainloop()
