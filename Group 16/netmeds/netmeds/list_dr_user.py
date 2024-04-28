import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import Button, Entry, Checkbutton
import mysql.connector
from datetime import datetime

class DoctorsPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Doctors Page")
        self.root.config(bg='teal')  # Set background color

        # Main Frame with teal background and border
        main_frame = tk.Frame(root, bg='teal', bd=5)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Logo
        logo_label = tk.Label(root, text="Netmeds.com", font="times 15 bold", foreground="White", bg='TEAL')
        logo_label.place(x=50, y=20)

        #Headings
        categories_label = tk.Label(root, text="CATEGORIES", font="times 15 bold", foreground="White", bg='TEAL')
        categories_label.place(x=75, y=70)
        listdoc_label = tk.Label(root, text="LIST OF DOCTORS", font="times 15 bold", foreground="White", bg='TEAL')
        listdoc_label.place(x=630, y=80)

        # Project Name Label
        project_label = tk.Label(main_frame, text=" Doctors ", font="times 25 bold", bg='teal', fg='white')
        project_label.pack(side=tk.TOP, pady=10)

        # Back Button
        backbtn = Button(root, text="BACK", foreground="TEAL", background="purple", font="times 15 bold", bg='White',height=1, width=5,command=self.back)
        backbtn.place(x=1000, y=10)

        # Blank Label
        blank_label = tk.Label(main_frame, text=" ", font=("Helvetica", 16), bg='teal', fg='white')
        blank_label.pack(side=tk.TOP, pady=5)

        # Categories Listbox (as sidebar)
        self.categories_listbox = tk.Listbox(main_frame, selectmode=tk.SINGLE, font=("Helvetica", 20))
        self.categories_listbox.pack(side=tk.LEFT, fill=tk.Y, padx=10)

        # Populate Categories
        categories = ["Cardiologist", "Dermatologist", "Orthopedic", "ENT", "Gynecologist",
                      "Adiatrixist", "Psychiatrist", "Neurologist", "Dentist", "General Physician"]
        for category in categories:
            self.categories_listbox.insert(tk.END, category)

        # Doctors Listbox
        self.doctors_listbox = tk.Listbox(main_frame, selectmode=tk.SINGLE, font=("Helvetica", 19), height=2, width=20)
        self.doctors_listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Doctor Description Text
        self.doctor_description_text = tk.Text(main_frame, height=10, width=50, font=("Helvetica", 18))  # Increased font size
        self.doctor_description_text.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Book Appointment Button
        self.book_appointment_button = tk.Button(main_frame, text="Book Appointment", command=self.book_appointment, state=tk.DISABLED)
        self.book_appointment_button.pack(side=tk.BOTTOM, pady=10)

        # Bind category selection event
        self.categories_listbox.bind('<<ListboxSelect>>', self.show_doctors)

        # Bind doctor selection event
        self.doctors_listbox.bind('<<ListboxSelect>>', self.show_doctor_info)

        # Time label
        Time = tk.Label(main_frame, text="Enter Time :", font="MSSerif 15 bold", foreground="TEAL",bg="white")
        Time.place(x=350, y=360)

        # Hour Combobox
        self.hour_var = tk.StringVar()
        hour_combo = ttk.Combobox(main_frame, values=[str(i).zfill(2) for i in range(1, 13)], textvariable=self.hour_var, font="times 12", width=3)
        hour_combo.place(x=350, y=400)

        # Minute Combobox
        self.minute_var = tk.StringVar()
        minute_combo = ttk.Combobox(main_frame, values=[str(i).zfill(2) for i in range(0, 60, 5)], textvariable=self.minute_var, font="times 12", width=3)
        minute_combo.place(x=400, y=400)

        # AM/PM Combobox
        self.ampm_var = tk.StringVar()
        ampm_combo = ttk.Combobox(main_frame, values=["AM", "PM"], textvariable=self.ampm_var, font="times 12", width=3)
        ampm_combo.place(x=450, y=400)

        # Date label
        Date = tk.Label(main_frame, text="Enter Date :", font="MSSerif 15 bold ", foreground="TEAL",bg="white")
        Date.place(x=350, y=440)

        # Using DateEntry widget from tkcalendar for date selection
        self.date_entry = DateEntry(main_frame, font="times 15 ", foreground="Black", width=20)
        self.date_entry.place(x=350, y=480)

        # Name Label
        Name = tk.Label(main_frame, text="Enter Name :", font="MSSerif 15 bold", foreground="TEAL",bg="white")
        Name.place(x=650, y=360)

        # Entry for Name
        self.name_entry = Entry(main_frame, font="MSSerif 15 ", width=20)
        self.name_entry.place(x=650, y=400)

        # Mobile Number label
        mobno = tk.Label(main_frame, text="Enter Mobile Number :", font="MSSerif 15 bold ", foreground="TEAL",bg="white")
        mobno.place(x=650, y=440)

        # Entry for Mobile Number
        self.mobno_entry = Entry(main_frame, font="MSSerif 15 ", width=20)
        self.mobno_entry.place(x=650, y=480)

        # Gender label
        Gender = tk.Label(main_frame, text="Select Gender :", font="MSSerif 15 bold", foreground="TEAL",bg="white")
        Gender.place(x=900, y=360)

        # Male check button
        self.male_var = tk.BooleanVar()
        male_checkbox = Checkbutton(main_frame, text="Male", variable=self.male_var, font="MSSerif 12", bg="teal",
                                    fg="black")
        male_checkbox.place(x=900, y=400)

        # Female check button
        self.female_var = tk.BooleanVar()
        female_checkbox = Checkbutton(main_frame, text="Female", variable=self.female_var, font="MSSerif 12", bg="teal",
                                      fg="black")
        female_checkbox.place(x=900, y=440)

        # Other check button
        self.other_var = tk.BooleanVar()
        other_checkbox = Checkbutton(main_frame, text="Other", variable=self.other_var, font="MSSerif 12", bg="teal",
                                     fg="black")
        other_checkbox.place(x=900, y=480)

        # Dictionary to store doctor information
        self.doctor_info = {
            "Dr. Babulaal": "Cardiologist\nWork Experience: Worked for 15 years\nContact: 45464642134",
            "Dr. Champak": "Cardiologist\nWork Experience: Worked for 10 years\nContact: 45464642135",
            "Dr. Hathi": "Cardiologist\nWork Experience: Worked for 20 years\nContact: 45464642136",
            "Dr. Mane": "Dermatologist\nWork Experience: Worked for 18 years\nContact: 45464642137",
            "Dr. Mohanty": "Dermatologist\nWork Experience: Worked for 12 years\nContact: 45464642138",
            "Dr. Mahajan": "Dermatologist\nWork Experience: Worked for 22 years\nContact: 45464642139",
            "Dr. Virkar": "Dermatologist\nWork Experience: Worked for 8 years\nContact: 45464642140",
            "Dr. Smith": "Orthopedic\nWork Experience: Worked for 15 years\nContact: 45464642141",
            "Dr. Johnson": "Orthopedic\nWork Experience: Worked for 10 years\nContact: 45464642142",
            "Dr. Patel": "Orthopedic\nWork Experience: Worked for 20 years\nContact: 45464642143",
            "Dr. Lee": "ENT\nWork Experience: Worked for 18 years\nContact: 45464642144",
            "Dr. Kim": "ENT\nWork Experience: Worked for 12 years\nContact: 45464642145",
            "Dr. Park": "ENT\nWork Experience: Worked for 22 years\nContact: 45464642146",
            "Dr. Garcia": "Gynecologist\nWork Experience: Worked for 8 years\nContact: 45464642147",
            "Dr. Martinez": "Gynecologist\nWork Experience: Worked for 15 years\nContact: 45464642148",
            "Dr. Rodriguez": "Gynecologist\nWork Experience: Worked for 10 years\nContact: 45464642149",
            "Dr. Wang": "Adiatrixist\nWork Experience: Worked for 20 years\nContact: 45464642150",
            "Dr. Zhang": "Adiatrixist\nWork Experience: Worked for 18 years\nContact: 45464642151",
            "Dr. Li": "Adiatrixist\nWork Experience: Worked for 12 years\nContact: 45464642152",
            "Dr. Jones": "Psychiatrist\nWork Experience: Worked for 22 years\nContact: 45464642153",
            "Dr. Davis": "Psychiatrist\nWork Experience: Worked for 8 years\nContact: 45464642154",
            "Dr. Brown": "Psychiatrist\nWork Experience: Worked for 15 years\nContact: 45464642155",
            "Dr. Nguyen": "Neurologist\nWork Experience: Worked for 10 years\nContact: 45464642156",
            "Dr. Tran": "Neurologist\nWork Experience: Worked for 20 years\nContact: 45464642157",
            "Dr. Le": "Neurologist\nWork Experience: Worked for 18 years\nContact: 45464642158",
            "Dr. White": "Dentist\nWork Experience: Worked for 12 years\nContact: 45464642159",
            "Dr. Taylor": "Dentist\nWork Experience: Worked for 22 years\nContact: 45464642160",
            "Dr. Anderson": "General Physician\nWork Experience: Worked for 8 years\nContact: 45464642161",
            "Dr. Thomas": "General Physician\nWork Experience: Worked for 15 years\nContact: 45464642162",
            "Dr. Wilson": "General Physician\nWork Experience: Worked for 10 years\nContact: 45464642163"
        }

    def show_doctors(self, event):
        selected_category_index = self.categories_listbox.curselection()

        if selected_category_index:
            # Clear previous doctors in the listbox and doctor description
            self.doctors_listbox.delete(0, tk.END)
            self.doctor_description_text.delete("1.0", tk.END)

            # Get selected category
            selected_category = self.categories_listbox.get(selected_category_index)

            # Display doctors for the selected category
            doctors = self.get_doctors_by_category(selected_category)
            for doctor in doctors:
                self.doctors_listbox.insert(tk.END, doctor)

            # Enable the Book Appointment button
            self.book_appointment_button.config(state=tk.NORMAL)

    def get_doctors_by_category(self, category):
        if category == "Cardiologist":
            return ["Dr. Babulaal", "Dr. Champak", "Dr. Hathi"]
        elif category == "Dermatologist":
            return ["Dr. Mane", "Dr. Mohanty", "Dr. Mahajan", "Dr. Virkar"]
        elif category == "Orthopedic":
            return ["Dr. Smith", "Dr. Johnson", "Dr. Patel"]
        elif category == "ENT":
            return ["Dr. Lee", "Dr. Kim", "Dr. Park"]
        elif category == "Gynecologist":
            return ["Dr. Garcia", "Dr. Martinez", "Dr. Rodriguez"]
        elif category == "Adiatrixist":
            return ["Dr. Wang", "Dr. Zhang", "Dr. Li"]
        elif category == "Psychiatrist":
            return ["Dr. Jones", "Dr. Davis", "Dr. Brown"]
        elif category == "Neurologist":
            return ["Dr. Nguyen", "Dr. Tran", "Dr. Le"]
        elif category == "Dentist":
            return ["Dr. White", "Dr. Taylor", "Dr. Martinez"]
        elif category == "General Physician":
            return ["Dr. Anderson", "Dr. Thomas", "Dr. Wilson"]
        else:
            return []

    def show_doctor_info(self, event):
        selected_doctor_index = self.doctors_listbox.curselection()
        if selected_doctor_index:
            selected_doctor = self.doctors_listbox.get(selected_doctor_index)
            doctor_info = self.doctor_info.get(selected_doctor, "No information available")
            self.doctor_description_text.delete("1.0", tk.END)
            self.doctor_description_text.insert(tk.END, doctor_info)

    def book_appointment(self):
        name = self.name_entry.get()
        mobile = self.mobno_entry.get()
        gender = ""
        if self.male_var.get():
            gender = "Male"
        elif self.female_var.get():
            gender = "Female"
        elif self.other_var.get():
            gender = "Other"
        else:
            gender = "Not Specified"

        selected_doctor_index = self.doctors_listbox.curselection()
        if selected_doctor_index:
            selected_doctor = self.doctors_listbox.get(selected_doctor_index)
            selected_time = self.hour_var.get() + ":" + self.minute_var.get() + " " + self.ampm_var.get()
            selected_date = self.date_entry.get()

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

                # Format date
                selected_date = datetime.strptime(selected_date, "%m/%d/%y").strftime("%Y-%m-%d")

                # Insert appointment data into the database
                sql = "INSERT INTO dr_appoint (doctor_name, name, time, date, phone, gender) VALUES (%s, %s, %s, %s, %s, %s)"
                val = (selected_doctor, name, selected_time, selected_date, mobile, gender)
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
        else:
            messagebox.showerror("Error", "Please select a doctor.")

    def back(self):
            self.root.destroy()
            from Medicine_Home import HomePage
            new_root = tk.Tk()
            app = HomePage(new_root)
            new_root.geometry("1100x600")
            new_root.title('NEW_PAGE')
            new_root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = DoctorsPage(root)
    root.geometry("1100x700")
    root.mainloop()
