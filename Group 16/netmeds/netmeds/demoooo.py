import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class HospitalManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1100x700")
        self.title('HOME')

        self.create_toolbar()
        self.create_labels()
        self.create_buttons()
        self.create_tables()
        self.create_show_button()

    def create_toolbar(self):
        toolbar = tk.Frame(self, bg='TEAL', bd=5)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        profile_button = tk.Button(toolbar, text='PROFILE', bg='White', fg='Teal', height=1, width=10, font="times 12 bold")
        profile_button.pack(side=tk.LEFT, padx=1000, pady=50)

        login_button = tk.Button(self, text="LOGOUT", bg='White', fg='TEAL', height=1, width=10, font="times 12 bold", command=self.open_login)
        login_button.place(x=950, y=50)

    def create_labels(self):
        admin_label = tk.Label(self, text="ADMIN", font="times 50 bold", foreground="White", bg='TEAL')
        admin_label.place(x=450, y=15)

    def create_buttons(self):
        hospital_button = tk.Button(self, text="HOSPITAL", bg='Teal', fg='WHITE', height=1, width=10, font="times 12 bold")
        hospital_button.place(x=750, y=150)

        lab_button = tk.Button(self, text="LAB", bg='Teal', fg='WHITE', height=1, width=10, font="times 12 bold")
        lab_button.place(x=600, y=150)

        doctors_button = tk.Button(self, text="DOCTORS", bg='Teal', fg='WHITE', height=1, width=10, font="times 12 bold")
        doctors_button.place(x=450, y=150)

        medicines_button = tk.Button(self, text="MEDICINES", bg='Teal', fg='WHITE', height=1, width=10, font="times 12 bold")
        medicines_button.place(x=300, y=150)

    def create_tables(self):
        # Create a Treeview widget for doctors
        doctors_tree = ttk.Treeview(self, columns=("Name", "Specialization", "Experience"), show="headings")
        doctors_tree.heading("Name", text="Name")
        doctors_tree.heading("Specialization", text="Specialization")
        doctors_tree.heading("Experience", text="Experience")
        doctors_tree.place(x=50, y=200, height=150, width=1000)

        # Create a Treeview widget for patients
        patients_tree = ttk.Treeview(self, columns=("Name", "Phone No", "Appointment", "Doctor Name", "Time"), show="headings")
        patients_tree.heading("Name", text="Name")
        patients_tree.heading("Phone No", text="Phone No")
        patients_tree.heading("Appointment", text="Appointment")
        patients_tree.heading("Doctor Name", text="Doctor Name")
        patients_tree.heading("Time", text="Time")
        patients_tree.place(x=50, y=365)

    def create_show_button(self):
        show_button = tk.Button(self, text="SHOW", bg='Teal', fg='WHITE', height=1, width=10, font="times 12 bold")
        show_button.place(x=500, y=600)

    def open_login(self):
        self.destroy()
        from Login import Loginhome
        new_root = tk.Tk()
        app = Loginhome(new_root)
        new_root.geometry("1100x600")
        new_root.title('LOGIN')
        new_root.mainloop()

if __name__ == "__main__":
    app = HospitalManagementApp()
    app.mainloop()
