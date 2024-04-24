import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector

class ProfilePage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1100x700")
        self.title('PROFILE')

        # Establish a connection to the MySQL database
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mane2004@",
            database="hospital"
        )
        self.cursor = self.connection.cursor()

        # Define StringVars for entry widgets
        self.name_var = StringVar()
        self.disease_text = Text(self, height=5, width=28, font="times 15 ", foreground="Black")
        self.address_text = Text(self, height=5, width=28, font="times 15 ", foreground="Black")
        self.blood = StringVar()
        self.gender = StringVar()
        self.age = StringVar()
        self.height = StringVar()
        self.weight = StringVar()

        toolbar = tk.Frame(self, bg='TEAL', bd=5)
        new_button = tk.Button(toolbar, text='BACK', bg='White', fg='Teal', height=1, width=10, font="times 12 bold")
        new_button.pack(side=tk.RIGHT, padx=500, pady=50)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        back = Button(self, text="BACK", bg='white', fg='teal', height=1, width=10, font="times 12 bold",
                      command=self.open_back)
        back.place(x=950, y=50)

        toolbar = tk.Frame(self, bg='silver', bd=5)
        new_button = tk.Button(toolbar, text='PROFILE', bg='White', fg='Teal', height=1, width=10, font="times 12 bold")
        new_button.pack(side=tk.LEFT, padx=100, pady=250)
        toolbar.pack(pady=50, fill=tk.X)

        login_label = Label(self, text="PROFILE", font="times 50 bold", foreground="White", bg='TEAL')
        login_label.place(x=400, y=25)

        name_entry = Entry(self, textvariable=self.name_var, font="times 20 ", foreground="Black")
        name_entry.place(x=200, y=250)

        Name = Label(self, text="Enter Name :", font="MSSerif 15 ", foreground="TEAL", background='silver')
        Name.place(x=200, y=220)

        self.disease_text = Text(self, height=5, width=28, font="times 15 ", foreground="Black")
        self.disease_text.place(x=200, y=330)

        disease = Label(self, text="Medical History :", font="MSSerif 15 ", foreground="TEAL", background='Silver')
        disease.place(x=200, y=300)

        address = Label(self, text="Address:", font="MSSerif 15 ", foreground="TEAL", background='Silver')
        address.place(x=200, y=450)

        self.address_text = Text(self, height=5, width=28, font="times 15 ", foreground="Black")
        self.address_text.place(x=200, y=480)

        blood_entry = Entry(self, textvariable=self.blood, font="times 20 ", foreground="Black", width=15)
        blood_entry.place(x=600, y=250)

        blood = Label(self, text="Enter Blood Group :", font="MSSerif 15 ", foreground="TEAL", background='silver')
        blood.place(x=600, y=220)

        gender_entry = Entry(self, textvariable=self.gender, font="times 20 ", foreground="Black", width=15)
        gender_entry.place(x=600, y=330)

        gender = Label(self, text="Gender :", font="MSSerif 15 ", foreground="TEAL", background='Silver')
        gender.place(x=600, y=300)

        age_entry = Entry(self, textvariable=self.age, font="times 15 ", foreground="Black", width=15)
        age_entry.place(x=600, y=410)

        age = Label(self, text="AGE:", font="MSSerif 15 ", foreground="TEAL", background='Silver')
        age.place(x=600, y=380)

        wt_entry = Entry(self, textvariable=self.weight, font="times 20 ", foreground="Black", width=15)
        wt_entry.place(x=600, y=565)

        save_btn = Button(self, text="Save", foreground="WHITE", background="purple", font="times 15 bold", bg='TEAL',width=10, command=self.save)
        save_btn.place(x=450, y=655)

        height_entry = Entry(self, textvariable=self.height, font="times 20 ", foreground="Black", width=15)
        height_entry.place(x=600, y=480)

        height = Label(self, text="Enter Height :", font="MSSerif 15 ", foreground="TEAL", background='silver')
        height.place(x=600, y=450)

        weight = Label(self, text="Enter weight :", font="MSSerif 15 ", foreground="TEAL", background='silver')
        weight.place(x=600, y=525)

    def save(self, event=None):
        # Retrieve data from tkinter entry widgets
        name = self.name_var.get()
        medical_history = self.disease_text.get("1.0", "end-1c")
        address = self.address_text.get("1.0", "end-1c")
        blood_group = self.blood.get()
        gender_value = self.gender.get()
        age_value = self.age.get()
        height_value = self.height.get()
        weight_value = self.weight.get()

        # Validate age input
        if not age_value.isdigit():
            messagebox.showerror("Error", "Please enter a valid age.")
            return  # Stop execution if age is not a valid integer

        age_value = int(age_value)  # Convert age input to integer

        # SQL INSERT query
        insert_query = "INSERT INTO profile_user (name, medical_history, address, blood_group, gender, age, height, weight) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        data = (name, medical_history, address, blood_group, gender_value, age_value, height_value, weight_value)

        # Execute the query
        self.cursor.execute(insert_query, data)

        # Commit changes to the database
        self.connection.commit()

        # Display a success message
        messagebox.showinfo("Success", "Data saved successfully!")

    def open_back(self):
        self.destroy()
        from Medicine_Home import HomePage
        new_root = tk.Tk()
        app = HomePage(new_root)
        new_root.geometry("1100x600")
        new_root.title('NEW_PAGE')
        new_root.mainloop()

if __name__ == "__main__":
    app = ProfilePage()
    app.mainloop()
