import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

class HomePage:
    def __init__(self, root):
        self.root = root

        # Toolbar
        toolbar = Frame(root, bg='TEAL', bd=5)
        new_button = Button(toolbar, text='PROFILE', bg='White', fg='Teal', height=1, width=10, font="times 12 bold",command= self.open_Profile_user)
        new_button.pack(side=LEFT, padx=50, pady=50)
        toolbar.pack(side=TOP, fill=X)

        # Second Toolbar
        toolbar = Frame(root, bg='silver', bd=5)
        new_button = Button(toolbar, text='PROFILE', bg='White', fg='Teal', height=1, width=10, font="times 12 bold")
        new_button.pack(side=LEFT, padx=100, pady=250)
        toolbar.pack(pady=50, fill=X)

        # Labels and Buttons
        netmeds = Label(root, text="Quickmeds", font="times 50 bold", foreground="White", bg='TEAL')
        netmeds.place(x=450, y=25)



        loginbtn = Button(root, text="Logout", foreground="TEAL", background="purple", font="times 15 bold", bg='White',
                          height=1, width=5,command=self.back)
        loginbtn.place(x=1000, y=10)



        # Load image for the button
        hospi_img = Image.open(r"C:\New folder\pro\hospital.jpg")
        button_width = 175
        button_height = 200
        hospi_img = hospi_img.resize((button_width, button_height))
        hospi_img = ImageTk.PhotoImage(hospi_img)


        hospi = Button(root, text="HOSPITAL", image=hospi_img, bg='Teal', fg='WHITE', height=button_height, width=button_width, font="times 12 bold",command=self.open_hosp)
        hospi.image = hospi_img  # Keep reference to avoid garbage collection
        hospi.place(x=825, y=300)
        hospital = Label(root, text="HOSPITAL", font="times 20 bold", foreground="Black",bg='Silver')
        hospital.place(x=860, y=550)

        lab_img = Image.open(r"C:\New folder\pro\lab.jpg")
        button_width = 175
        button_height = 200
        lab_img = lab_img.resize((button_width, button_height))
        lab_img = ImageTk.PhotoImage(lab_img)

        lab = Button(root, text="MEDICINES", image=lab_img, bg='Teal', fg='WHITE', height=button_height,
                    width=button_width, font="times 12 bold", command=self.lab)
        lab.image = lab_img  # Keep reference to avoid garbage collection
        lab.place(x=575, y=300)
        Lab = Label(root, text="LAB", font="times 20 bold", foreground="Black",bg='Silver')
        Lab.place(x=640, y=550)

        dr_img = Image.open(r"C:\New folder\pro\dr1.webp")
        button_width = 175
        button_height = 200
        dr_img = dr_img.resize((button_width, button_height))
        dr_img = ImageTk.PhotoImage(dr_img)

        dr = Button(root, text="MEDICINES", image=dr_img, bg='Teal', fg='WHITE', height=button_height,
                      width=button_width, font="times 12 bold", command=self.open_de_list_user)
        dr.image = dr_img  # Keep reference to avoid garbage collection
        dr.place(x=325, y=300)
        dr = Label(root, text="DOCTOR", font="times 20 bold", foreground="Black",bg='Silver')
        dr.place(x=350, y=550)

        # Load image for the button
        medi_img = Image.open(r"C:\New folder\pro\medicine.jpg")
        button_width = 175
        button_height = 200
        medi_img = medi_img.resize((button_width, button_height))
        medi_img = ImageTk.PhotoImage(medi_img)

        medi = Button(root, text="MEDICINES", image=medi_img, bg='Teal', fg='WHITE', height=button_height,
                      width=button_width, font="times 12 bold")
        medi.image = medi_img  # Keep reference to avoid garbage collection
        medi.place(x=75, y=300)
        Medicine = Label(root, text="MEDICINE", font="times 20 bold", foreground="Black",bg='Silver')
        Medicine.place(x=90, y=550)


    def open_Profile_user(self):
        self.root.destroy()
        from Profile_user import ProfilePage

        app = ProfilePage()




    def open_new_page(self):
        # Close the current window
        self.root.destroy()
        # Open the new page window
        from me_cold_cough import NewPage  # Import the NewPage class from the second script
        root = tk.Tk()
        app = NewPage(root)
        root.geometry("1100x600")
        root.title('NEW_PAGE')
        root.mainloop()

    def open_add_cart(self):
        # Close the current window
        self.root.destroy()
        # Open the new page window
        from add_cart import AddToCartPage  # Import the NewPage class from the second script
        root = tk.Tk()
        app = AddToCartPage(root)
        root.geometry("1100x600")
        root.title('NEW_PAGE')
        root.mainloop()
    def login_admin(self):
        self.destroy()
        from Profile_user import ProfilePage
        #new_root = tk.Tk()
        app = ProfilePage()
        #new_root.geometry("1100x600")
        #new_root.title('NEW_PAGE')

    def open_de_list_user(self):
            self.root.destroy()
            from list_dr_user import DoctorsPage
            new_root = tk.Tk()
            app = DoctorsPage(new_root)
            new_root.geometry("1100x600")
            new_root.title('NEW_PAGE')
            new_root.mainloop()

    def open_hosp(self):
            self.root.destroy()
            from hospital_user import HospitalApp
            new_root = tk.Tk()
            app = HospitalApp(new_root)
            new_root.geometry("1100x600")
            new_root.title('NEW_PAGE')
            new_root.mainloop()

    def login(self):
            self.root.destroy()
            from Login import Loginhome
            new_root = tk.Tk()
            app = Loginhome(new_root)
            new_root.geometry("1100x600")
            new_root.title('NEW_PAGE')
            new_root.mainloop()

    def lab(self):
            self.root.destroy()
            from lab_user import LabTestPage
            #new_root = tk.Tk()
            app = LabTestPage()
            #new_root.geometry("1100x600")
            #new_root.title('NEW_PAGE')
            new_root.mainloop()

    def back(self):
        try:
            self.root.destroy()  # Destroy the main window
            from Login import Loginhome

            app = Loginhome()  # Remove the 'new_root' argument here

        except ImportError:
            print("Error importing NewPage from me_cold_cough")


if __name__ == "__main__":
    root = tk.Tk()
    app = HomePage(root)
    root.geometry("1100x700")
    root.title('HOME')
    root.mainloop()
