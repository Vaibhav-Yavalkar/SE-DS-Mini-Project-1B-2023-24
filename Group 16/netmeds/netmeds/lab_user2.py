import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry  # Import DateEntry from tkcalendar module for date picker
import mysql.connector


class LabTestPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1100x700")
        self.title('LOGIN')

        toolbar = tk.Frame(self, bg='TEAL', bd=5)
        new_button = tk.Button(toolbar, text='BACK', bg='White', fg='Teal', height=1, width=10, font="times 12 bold",
                               command=self.back)
        new_button.pack(side=tk.RIGHT, padx=5, pady=50)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        toolbar = tk.Frame(self, bg='silver', bd=5)
        new_button = tk.Button(toolbar, text='PROFILE', bg='White', fg='Teal', height=1, width=10, font="times 12 bold")
        new_button.pack(side=tk.LEFT, padx=100, pady=250)
        toolbar.pack(pady=50, fill=tk.X)

        login_label = tk.Label(self, text="LAB TEST", font="times 50 bold", foreground="White", bg='TEAL')
        login_label.place(x=400, y=5)

        Create = tk.Label(self, text="Please fill in your details :", font="MSSerif 15  ", foreground="black")
        Create.place(x=250, y=150)

        Name = tk.Label(self, text="Enter Name :", font="MSSerif 15 bold", foreground="TEAL", background='Silver')
        Name.place(x=250, y=200)

        self.name_var = StringVar()
        name_entry = Entry(self, textvariable=self.name_var, font="times 15 ", foreground="Black", width=28)
        name_entry.place(x=250, y=230)

        phone = tk.Label(self, text="Enter Phone no :", font="MSSerif 15 bold ", foreground="TEAL", background='Silver')
        phone.place(x=250, y=280)

        self.passw_var = StringVar()
        passw_entry = Entry(self, textvariable=self.passw_var, font="times 15 ", foreground="Black")
        passw_entry.place(x=250, y=310, height=35, width=285)

        disease = tk.Label(self, text="Medical History if any:", font="MSSerif 15 bold", foreground="TEAL",
                           background='Silver')
        disease.place(x=250, y=360)
        self.disease_text = Text(self, height=3, width=28, font="times 15 ", foreground="Black")
        self.disease_text.place(x=250, y=390)

        address = tk.Label(self, text="Address:", font="MSSerif 15 bold", foreground="TEAL", background='Silver')
        address.place(x=250, y=470)
        self.address_text = Text(self, height=3, width=28, font="times 15 ", foreground="Black")
        self.address_text.place(x=250, y=500)

        select = tk.Label(self, text="Select Package and Test :", font="MSSerif 15  ", foreground="black")
        select.place(x=650, y=150)

        Test = tk.Label(self, text="Choose Test :", font="MSSerif 15 bold", foreground="TEAL", background='Silver')
        Test.place(x=650, y=200)

        options = ['Diabetes', 'Kidney', 'Thyroid', 'Dengue', 'Covid-19', 'Cardiac Arrest', 'X-ray', 'MRI CT Scan',
                   'Vitamin', 'Calcium', 'iron Defiency', 'Testosterone', 'complete urine routine']
        self.test_combo = ttk.Combobox(self, values=options, font="times 12 ", width=25)
        self.test_combo.place(x=650, y=230)

        package = tk.Label(self, text="Choose Package :", font="MSSerif 15 bold", foreground="TEAL",
                           background='Silver')
        package.place(x=650, y=280)

        options = ['Woman Health', 'Senior Citizen', 'Full Body Checkup', 'Basic Allergy Package', 'Immunity Care',
                   'Male Package', 'Childrens Checkup']
        self.package_combo = ttk.Combobox(self, values=options, font="times 12 ", width=25)
        self.package_combo.place(x=650, y=310)

        Time = tk.Label(self, text="Enter Time :", font="MSSerif 15 bold", foreground="TEAL", background='Silver')
        Time.place(x=650, y=360)

        # Hour Combobox
        self.hour_var = StringVar()
        hour_combo = ttk.Combobox(self, values=[str(i).zfill(2) for i in range(1, 13)], textvariable=self.hour_var,
                                  font="times 12", width=3)
        hour_combo.place(x=650, y=390)

        # Minute Combobox
        self.minute_var = StringVar()
        minute_combo = ttk.Combobox(self, values=[str(i).zfill(2) for i in range(0, 60, 5)],
                                    textvariable=self.minute_var, font="times 12", width=3)
        minute_combo.place(x=700, y=390)

        # AM/PM Combobox
        self.ampm_var = StringVar()
        ampm_combo = ttk.Combobox(self, values=["AM", "PM"], textvariable=self.ampm_var, font="times 12", width=3)
        ampm_combo.place(x=750, y=390)

        Date = tk.Label(self, text="Enter Date :", font="MSSerif 15 bold ", foreground="TEAL", background='Silver')
        Date.place(x=650, y=470)

        # Using DateEntry widget from tkcalendar for date selection
        self.date_entry = DateEntry(self, font="times 15 ", foreground="Black", width=20)
        self.date_entry.place(x=650, y=500)

        book = Button(self, text="Book", foreground="White", background="purple", font="times 15 bold", bg='TEAL',
                      height=1, width=25, command=self.book_appointment)
        book.place(x=400, y=600)

    def book_appointment(self):
        name = self.name_var.get()
        mobile = self.passw_var.get()
        selected_test = self.test_combo.get()
        selected_package = self.package_combo.get()
        selected_time = self.hour_var.get() + ":" + self.minute_var.get() + " " + self.ampm_var.get()
        selected_date = self.date_entry.get()

        # Get medical history and address values from Text widgets
        medihistory_value = self.disease_text.get("1.0", "end-1c")
        address_value = self.address_text.get("1.0", "end-1c")

        try:
            # Connect to the database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Mane2004@",
                database="hospital"
            )

            # Create a cursor object
            mycursor = mydb.cursor()

            # Insert appointment data into the database
            sql = "INSERT INTO lab (name, phone, medihistory, address, test, package,time,date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (name, mobile, medihistory_value, address_value, selected_test, selected_package, selected_time,
                   selected_date)
            mycursor.execute(sql, val)

            # Commit the transaction
            mydb.commit()

            # Display a success message
            messagebox.showinfo("Success", "Appointment booked successfully!")
        except mysql.connector.Error as error:
            print("Error inserting data into MySQL table:", error)
        finally:
            # Close the database connection
            if mydb.is_connected():
                mycursor.close()
                mydb.close()


        name = self.name_var.get()
        mobile = self.passw_var.get()
        selected_test = self.test_combo.get()
        selected_package = self.package_combo.get()
        selected_time = self.hour_var.get() + ":" + self.minute_var.get() + " " + self.ampm_var.get()
        selected_date = self.date_entry.get()
        messagebox.showinfo("Book Appointment",
                            f"Name: {name}.\nPhone No: {mobile}\nTest: {selected_test}\nPackage: {selected_package}\nTime: {selected_time}\nDate: {selected_date}")

    def back(self):
            self.destroy()
            from Medicine_Home import HomePage
            new_root = tk.Tk()
            app = HomePage(new_root)
            new_root.geometry("1100x600")
            new_root.title('NEW_PAGE')
            new_root.mainloop()


if __name__ == "__main__":
    app = LabTestPage()
    app.mainloop()
