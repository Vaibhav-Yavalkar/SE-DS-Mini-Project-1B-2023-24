import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import Button, OptionMenu, StringVar, Canvas, Scrollbar

class HospitalApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x700")
        self.root.title('Hospitals Page')

        # Teal rectangle at the top
        self.canvas_teal = tk.Canvas(root, width=1100, height=100, bg='TEAL')
        self.canvas_teal.place(relx=0, rely=0, relwidth=1, relheight=0.2, anchor='nw')

        # Project label "Hospitals" above the teal rectangle
        self.project_label = tk.Label(root, text="Hospitals", font="times 45 bold", bg='TEAL', fg='WHITE')
        self.project_label.place(relx=0.5, rely=0.06, relwidth=0.3, relheight=0.1, anchor='n')

        # Dropdown menu for selecting city
        self.selected_city = StringVar(root)
        self.selected_city.set("Select City")  # Default value
        self.city_dropdown = OptionMenu(root, self.selected_city, "Thane", "Mulund", "Kalwa","Mumbai")
        self.city_dropdown.place(relx=0.1, rely=0.25, relwidth=0.2, relheight=0.05, anchor='nw')

        # Button to trigger search
        self.search_button = tk.Button(root, text="Search", font=("Arial", 12), command=self.search_hospitals)
        self.search_button.place(relx=0.35, rely=0.25, relwidth=0.1, relheight=0.05, anchor='nw')

        backbtn = Button(root, text="BACK", foreground="TEAL", background="purple", font="times 15 bold", bg='White',
                         height=1, width=5, command=self.back)
        backbtn.place(x=1000, y=50)

        # List of hospitals with name, address, and image path (Sample data)
        self.hospitals = [
            {"name": "Jupiter Hospital, Thane", "address": "Service Rd, Eastern Express Hwy, next to Viviana Mall, Thane, Maharashtra 400601", "phone": "123-456-7890","image_path": r"C:\Users\Abhijit\OneDrive\Desktop\pro\hos\thane\jupiter.jpg"},
            {"name": "Bethany Hospital", "address": "Bethany Hospital, Pokharan Rd Number 2, Shastri Nagar, Thane West, Thane, Maharashtra 400606", "phone": "987-654-3210","image_path": r"C:\Users\Abhijit\OneDrive\Desktop\pro\hos\thane\bethany.jpg"},
            {"name": "Vivek Birla Hospital  ", "address": " Landmark Arcade, 1st Floor, Louiswadi, Highway, Service Rd, Thane West, Thane, Maharashtra 400601", "phone": "456-789-0123","image_path": r"C:\Users\Abhijit\OneDrive\Desktop\pro\hos\thane\birla.jpeg"},
            {"name": "Criticare Superspeciality Hospital Thane", "address": " West, Eastern Express Hwy, next to Korum Mall, Sambhaji Nagar, Thane West, Thane, Maharashtra 400604", "phone": "789-012-3456","image_path": r"C:\Users\Abhijit\OneDrive\Desktop\pro\hos\thane\criticare.jpeg"},
            {"name": "Currae speciality hospital", "address": " Currae speciality hospital, Samata Nagar, Kapurbawdi, Majiwada, Thane, Maharashtra 400607", "phone": "012-345-6789","image_path": r"C:\Users\Abhijit\OneDrive\Desktop\pro\hos\thane\currae,thane.jpg"},
            {"name": "Dhanwantari Multispeciality Hospital", "address": "1st Floor, Om Sai Plaza, Near Mahindra Showroom, Ovala Naka, Ghodbunder Road, Thane West, Thane, Maharashtra 400607", "phone": "345-678-9012","image_path": r"C:\Users\Abhijit\OneDrive\Desktop\pro\hos\thane\dhanwantari-multispeciality-thane.jpg"},
            {"name": "Kaizen Super Specialty Hospital", "address": "1st floor, Silver Plaza, Road No. 33, above Raanka Banquet, nr. Nitin Company, Ramachandra Nagar, Signal, Thane West, Thane, Maharashtra 400606", "phone": "678-901-2345","image_path": r"C:\Users\Abhijit\OneDrive\Desktop\pro\hos\thane\kaizen.jpg"},
            {"name": "Kaushalya Medical Foundation Trust Hospital", "address": ": Ganeshwadi, behind Nitin Company, Panch Pakhdi, Thane, Maharashtra 400601", "phone": "901-234-5678","image_path": r"C:\Users\Abhijit\OneDrive\Desktop\pro\hos\thane\kaushlya.jpeg"},
            {"name": "Solaris Superspecialty Hospital", "address": " Service Road, Ghodbunder Rd, next to AP Shah Institute of Technology, Kasarvadavali, Thane West, Maharashtra 400615", "phone": "111-222-3333","image_path": "C:/New folder/pro/hosptials/solaris.jpeg"},
            {"name": "Tieten Medicity - Super Speciality Hospital", "address": " Tieten Medicity, Ghodbunder Rd, Kasarvadavali, Thane West, Thane, Maharashtra 400615", "phone": "444-555-6666","image_path": r"C:\Users\Abhijit\OneDrive\Desktop\pro\hos\thane\vedant.jpeg"},


            {"name": "Platinum Hospital Mulund", "address": " Neptune Colorscape, Dumping Rd, Siddharth Nagar, Mulund West, Maharashtra 400080", "phone": "777-888-9999","image_path": r"C:\Users\Abhijit\OneDrive\Desktop\pro\hos\mulund\Platinum Hospitals.jpg"},
            {"name": "Apex Hospitals Mulund", "address": "Tulsi Pipe Line Road, Veena Nagar Phase-II, Mulund West, Maharashtra 400080", "phone": "888-999-0000","image_path": r"C:\Users\Abhijit\OneDrive\Desktop\pro\hos\mulund\apex hospitals mulund.jpg"},
            {"name": "Sai Kripa Hospital & ICU", "address": " Ashish Apartment, Rani Sati Rd, beside Mohammadi Apartment, Vrindavan Society, Shantivan Society, Raheja Twp, Mulund East, Maharashtra 400097", "phone": "222-333-4444","image_path": r"C:\Users\Abhijit\OneDrive\Desktop\pro\hos\mulund\sai krupa.webp"},
            {"name": "Ayush healthcare", "address": "5XH4+MFH, Shanti Industrial Estate, Sarojini Naidu Rd, Mulund West, Maharashtra 400080", "phone": "333-444-5555","image_path": r"C:\Users\Abhijit\OneDrive\Desktop\pro\hos\mulund\ayush hospital mulund.jpg"},
            {"name": "Nirmaladevi Sardarmal Jain Charitable Medical Center", "address": " 5XH2+CM7, NS Rd, Near Jawar Talkies Compund, Jagjivan Ram Nagar, Mulund West, Maharashtra 400080", "phone": "444-555-6666","image_path": r"C:\Users\Abhijit\OneDrive\Desktop\pro\hos\mulund\Nirmal Hospital mulund.jpg"},

            {"name": "Siddhivinayak Hospital", "address": "S1, Tulsi Dham, Vedant Complex, Vartak Nagar, Mulund West, mulund, Maharashtra 400606", "phone": "444-555-6666",
             "image_path": r"C:\Users\Abhijit\OneDrive\Desktop\pro\hos\mulund\Siddhivinayak Multispeciality Hospital mulund.png"},


            {"name": "Aayush Multispecialty Hospital -", "address": "1st Floor , Marigold Apartment Almeda Rd, Mahapalika Bhavan Rd, opposite Nitin Co & Honda Showroom, Panch Pakhdi, Kalwa, Kalwa, Maharashtra 400602", "phone": "444-555-6666",
             "image_path": r"C:\Users\Abhijit\OneDrive\Desktop\pro\hos\kalwa\ayush,kalwa.jpg"},
            {"name": "Chhatrapati Shivaji Maharaj Hospital, Kalwa", "address": "5XVP+9PF, Unnamed Road, Kalwa West, Budhaji Nagar, Kalwa, Maharashtra 400605", "phone": "444-555-6666",
             "image_path": r"C:\Users\Abhijit\OneDrive\Desktop\pro\hos\kalwa\Chhatrapati-Shivaji-Maharaj-Hospital-Kalwa-deaths.webp"},
            {"name": "Drishti Eye Clinic", "address": "101, 102, 1st Floor Bharti Apt, Pune - Mumbai Hwy, Shastri Nagar, Kalwa, Maharashtra 400605", "phone": "444-555-6666",
             "image_path": r"C:\Users\Abhijit\OneDrive\Desktop\pro\hos\kalwa\Dadar Eye & Maternity Hospital kalwa.jpg"},
            {"name": "Parekh Hospital", "address": "5, Pune - Mumbai Hwy, Parsik Nagar, Kalwa, Maharashtra 400605", "phone": "444-555-6666",
             "image_path": r"C:\Users\Abhijit\OneDrive\Desktop\pro\hos\kalwa\Parekh Hospital kalwa.png"},
            {"name": "Sanjivani Hospital", "address": "Shiv Shakti Mitra Mandal Chawl, Kalwa  - 400605 (Near Ambe Mata Mandir, Bhaskar Nagar)", "phone": "444-555-6666",
             "image_path": r"C:\Users\Abhijit\OneDrive\Desktop\pro\hos\kalwa\Sanjeevani Hospital  kalwa.jpg"},
            {"name": "Vaishnavis Multispeciality Hospita", "address": " 11, Guru Nanak Rd, Kopari, Daulat Nagar, kalwa  , Maharashtra 400603", "phone": "444-555-6666",
             "image_path": r"C:\Users\Abhijit\OneDrive\Desktop\pro\hos\kalwa\Vaishnavi Hospital kalwa.jpg"},

            {"name": "Bombay Hospital & Medical Research Centre", "address": " Bombay Hospital, 12, Vitthaldas Thackersey Marg, near Liberty cinema, New Marine Lines, Marine Lines, Mumbai, Maharashtra 400020", "phone": "444-555-6666",
             "image_path": r"C:\Users\Abhijit\OneDrive\Desktop\pro\hos\bombay.jpg"},
            {"name": "Jai Hind Hospital & ICCU", "address": " K School, 162, PL Lokhande Marg, opposite Mighty Commercial Complex & R.B, Gautam Nagar, Govandi East, Mumbai, Maharashtra 400043", "phone": "444-555-6666",
             "image_path": r"C:\Users\Abhijit\OneDrive\Desktop\pro\hos\hind.jpeg"},
            {"name": "Horizon Prime Hospital", "address": " Vibgyor, B- Wing, Patlipada, Ghodbunder Rd, near Hiranandani Estate, behind Ritu Nissan Showroom, mumbai , Maharashtra 400607", "phone": "444-555-6666",
             "image_path": r"C:\Users\Abhijit\OneDrive\Desktop\pro\hos\horizon prime.jpg"},
            {"name": "Jaslok Hospital & Research Centre", "address": "15, Pedder Rd, IT Colony, Tardeo, Mumbai, Maharashtra 400026", "phone": "444-555-6666",
             "image_path": r"C:\Users\Abhijit\OneDrive\Desktop\pro\hos\jaslok.jpeg"},
            {"name": "Kokilaben Dhirubhai Ambani Hospital and Medical Research Institute", "address": "Rao Saheb, Rao Saheb Achutrao Patwardhan Marg, Four Bungalows, Andheri West, Mumbai, Maharashtra 400053", "phone": "444-555-6666",
             "image_path": r"C:\Users\Abhijit\OneDrive\Desktop\pro\hos\kokilaben.jpeg"},
            {"name": "Lilavati Hospital And Research Centre", "address": "A-791, A-791, Bandra Reclamation Rd, General Arunkumar Vaidya Nagar, Bandra West, Mumbai, Maharashtra 400050", "phone": "444-555-6666",
             "image_path": r"C:\Users\Abhijit\OneDrive\Desktop\pro\hos\lilavati.jpeg"},
            {"name": "Tata Memorial Hospital", "address": "Homi Babha Building, Dr Ernest Borges Rd, Parel East, Parel, Mumbai, Maharashtra 400012", "phone": "444-555-6666",
             "image_path": r"C:\Users\Abhijit\OneDrive\Desktop\pro\hos\tata.jpg"},



        ]

        # Canvas to contain hospital information
        self.canvas = Canvas(root, bg="WHITE", bd=0, highlightthickness=0)
        self.canvas.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.6)

        # Scrollbar
        self.scrollbar = Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.scrollbar.place(relx=0.9, rely=0.35, relheight=0.6)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.hospital_frame = tk.Frame(self.canvas, bg="WHITE")
        self.canvas.create_window((0, 0), window=self.hospital_frame, anchor="nw")

        # Display hospitals initially
        self.display_hospitals()

    def search_hospitals(self):
        selected_city = self.selected_city.get()
        if selected_city == "Select City":
            messagebox.showinfo("Info", "Please select a city.")  # Display messagebox if no city is selected
            return
        filtered_hospitals = [hospital for hospital in self.hospitals if selected_city.lower() in hospital['address'].lower()]
        self.display_hospitals(filtered_hospitals)

    def display_hospitals(self, hospitals=None):
        # Clear previous hospital information
        for widget in self.hospital_frame.winfo_children():
            widget.destroy()

        # Display hospital information
        if hospitals:
            for idx, hospital in enumerate(hospitals):
                try:
                    # Load and display image
                    image = Image.open(hospital['image_path'])
                    image = image.resize((100, 100), Image.BILINEAR)
                    photo = ImageTk.PhotoImage(image)
                    image_label = tk.Label(self.hospital_frame, image=photo)
                    image_label.image = photo
                    image_label.grid(row=idx, column=0, padx=10, pady=10, sticky='n')

                    # Display hospital name, phone number, and address
                    name_label = tk.Label(self.hospital_frame, text=hospital['name'], font=("Arial", 12))
                    name_label.grid(row=idx, column=1, padx=10, pady=(20, 5), sticky='nw')

                    phone_label_text = "Contact Number: " + hospital.get('phone', 'Phone number not available')
                    phone_label = tk.Label(self.hospital_frame, text=phone_label_text, font=("Arial", 10))
                    phone_label.grid(row=idx, column=1, padx=10, pady=(5, 5), sticky='w')

                    address_label = tk.Label(self.hospital_frame, text=hospital['address'], font=("Arial", 12))
                    address_label.grid(row=idx, column=1, padx=10, pady=(5, 20), sticky='sw')
                except Exception as e:
                    print(f"Error loading image: {e}")

        # Update canvas scroll region
        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

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
    app = HospitalApp(root)
    root.mainloop()
