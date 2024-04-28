import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

class DoctorsPage:
    def __init__(self, root):
        self.root = root

        # Toolbar
        toolbar = Frame(root, bg='TEAL', bd=5)
        new_button = Button(toolbar, text='PROFILE', bg='White', fg='Teal', height=1, width=10, font="times 12 bold")
        new_button.pack(side=LEFT, padx=50, pady=50)
        toolbar.pack(side=TOP, fill=X)

        # Header
        netmeds = Label(root, text="Netmeds", font="times 50 bold", foreground="White", bg='TEAL')
        netmeds.place(x=475, y=25)

        cart = Button(root, text="cart", foreground="TEAL", background="purple", font="times 15 bold", bg='White',
                      height=1, width=5)
        cart.place(x=900, y=10)

        home = Button(root, text="Home", foreground="TEAL", background="purple", font="times 15 bold", bg='White',
                      height=1, width=5)
        home.place(x=1000, y=10)

        medicine = Label(root, text="Medicines - Burns", font="times 30 bold", foreground="BLack", bg='White')
        medicine.place(x=450, y=145)





        # Second Toolbar
        toolbar = Frame(root, bg='silver', bd=5)
        new_button = Button(toolbar, text='PROFILE', bg='White', fg='Teal', height=1, width=10, font="times 12 bold")
        new_button.pack(side=LEFT, padx=100, pady=250)
        toolbar.pack(pady=50, fill=X)



        # Categories Listbox
        categories1 = Button(root, text="Allergies", foreground="TEAL", background="Silver", font="times 10 ",
                             bg='White',
                             height=1, width=18, command=self.open_all)
        categories1.place(x=15, y=205)

        categories2 = Button(root, text="AntiScar", foreground="TEAL", background="Silver", font="times 10 ",
                             bg='White',
                             height=1, width=18, command=self.open_anti)
        categories2.place(x=15, y=228)

        categories3 = Button(root, text="Asthma", foreground="TEAL", background="Silver", font="times 10 ",
                             bg='White',
                             height=1, width=18, command=self.open_asth)
        categories3.place(x=15, y=251)

        categories4 = Button(root, text="Ayurvedic Medicines", foreground="TEAL", background="Silver", font="times 10 ",
                             bg='White',
                             height=1, width=18, command=self.open_ayu)
        categories4.place(x=15, y=274)

        categories5 = Button(root, text="Bacterial Infection", foreground="TEAL", background="Silver", font="times 10 ",
                             bg='White',
                             height=1, width=18, command=self.open_bact)
        categories5.place(x=15, y=297)

        categories6 = Button(root, text="Burns", foreground="TEAL", background="Silver", font="times 10 ",
                             bg='White',
                             height=1, width=18, command=self.open_burns)
        categories6.place(x=15, y=320)

        categories7 = Button(root, text="Bone Metabolism", foreground="TEAL", background="Silver", font="times 10 ",
                             bg='White',
                             height=1, width=18, command=self.open_bone)
        categories7.place(x=15, y=343)

        categories8 = Button(root, text="Cough & Cold", foreground="TEAL", background="Silver", font="times 10 ",
                             bg='White',
                             height=1, width=18, command=self.open_me_cold_cough)
        categories8.place(x=15, y=366)

        categories9 = Button(root, text="Constipation", foreground="TEAL", background="Silver", font="times 10 ",
                             bg='White',
                             height=1, width=18, command=self.open_consti)
        categories9.place(x=15, y=389)

        categories10 = Button(root, text="Cleansers", foreground="TEAL", background="Silver", font="times 10 ",
                              bg='White',
                              height=1, width=18, command=self.open_clean)
        categories10.place(x=15, y=412)

        categories11 = Button(root, text="Diabetes", foreground="TEAL", background="Silver", font="times 10 ",
                              bg='White',
                              height=1, width=18, command=self.open_dia)
        categories11.place(x=15, y=435)

        categories12 = Button(root, text="Dry Skin", foreground="TEAL", background="Silver", font="times 10 ",
                              bg='White',
                              height=1, width=18, command=self.open_dryskin)
        categories12.place(x=15, y=458)

        categories13 = Button(root, text="Fever", foreground="TEAL", background="Silver", font="times 10 ",
                              bg='White',
                              height=1, width=18, command=self.open_fever)
        categories13.place(x=15, y=481)

        categories14 = Button(root, text="Malaria", foreground="TEAL", background="Silver", font="times 10 ",
                              bg='White',
                              height=1, width=18, command=self.open_Mal)
        categories14.place(x=15, y=504)

        categories15 = Button(root, text="Scar", foreground="TEAL", background="Silver", font="times 10 ",
                              bg='White',
                              height=1, width=18, command=self.open_scar)
        categories15.place(x=15, y=527)

        # Bind category selection event
        #self.categories_listbox.bind('<<ListboxSelect>>', self.show_doctors)

        # Load and resize image
        image_path = r"C:\Users\Abhijit\OneDrive\Desktop\pro\candid.jpg"
        original_image = Image.open(image_path)
        resized_image = original_image.resize((150, 160), Image.BILINEAR)  # Resize image to 200x200
        self.tkinter_image = ImageTk.PhotoImage(resized_image)

        # Display resized image
        self.image_label = Label(root, image=self.tkinter_image)
        self.image_label.place(x=180, y=225)  # Relocate image on the page

        all1 = Label(root, text=" Burns Cream", font="times 20 bold", foreground="Black", bg='Silver')
        all1.place(x=180, y=400)

        allt1 = Label(root, text="     Rs. 86.40", font="times 16 bold", foreground="Black", bg='Silver')
        allt1.place(x=180, y=445)

        medi = Button(root, text="Add To cart", bg='white', fg='black', height=1, width=10, font="times 12 bold")
        medi.place(x=200, y=485)


        image_path = r"C:\Users\Abhijit\OneDrive\Desktop\pro\candid.jpg"
        original_image = Image.open(image_path)
        resized_image = original_image.resize((150, 160), Image.BILINEAR)  # Resize image to 200x200
        self.tkinter_image = ImageTk.PhotoImage(resized_image)

        # Display resized image
        self.image_label = Label(root, image=self.tkinter_image)
        self.image_label.place(x=370, y=225)

        all2 = Label(root, text=" Burncet", font="times 20 bold", foreground="Black", bg='Silver')
        all2.place(x=370, y=400)

        allt2 = Label(root, text="     Rs. 96.00", font="times 16 bold", foreground="Black", bg='Silver')
        allt2.place(x=370, y=445)

        medi = Button(root, text="Add To cart", bg='white', fg='black', height=1, width=10, font="times 12 bold")
        medi.place(x=390, y=485)

        image_path =r"C:\Users\Abhijit\OneDrive\Desktop\pro\candid.jpg"
        original_image = Image.open(image_path)
        resized_image = original_image.resize((150, 160), Image.BILINEAR)  # Resize image to 200x200
        self.tkinter_image = ImageTk.PhotoImage(resized_image)

        # Display resized image
        self.image_label = Label(root, image=self.tkinter_image)
        self.image_label.place(x=550, y=225)

        all3 = Label(root, text=" Burnol ", font="times 20 bold", foreground="Black", bg='Silver')
        all3.place(x=550, y=400)

        allt3 = Label(root, text="     Rs. 112.96", font="times 16 bold", foreground="Black", bg='Silver')
        allt3.place(x=550, y=445)

        medi = Button(root, text="Add To cart", bg='white', fg='black', height=1, width=10, font="times 12 bold")
        medi.place(x=570, y=485)

        image_path = r"C:\Users\Abhijit\OneDrive\Desktop\pro\candid.jpg"
        original_image = Image.open(image_path)
        resized_image = original_image.resize((150, 160), Image.BILINEAR)  # Resize image to 200x200
        self.tkinter_image = ImageTk.PhotoImage(resized_image)

        # Display resized image
        self.image_label = Label(root, image=self.tkinter_image)
        self.image_label.place(x=735, y=225)

        all4 = Label(root, text="    Sputral ", font="times 20 bold", foreground="Black", bg='Silver')
        all4.place(x=735, y=400)

        allt4 = Label(root, text="     Rs. 25.92", font="times 16 bold", foreground="Black", bg='Silver')
        allt4.place(x=735, y=445)

        medi = Button(root, text="Add To cart", bg='white', fg='black', height=1, width=10, font="times 12 bold")
        medi.place(x=755, y=485)

        image_path = r"C:\Users\Abhijit\OneDrive\Desktop\pro\candid.jpg"
        original_image = Image.open(image_path)
        resized_image = original_image.resize((150, 160), Image.BILINEAR)  # Resize image to 200x200
        self.tkinter_image = ImageTk.PhotoImage(resized_image)

        # Display resized image
        self.image_label = Label(root, image=self.tkinter_image)
        self.image_label.place(x=920, y=225)

        all5 = Label(root, text="  Candid Burn", font="times 20 bold", foreground="Black", bg='Silver')
        all5.place(x=920, y=400)

        allt5 = Label(root, text="     Rs. 45.30", font="times 16 bold", foreground="Black", bg='Silver')
        allt5.place(x=920, y=445)

        medi = Button(root, text="Add To cart", bg='white', fg='black', height=1, width=10, font="times 12 bold")
        medi.place(x=940, y=485)

    def open_me_cold_cough(self):
        # Close the current window
        self.root.destroy()
        # Open the new page window
        from Medicine_Home import HomePage  # Import the NewPage class from the second script
        root = tk.Tk()
        app = HomePage(root)
        root.geometry("1100x600")
        root.title('NEW_PAGE')
        root.mainloop()

    def open_bact(self):
            self.root.destroy()
            from med_bacterial_infection import DoctorsPage
            new_root = tk.Tk()
            app = DoctorsPage(new_root)
            new_root.geometry("1100x600")
            new_root.title('NEW_PAGE')
            new_root.mainloop()

    def open_bone(self):
            self.root.destroy()
            from med_bone import DoctorsPage
            new_root = tk.Tk()
            app = DoctorsPage(new_root)
            new_root.geometry("1100x600")
            new_root.title('NEW_PAGE')
            new_root.mainloop()

    def open_burns(self):
            self.root.destroy()
            from Med_burns import DoctorsPage
            new_root = tk.Tk()
            app = DoctorsPage(new_root)
            new_root.geometry("1100x600")
            new_root.title('NEW_PAGE')
            new_root.mainloop()

    def open_clean(self):
            self.root.destroy()
            from Med_Cleansers import DoctorsPage
            new_root = tk.Tk()
            app = DoctorsPage(new_root)
            new_root.geometry("1100x600")
            new_root.title('NEW_PAGE')
            new_root.mainloop()

    def open_consti(self):
        self.root.destroy()
        from med_constipation import DoctorsPage
        new_root = tk.Tk()
        app = DoctorsPage(new_root)
        new_root.geometry("1100x600")
        new_root.title('NEW_PAGE')
        new_root.mainloop()

    def open_dryskin(self):
            self.root.destroy()
            from med_dental import DoctorsPage
            new_root = tk.Tk()
            app = DoctorsPage(new_root)
            new_root.geometry("1100x600")
            new_root.title('NEW_PAGE')
            new_root.mainloop()

    def open_dia(self):
            self.root.destroy()
            from med_diabetes import DoctorsPage
            new_root = tk.Tk()
            app = DoctorsPage(new_root)
            new_root.geometry("1100x600")
            new_root.title('NEW_PAGE')
            new_root.mainloop()

    def open_fever(self):
            self.root.destroy()
            from Med_fever import DoctorsPage
            new_root = tk.Tk()
            app = DoctorsPage(new_root)
            new_root.geometry("1100x600")
            new_root.title('NEW_PAGE')
            new_root.mainloop()

    def open_Mal(self):
            self.root.destroy()
            from Med_Malaria import DoctorsPage
            new_root = tk.Tk()
            app = DoctorsPage(new_root)
            new_root.geometry("1100x600")
            new_root.title('NEW_PAGE')
            new_root.mainloop()

    def open_scar(self):
        self.root.destroy()
        from Med_Scar import DoctorsPage
        new_root = tk.Tk()
        app = DoctorsPage(new_root)
        new_root.geometry("1100x600")
        new_root.title('NEW_PAGE')
        new_root.mainloop()

    def open_all(self):
            self.root.destroy()
            from Medicine_allergies import DoctorsPage
            new_root = tk.Tk()
            app = DoctorsPage(new_root)
            new_root.geometry("1100x600")
            new_root.title('NEW_PAGE')
            new_root.mainloop()

    def open_anti(self):
            self.root.destroy()
            from Medicine_antibiotic import DoctorsPage
            new_root = tk.Tk()
            app = DoctorsPage(new_root)
            new_root.geometry("1100x600")
            new_root.title('NEW_PAGE')
            new_root.mainloop()

    def open_asth(self):
            self.root.destroy()
            from Medicine_asthama import DoctorsPage
            new_root = tk.Tk()
            app = DoctorsPage(new_root)
            new_root.geometry("1100x600")
            new_root.title('NEW_PAGE')
            new_root.mainloop()

    def open_ayu(self):
            self.root.destroy()
            from Medicine_Ayu import DoctorsPage
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

    def open_de_list_user(self):
            self.root.destroy()
            from list_dr_user import DoctorsPage
            new_root = tk.Tk()
            app = DoctorsPage(new_root)
            new_root.geometry("1100x600")
            new_root.title('NEW_PAGE')
            new_root.mainloop()


def show_doctors(self, event):
        selected_index = self.categories_listbox.curselection()
        if selected_index:
            selected_category = self.categories_listbox.get(selected_index)
            print(f"Selected category: {selected_category}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DoctorsPage(root)
    root.geometry("1100x600")
    root.title('MEDICINE_HOME')
    root.mainloop()