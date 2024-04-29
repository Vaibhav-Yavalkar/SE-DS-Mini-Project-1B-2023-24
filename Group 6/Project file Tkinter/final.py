from tkinter import *
from tkinter import ttk 
from verification import *
import random
import time
from tkinter import messagebox, filedialog
import sqlite3
import os
import subprocess
import admin_db
import tkinter as tk
import shutil

def on_closing(window):
   if messagebox.askokcancel("Quit", "Do you want to quit?"):
        logout()
        window.destroy()
      
        
def forgot_password(event=None):
    print("Forgot password...")

def create_account():
    login_window.withdraw()  # Hide the login window
    register_window.deiconify()  # Show the register window

def back_to_login():
    register_window.withdraw()  # Hide the register window
    login_window.deiconify()  # Show the login window again

def generate_token():
    return str(random.randint(100000, 999999))
    login_window.after(180000, clear_otp)
    return otp

def clear_otp():
    global otp
    otp = None
    
def register():
    name = name_entry.get()
    role = roles_combobox.get()
    email = email_entry.get()
    password = password_entry_reg.get()
    confirm_password = confirm_entry.get()

    # Check if any input field is empty
    if not all([name, role, email, password, confirm_password]):
        messagebox.showerror("Error", "All fields are required.")
        return

    if password != confirm_password:
        messagebox.showerror("Error", "Password does not match.")
        return

    global otp
    otp = generate_token()

    result = register_user(name, role, email, password, otp)
    
    if result.startswith("Error"):
        messagebox.showerror("Error", result)
        name_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry_reg.delete(0, END)
        roles_combobox.set('')
        confirm_entry.delete(0, END)
    else:
        # messagebox.showinfo("Success", result)
        # If registration is successful, show the OTP window
        otp_window.deiconify()  # Show the OTP window
    
    print("Register account...")

global login_email

def login():
    # close_login()
    global login_email  # Declare login_email as a global variable
    email = email_entry_log.get()
    email = email_entry_log.get()
    login_email = email
    login_password = password_entry_log.get()
    
    # Validate user input
    if not all([email, login_password]):
        messagebox.showerror("Error", "Please enter both email and password.")
        return

    authenticated = authenticate_user(email, login_password)

    if authenticated:
        if is_admin(email):
            close_login()
        elif is_applicant(email):
            close_login_applicant()
        else:
            # User is neither admin nor applicant
            email_entry_log.delete(0, END)
            password_entry_log.delete(0, END)
            close_login()
    else:
        messagebox.showerror("Error", "Invalid email or password. Please try again.")

def close_login():
    # otp_window.withdraw()
    login_window.withdraw()
    # register_window.withdraw()
    home_window.deiconify()
    
def close_login_applicant():
    login_window.withdraw()
    # register_window.withdraw()
    applicant_window.deiconify()
    admin_db.applicant_file(table_submission_app)

def close_otp():
    otp_window.withdraw()
    register_window.withdraw()
    login_window.withdraw()
    window_admin.deiconify() 
    
def verify_otp():
    entered_otp = otp_entry.get()
    if entered_otp == str(otp):
        
        # Get user inputs
        name = name_entry.get()
        role = roles_combobox.get()
        email = email_entry.get()
        password = password_entry_reg.get()
        email_token = secrets.token_urlsafe(16)
        
        # Show success message for OTP verification
        messagebox.showinfo("Success", "OTP Verified Successfully!")
        
        # Connect to the database
        conn = sqlite3.connect('user_database.db')
        c = conn.cursor()
        
        # Insert new user into the database
        c.execute("INSERT INTO users (name, role, email, password, email_token) VALUES (?, ?, ?, ?, ?)",
                (name, role, email, password, email_token))
        
        # Update user table to mark email as verified
        c.execute("UPDATE users SET email_verified = ? WHERE email = ?", (True, email))
        
        # Commit changes and close connection
        conn.commit()
        conn.close()
        
        name_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry_reg.delete(0, END)
        roles_combobox.set('')
        confirm_entry.delete(0, END)
        otp_entry.delete(0, END)
        
        close_otp()
        login_window.deiconify()
    else:
        messagebox.showerror("Error", "Invalid OTP")

def resend():
    email = email_entry.get()
    global otp  
    otp = generate_token()
    
    result2 = resend_otp(email, otp)
    messagebox.showinfo("Success", result2) 

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x_offset = (window.winfo_screenwidth() - width) // 2
    y_offset = (window.winfo_screenheight() - height) // 2
    window.geometry(f"+{x_offset}+{y_offset - 20}")
       
# Login window
login_window = Tk()
login_window.title("Login")
login_window.geometry("800x600")
center_window(login_window)

login_label = Label(login_window, text="Sign in to your account", font=("Arial", 18))
login_label.place(relx=0.5, rely=0.2, anchor=CENTER)

email_label = Label(login_window, text="Email", font=("Arial", 12))
email_label.place(relx=0.3, rely=0.35)
email_frame = Frame(login_window)
email_frame.place(relx=0.3, rely=0.4, relwidth=0.4)
email_entry_log = Entry(email_frame, font=("Arial", 12))
email_entry_log.pack(fill=BOTH, ipadx=5, ipady=5)

password_label = Label(login_window, text="Password", font=("Arial", 12))
password_label.place(relx=0.3, rely=0.5)
password_frame = Frame(login_window)
password_frame.place(relx=0.3, rely=0.55, relwidth=0.4)
password_entry_log = Entry(password_frame, show="*", font=("Arial", 12))
password_entry_log.pack(fill=BOTH, ipadx=5, ipady=5)

forget_label = Label(login_window, text="Forgot Password?", font=("Arial", 10), fg="blue", cursor="hand2")
forget_label.place(relx=0.3, rely=0.6)
forget_label.bind("<Button-1>", forgot_password)

login_button = Button(login_window, text="Login", width=10, font=("Arial", 12), bg="blue", fg="white", padx=10, pady=5, command=login)
login_button.place(relx=0.5, rely=0.75, anchor=CENTER, relwidth=0.4)

create_account_label = Label(login_window, text="Not a member? Create account", font=("Arial", 10), fg="blue", cursor="hand2")
create_account_label.place(relx=0.5, rely=0.85, anchor=CENTER)
create_account_label.bind("<Button-1>", lambda event: create_account())

# login_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(login_window))

# Register window
register_window = Toplevel()
register_window.title("Register")
register_window.geometry("800x600")
center_window(register_window)
register_window.withdraw()  # Hide the register window initially

arrow_img = PhotoImage(file="img/arrow.png")
arrow_img = arrow_img.subsample(4) 

back_arrow_label = Label(register_window, image=arrow_img)
back_arrow_label.place(relx=0.02, rely=0.02, anchor=NW)
back_arrow_label.bind("<Button-1>", lambda event: back_to_login())

register_label = Label(register_window, text="Register Page", font=("Arial", 18))
register_label.place(relx=0.5, rely=0.1, anchor=CENTER)

name_label = Label(register_window, text="Full name", font=("Arial", 12))
name_label.place(relx=0.3, rely=0.2)
name_frame = Frame(register_window)
name_frame.place(relx=0.3, rely=0.25, relwidth=0.4)
name_entry = Entry(name_frame, font=("Arial", 12))
name_entry.pack(fill=BOTH, ipadx=5, ipady=5)

roles_label = Label(register_window, text="Select Role", font=("Arial", 12))
roles_label.place(relx=0.3, rely=0.33)
roles_frame = Frame(register_window)
roles_frame.place(relx=0.45, rely=0.32, relwidth=0.25)
roles_combobox = ttk.Combobox(roles_frame, values=["Applicant", "Staff", "Committee Member","Instructor","admin"], font=("Arial", 12), state="readonly")
roles_combobox.pack(fill=BOTH, ipadx=5, ipady=5)

email_label = Label(register_window, text="Email", font=("Arial", 12))
email_label.place(relx=0.3, rely=0.39)
email_frame = Frame(register_window)
email_frame.place(relx=0.3, rely=0.44, relwidth=0.4)
email_entry = Entry(email_frame, font=("Arial", 12))
email_entry.pack(fill=BOTH, ipadx=5, ipady=5)

password_label = Label(register_window, text="Password", font=("Arial", 12))
password_label.place(relx=0.3, rely=0.5)
password_frame = Frame(register_window)
password_frame.place(relx=0.3, rely=0.55, relwidth=0.4)
password_entry_reg = Entry(password_frame, show="*", font=("Arial", 12))
password_entry_reg.pack(fill=BOTH, ipadx=5, ipady=5)

confirm_label = Label(register_window, text="Confirm password", font=("Arial", 12))
confirm_label.place(relx=0.3, rely=0.6)
confirm_frame = Frame(register_window)
confirm_frame.place(relx=0.3, rely=0.65, relwidth=0.4)
confirm_entry = Entry(confirm_frame, show="*", font=("Arial", 12))
confirm_entry.pack(fill=BOTH, ipadx=5, ipady=5)

register_button = Button(register_window, text="Register", width=10, font=("Arial", 12), bg="blue", fg="white", padx=10, pady=5, command=register)
register_button.place(relx=0.5, rely=0.8, anchor=CENTER)

login_account_label = Label(register_window, text="Already have an account? Log in", font=("Arial", 10), fg="blue", cursor="hand2")
login_account_label.place(relx=0.5, rely=0.9, anchor=CENTER)
login_account_label.bind("<Button-1>", lambda event: back_to_login())

# register_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(login_window))


# OTP verification window
otp_window = Toplevel()
otp_window.title("OTP Verification")
otp_window.geometry("400x200")
center_window(otp_window)
otp_window.withdraw()

otp_label = Label(otp_window, text="", font=("Arial", 12))
otp_label.pack()

otp_entry = Entry(otp_window, font=("Arial", 12))
otp_entry.pack()

verify_button = Button(otp_window, text="Verify OTP", command=verify_otp)
verify_button.pack()

resend_otp_label = Label(otp_window, text="Resend OTP", font=("Arial", 10), fg="blue", cursor="hand2")
resend_otp_label.place(relx=0.27, rely=0.6, anchor=W)
resend_otp_label.bind("<Button-1>", lambda event: resend())



def on_double_click_verified(event):
    print("call")
    selection = table_verified.selection()
    if selection:
        item = selection[0]
        email = table_verified.item(item, "values")[0]
        admin_db.unverify_user(email)
        admin_db.Re_unverified_user(table_verified)
        

def on_double_click_unverified(event):
    print("call")
    selection = table_unverified.selection()
    if selection:
        item = selection[0]
        email = table_unverified.item(item, "values")[0]
        admin_db.verify_user(email)
        admin_db.reload_data(table_unverified)
        

def on_double_click_applicant(event):
    print("on_double_click_applicant")
    selection = table_applicant.selection()
    if selection:           
        item = selection[0]  # Corrected index to 0
        email = table_applicant.item(item, "values")[0]
        print(email)
        cv_result = admin_db.verify_cv(email)
        
        print(cv_result)
        
        if cv_result:
            if os.path.exists(cv_result):
                try:
                    os.startfile(cv_result)
                except Exception as e:
                    print("Error opening CV file:", e)
            else:
                print("CV file does not exist:", cv_result)
        else:
            print("No CV path found for the provided email.")
            
        admin_db.applicant_data(table_applicant)

def show_unverified_frame():
    admin_db.reload_data(table_unverified)
    unverified_window.deiconify()  # Show the Unverified window
    home_window.withdraw()  # Hide the Home window
    verified_window.withdraw()

        
def show_home_frame():
    home_window.deiconify()
    unverified_window.withdraw()  # Hide the Unverified window
    verified_window.withdraw()

def show_verified_frame():
    admin_db.Re_unverified_user(table_verified)
    verified_window.deiconify()
    unverified_window.withdraw()  # Hide the Unverified window
    home_window.withdraw()

def adjust_text_position(event):
    screen_width = applicant_window.winfo_width()
    rel_x = 0.2
    rel_y = 0.3
        
    if text_label.winfo_exists():
        text_width = text_label.winfo_reqwidth()
        x_offset = 0.5 * (1 + rel_x) * screen_width - 0.48 * text_width
        y_offset = 0

        text_label.place(relx=rel_x, rely=rel_y, anchor=tk.CENTER, x=x_offset, y=y_offset)

def logout():
    global login_email  # Declare login_email as a global variable
    login_mail_result = logout_user(login_email)
    login_email = None  # Reset login_email after logout
    print("Logged out successfully")
    login_window.deiconify()
    
    otp_window.withdraw()
    register_window.withdraw()
    applicant_window.withdraw()
    home_window.withdraw()
    deep_learning.withdraw()
    submission_window.withdraw()
    verified_window.withdraw()


home_window = Toplevel()
home_window.title("Home")
home_window.geometry("800x600")
center_window(home_window)
home_window.withdraw()  # Hide the Home window

frame_home = Frame(home_window)
frame_home.pack(fill=BOTH, expand=True)

# Create a navigation bar frame
navbar_frame_home = Frame(frame_home, bd=1, relief=SUNKEN)
navbar_frame_home.pack(side=TOP, fill=X)

# Create a bottom border for the navbar
bottom_border = Frame(navbar_frame_home, height=1, bg="black")
bottom_border.pack(side=BOTTOM, fill=X)

logo_image_home = PhotoImage(file="img/logo.png")
logo_image_home = logo_image_home.subsample(4)
logo_label = Label(navbar_frame_home, image=logo_image_home)
logo_label.pack(side=LEFT)

# Add navigation buttons to the navbar frame
logout_button = Button(navbar_frame_home, text="Logout",  command=logout)
logout_button.pack(side=RIGHT, padx=5, pady=10)

verified_button = Button(navbar_frame_home, text="Verified",  command=show_verified_frame)
verified_button.pack(side=RIGHT, padx=5, pady=10)

unverifed_button = Button(navbar_frame_home, text="Unverifed", command=show_unverified_frame)
unverifed_button.pack(side=RIGHT, padx=5, pady=10)

courses_button = Button(navbar_frame_home, text="Courses")
courses_button.pack(side=RIGHT, padx=5, pady=10)

application_button = Button(navbar_frame_home, text="Application", command=show_home_frame)
application_button.pack(side=RIGHT, padx=5, pady=10)

# From

def on_enter_applicant(event):
    applicant_label.config(relief=FLAT)  # Remove border when mouse enters

def on_leave_applicant(event):
    applicant_label.config(relief=SOLID, borderwidth=1)  # Add border when mouse leaves
    
applicant_label = Label(frame_home, text="Applicant", font=("Arial", 18),relief=SOLID, borderwidth=1)
applicant_label.pack(padx=1, pady=10)

# Bind events for hover effect
applicant_label.bind("<Enter>", on_enter_applicant)
applicant_label.bind("<Leave>", on_leave_applicant)


# Define columns
columns_applicant = ("Email", "Course Name", "Experience", "cv")

# Create the treeview with columns for unverified users
table_applicant = ttk.Treeview(frame_home, columns=columns_applicant, show="headings")

# Define column headings for unverified users
for col in columns_applicant:
    table_applicant.heading(col, text=col)

# Configure the treeview to stretch columns and fill the whole width for unverified users
for col in columns_applicant:
    table_applicant.column(col, stretch=True)

# Define tag configuration for unverified users
table_applicant.tag_configure("unverified", background="light gray")

# Define action for verifying user for unverified users
table_applicant.bind("<Double-1>", on_double_click_applicant)

# Pack the table to fill both width and height of the window for unverified users
table_applicant.pack(fill="both", expand=True)

admin_db.applicant_data(table_applicant)


home_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(login_window))
# till




# Unverified Window
unverified_window = Toplevel()
unverified_window.title("Unverified")
unverified_window.geometry("800x600")
center_window(unverified_window)
unverified_window.withdraw()

frame_unverified = Frame(unverified_window)
frame_unverified.pack(fill=BOTH, expand=True)

navbar_frame_unverified = Frame(frame_unverified, bd=1, relief=SUNKEN)
navbar_frame_unverified.pack(side=TOP, fill=X)

# Create a bottom border for the navbar
bottom_border = Frame(navbar_frame_unverified, height=1, bg="black")
bottom_border.pack(side=BOTTOM, fill=X)

logo_image_unverified = PhotoImage(file="img/logo.png")
logo_image_unverified = logo_image_unverified.subsample(4)
logo_label = Label(navbar_frame_unverified, image=logo_image_unverified)
logo_label.pack(side=LEFT)

logout_button = Button(navbar_frame_unverified, text="Logout",  command=logout)
logout_button.pack(side=RIGHT, padx=5, pady=10)

verified_button = Button(navbar_frame_unverified, text="Verified",  command=show_verified_frame)
verified_button.pack(side=RIGHT, padx=5, pady=10)

unverifed_button = Button(navbar_frame_unverified, text="Unverifed", command=show_unverified_frame)
unverifed_button.pack(side=RIGHT, padx=5, pady=10)

courses_button = Button(navbar_frame_unverified, text="Courses")
courses_button.pack(side=RIGHT, padx=5, pady=10)

application_button = Button(navbar_frame_unverified, text="Application", command=show_home_frame)
application_button.pack(side=RIGHT, padx=5, pady=10)


def on_enter(event):
    unverified_label.config(relief=FLAT)  # Remove border when mouse enters

def on_leave(event):
    unverified_label.config(relief=SOLID, borderwidth=1)  # Add border when mouse leaves



# Create the submission label with initial border
unverified_label = Label(frame_unverified, text="Unverified account", font=("Arial", 18),relief=SOLID, borderwidth=1)
unverified_label.pack(padx=1, pady=10)

# Bind events for hover effect
unverified_label.bind("<Enter>", on_enter)
unverified_label.bind("<Leave>", on_leave)


# Define columns
columns_unverified = ("Email", "Name", "Role", "Action")

# Create the treeview with columns for unverified users
table_unverified = ttk.Treeview(frame_unverified, columns=columns_unverified, show="headings")

# Define column headings for unverified users
for col in columns_unverified:
    table_unverified.heading(col, text=col)

# Configure the treeview to stretch columns and fill the whole width for unverified users
for col in columns_unverified:
    table_unverified.column(col, stretch=True)

# Define tag configuration for unverified users
table_unverified.tag_configure("unverified", background="light gray")

# Define action for verifying user for unverified users
table_unverified.bind("<Double-1>", on_double_click_unverified)

# Pack the table to fill both width and height of the window for unverified users
table_unverified.pack(fill="both", expand=True)

admin_db.reload_data(table_unverified)


unverified_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(login_window))




# Verified Window
verified_window = Toplevel()
verified_window.title("Verified")
verified_window.geometry("800x600")
center_window(verified_window)
verified_window.withdraw()

verified_frame = Frame(verified_window)
verified_frame.pack(fill=BOTH, expand=True)

navbar_frame_verified = Frame(verified_frame, bd=1, relief=SUNKEN)
navbar_frame_verified.pack(side=TOP, fill=X)

# Create a bottom border for the navbar
bottom_border = Frame(navbar_frame_verified, height=1, bg="black")
bottom_border.pack(side=BOTTOM, fill=X)


logo_image_verified = PhotoImage(file="img/logo.png")
logo_image_verified = logo_image_verified.subsample(4)
logo_label_verified = Label(navbar_frame_verified, image=logo_image_verified)
logo_label_verified.pack(side=LEFT)


logout_button = Button(navbar_frame_verified, text="Logout",  command=logout)
logout_button.pack(side=RIGHT, padx=5, pady=10)

verified_button = Button(navbar_frame_verified, text="Verified",  command=show_verified_frame)
verified_button.pack(side=RIGHT, padx=5, pady=10)

unverifed_button = Button(navbar_frame_verified, text="Unverifed", command=show_unverified_frame)
unverifed_button.pack(side=RIGHT, padx=5, pady=10)

courses_button = Button(navbar_frame_verified, text="Courses")
courses_button.pack(side=RIGHT, padx=5, pady=10)

application_button = Button(navbar_frame_verified, text="Application", command=show_home_frame)
application_button.pack(side=RIGHT, padx=5, pady=10)


def on_enter(event):
    submission_label.config(relief=FLAT)  # Remove border when mouse enters

def on_leave(event):
    submission_label.config(relief=SOLID, borderwidth=1)  # Add border when mouse leaves



# Create the submission label with initial border
submission_label = Label(verified_frame, text="Verified Account", font=("Arial", 18),relief=SOLID, borderwidth=1)
submission_label.pack(padx=1, pady=10)

# Bind events for hover effect
submission_label.bind("<Enter>", on_enter)
submission_label.bind("<Leave>", on_leave)


# Define columns for verified users
columns_verified = ("Email", "Name", "Role", "Action")
table_verified = ttk.Treeview(verified_frame, columns=columns_verified, show="headings")

# Define column headings for verified users
for col in columns_verified:
    table_verified.heading(col, text=col)

# Configure the treeview to stretch columns and fill the whole width for verified users
for col in columns_verified:
    table_verified.column(col, stretch=True)

# Define action for verifying user for verified users
table_verified.bind("<Double-1>", on_double_click_verified)

# Pack the table to fill both width and height of the window for verified users
table_verified.pack(fill="both", expand=True)

# Load data initially for verified users
admin_db.Re_unverified_user(table_verified)

verified_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(login_window))



def on_frame_enter(event):
    frame = event.widget
    frame.config(bg="light blue")
    if hasattr(frame, 'label'):
        frame.label.config(bg="light blue")
    if hasattr(frame, 'definition_label'):
        frame.definition_label.config(bg="light blue")

def on_frame_leave(event):
    frame = event.widget
    frame.config(bg="white")
    if hasattr(frame, 'label'):
        frame.label.config(bg="white")
    if hasattr(frame, 'definition_label'):
        frame.definition_label.config(bg="white")

def create_border_frame(parent, pady):
    frame = tk.Frame(parent, highlightbackground="light blue", highlightthickness=1, padx=10, pady=10, bg="white")
    frame.pack(fill=tk.BOTH, padx=10, pady=pady)
    return frame

def on_button_enter(event):
    event.widget.config(bg="light blue")

def on_button_leave(event):
    event.widget.config(bg="white")

def on_button_click(event, frame_number):
    frame_functions = {
        1: deep_learning_function,
        2: applied_science_function,
        3: machine_learning_function,
        4: database_management_function
    }
    if frame_number in frame_functions:
        frame_functions[frame_number]()

def deep_learning_function():
    applicant_window.withdraw()  # Hide the login window
    deep_learning.deiconify()

def applied_science_function():
    print("Applied Science function called")

def machine_learning_function():
    print("Machine Learning function called")

def database_management_function():
    print("Database Management function called")



def on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    sub_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
def deep_on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    deep_canvas.yview_scroll(int(-1*(event.delta/120)), "units")



# Function to handle "Submission" button click
def submission_button_click():
    submission_window.deiconify()
    admin_db.applicant_file(table_submission_app)
    admin_db.applicant_data(table_applicant)
    applicant_window.withdraw()
    deep_learning.withdraw()

def career_button_click():
    applicant_window.deiconify()
    submission_window.withdraw() 
    deep_learning.withdraw()

def create_frame(frame, frame_number, label_text, definition_text):
    label = Label(frame, text=label_text, font=("Arial", 16))
    label.grid(row=0, column=0, sticky="w")
    frame.label = label  

    definition = Label(frame, text=definition_text, font=("Arial", 12))
    definition.grid(row=0, column=1, sticky="w")
    frame.definition_label = definition

    button = Button(frame, text="Apply Now →", font=("Arial", 12))
    button.grid(row=1, column=0, sticky="w", pady=10)
    button.bind("<Enter>", on_button_enter)
    button.bind("<Leave>", on_button_leave)
    button.bind("<Button-1>", lambda event, num=frame_number: on_button_click(event, num))


    
applicant_window = Toplevel()
applicant_window.title("Applicant")
applicant_window.geometry("800x600")
center_window(applicant_window)
applicant_window.withdraw()

nav_bar = Frame(applicant_window, bg="light blue", height=50)
nav_bar.pack(fill=X)

logo_image = PhotoImage(file="img/logo.png")
logo_image = logo_image.subsample(4)
logo_label = Label(nav_bar, image=logo_image)
logo_label.pack(side=LEFT, padx=10, pady=10)

logout_button = Button(nav_bar, text="Logout", font=("Arial", 12), command=logout)
logout_button.pack(side=RIGHT, padx=5, pady=10)

submission_button = Button(nav_bar, text="Submission", font=("Arial", 12), command=submission_button_click)
submission_button.pack(side=RIGHT, padx=5, pady=10)

career_button = Button(nav_bar, text="Career", font=("Arial", 12), command=career_button_click)
career_button.pack(side=RIGHT, padx=5, pady=10)

frame_home = Frame(applicant_window)
frame_home.pack(fill=BOTH, expand=True)

scrollbar =Scrollbar(frame_home, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

canvas = Canvas(frame_home, yscrollcommand=scrollbar.set)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar.config(command=canvas.yview)

inner_frame = Frame(canvas)

image_path = "img/bg_img.png"
img = PhotoImage(file=image_path)
img_label = Label(inner_frame, image=img)
img_label.pack()

text = "Join Our Team as a Teaching Assistant at Florida Atlantic University\nExplore exciting opportunities to contribute to academic excellence! We're seeking\n dedicated individuals passionate about education to join us as Teaching Assistants\n at North University. Shape the future of learning and inspire students on their\n educational journey. Apply now to be a part of our dynamic team!"
text_label = Label(inner_frame, text=text, bg="white", font=("Arial", 14, "bold"))
text_label.pack()

applicant_window.bind("<Configure>", adjust_text_position)

heading_frame = Frame(inner_frame)
heading_frame.pack(side=TOP, fill=BOTH, padx=15, pady=25)

heading_border_frame = Frame(heading_frame, highlightbackground="black", highlightthickness=1, padx=5, pady=5)
heading_border_frame.pack(side=LEFT)

heading_label = Label(heading_border_frame, text="Open Positions", font=("Arial", 18))
heading_label.pack()

button_frame = Frame(inner_frame)
button_frame.pack(side=BOTTOM, fill=BOTH, padx=10, pady=10, anchor=E, expand=True)

deep_learning_frame = create_border_frame(button_frame, pady=20)
applied_science_frame = create_border_frame(button_frame, pady=20)
machine_learning_frame = create_border_frame(button_frame, pady=20)
database_management_frame = create_border_frame(button_frame, pady=20)

for frame in (deep_learning_frame, applied_science_frame, machine_learning_frame, database_management_frame):
    frame.bind("<Enter>", on_frame_enter)
    frame.bind("<Leave>", on_frame_leave)

create_frame(applied_science_frame, 1, "Applied Science", "Applied science is the application of scientific knowledge to practical purposes.")
create_frame(machine_learning_frame, 2, "Machine Learning", "Machine learning is the study of algorithms that improve automatically through experience.")
create_frame(database_management_frame, 3, "Database Management System", "A database management system (DBMS) is a software for managing databases.")

canvas.create_window((0, 0), window=inner_frame, anchor="nw")
canvas.update_idletasks()

canvas.config(scrollregion=canvas.bbox("all"))
canvas.bind_all("<MouseWheel>", on_mousewheel)


applicant_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(login_window))


# from here


submission_window = Toplevel()
submission_window.title("Home")
submission_window.geometry("800x600")
center_window(submission_window)
submission_window.withdraw()  # Hide the Home window

frame_submission = Frame(submission_window)
frame_submission.pack(fill=BOTH, expand=True)

# Create a navigation bar frame
navbar_frame_sub = Frame(frame_submission, bd=1, relief=SUNKEN)
navbar_frame_sub.pack(side=TOP, fill=X)

# Create a bottom border for the navbar
bottom_border = Frame(navbar_frame_sub, height=1, bg="black")
bottom_border.pack(side=BOTTOM, fill=X)

logo_image_home = PhotoImage(file="img/logo.png")
logo_image_home = logo_image_home.subsample(4)
logo_label = Label(navbar_frame_sub, image=logo_image_home)
logo_label.pack(side=LEFT)

# Add navigation buttons to the navbar frame
logout_button = Button(navbar_frame_sub, text="Logout", font=("Arial", 12), command=logout)
logout_button.pack(side=RIGHT, padx=5, pady=10)

submission_button = Button(navbar_frame_sub, text="Submission", font=("Arial", 12), command=submission_button_click)
submission_button.pack(side=RIGHT, padx=5, pady=10)

career_button = Button(navbar_frame_sub, text="Career", font=("Arial", 12), command=career_button_click)
career_button.pack(side=RIGHT, padx=5, pady=10)



def on_enter_sub(event):
    applicant_label.config(relief=FLAT)  # Remove border when mouse enters

def on_leave_sub(event):
    applicant_label.config(relief=SOLID, borderwidth=1)  # Add border when mouse leaves
    
applicant_label = Label(frame_submission, text="Applicant", font=("Arial", 18),relief=SOLID, borderwidth=1)
applicant_label.pack(padx=1, pady=10)

# Bind events for hover effect
applicant_label.bind("<Enter>", on_enter_sub)
applicant_label.bind("<Leave>", on_leave_sub)


# Define columns
columns_applicant = ("Email", "Course Name", "Experience", "cv")

# Create the treeview with columns for unverified users
table_submission_app = ttk.Treeview(frame_submission, columns=columns_applicant, show="headings")

# Define column headings for unverified users
for col in columns_applicant:
    table_submission_app.heading(col, text=col)

# Configure the treeview to stretch columns and fill the whole width for unverified users
for col in columns_applicant:
    table_submission_app.column(col, stretch=True)

# Define tag configuration for unverified users
table_submission_app.tag_configure("unverified", background="light gray")

# Define action for verifying user for unverified users
table_submission_app.bind()

# Pack the table to fill both width and height of the window for unverified users
table_submission_app.pack(fill="both", expand=True)

admin_db.applicant_file(table_submission_app)


submission_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(login_window))



# till


cv_path = None

def browse_cv():
    global cv_path
    cv_file = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if cv_file:
        cv_path = cv_file 
        
def check_duplicate(email, course_name):
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM applicants WHERE email = ? AND course_name = ?''', (email, course_name))
    result = c.fetchone()
    conn.close()
    return result

def submit_form():
    global cv_path
    global login_email  # Declare login_email as a global variable
    
    cv_path_value = cv_path
    if cv_path_value:
        # Create the cv_folder if it doesn't exist
        if not os.path.exists("cv_folder"):
            os.makedirs("cv_folder")

        # Fetch name from users table based on login_email
        conn = sqlite3.connect('user_database.db')
        c = conn.cursor()
        c.execute("SELECT name FROM users WHERE email = ?", (login_email,))
        result = c.fetchone()
        conn.close()

        
        
        if result:
            
            name = result[0]  # Extracting name from the result
            experience = ta_var.get()

            existing_record = check_duplicate(login_email, "Deep Learning")
            
            if not existing_record:
                
                 # Move the CV file to the cv_folder
                cv_filename = os.path.basename(cv_path_value)
                target_path = os.path.join("cv_folder", cv_filename)
                shutil.copy(cv_path_value, target_path)
                
                # Insert applicant information into the applicants table
                conn = sqlite3.connect('user_database.db')
                c = conn.cursor()
                c.execute('''INSERT INTO applicants (name, email, cv_path, experience, course_name) 
                            VALUES (?, ?, ?, ?, ?)''', (name, login_email, target_path, experience, "Deep Learning"))
                conn.commit()
                conn.close()

               
        
                messagebox.showinfo("Success", "Form submitted successfully!")
            else:
                messagebox.showerror("Error", "A user with the same email and course name already exists.")
        else:
            messagebox.showerror("Error", "User not found for the given email.")
    else:
        messagebox.showerror("Error", "Please select a CV file.")
        

# deep learning

# Create the Deep Learning window
deep_learning = Toplevel()
deep_learning.title("Deep Learning")
deep_learning.geometry("800x600")
center_window(deep_learning)
deep_learning.withdraw()


deep_nav_bar = Frame(deep_learning, bg="light blue", height=50)
deep_nav_bar.pack(fill=X)

deep_logo_image = PhotoImage(file="img/logo.png")
deep_logo_image = deep_logo_image.subsample(4)
deep_logo_label = Label(deep_nav_bar, image=deep_logo_image)
deep_logo_label.pack(side=LEFT, padx=10, pady=10)

logout_button = Button(deep_nav_bar, text="Logout", font=("Arial", 12), command= logout)
logout_button.pack(side=RIGHT, padx=5, pady=10)

submission_button = Button(deep_nav_bar, text="Submission", font=("Arial", 12), command=submission_button_click)
submission_button.pack(side=RIGHT, padx=5, pady=10)

career_button = Button(deep_nav_bar, text="Career", font=("Arial", 12), command=career_button_click)
career_button.pack(side=RIGHT, padx=5, pady=10)

# Deep Learning Frame
deeplearning_frame = Frame(deep_learning)
deeplearning_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

# Scrollbar for the Deep Learning Frame
deep_scrollbar = Scrollbar(deeplearning_frame, orient=VERTICAL)
deep_scrollbar.pack(side=RIGHT, fill=Y)

# Canvas for Deep Learning Frame
deep_canvas = Canvas(deeplearning_frame, yscrollcommand=deep_scrollbar.set)
deep_canvas.pack(side=LEFT, fill=BOTH, expand=True)

# Configure Scrollbar
deep_scrollbar.config(command=deep_canvas.yview)

# Frame for Scrollable Content
deep_inner_frame = Frame(deep_canvas)
deep_canvas.create_window((0, 0), window=deep_inner_frame, anchor="nw")

# Bind Mousewheel Event
deep_canvas.bind_all("<MouseWheel>", deep_on_mousewheel)

# Form Labels and Entry Widgets
label1 = Label(deep_inner_frame, text="Are you a passionate deep learning enthusiast?", font=("Arial", 14, "bold"), anchor="w")
label1.pack(pady=(20, 10), anchor="w")

label2_text = "Unlock the next level of your career by becoming a vital part of our cutting-edge Deep Learning team at North University. We're on the lookout for skilled individuals well-versed in frameworks like TensorFlow and PyTorch, with a strong background in neural networks and machine learning algorithms."
label2 = Label(deep_inner_frame, text=label2_text, font=("Arial", 12), wraplength=600, justify=LEFT, anchor="w")
label2.pack(pady=(0, 10), anchor="w")

label3 = Label(deep_inner_frame, text="Requirements", font=("Arial", 12, "bold"), anchor="w")
label3.pack(anchor="w")

requirements = [
    "Proficiency in Python programming",
    "Extensive knowledge of deep learning frameworks (TensorFlow, PyTorch)",
    "Hands-on experience with neural networks and machine learning algorithms",
    "Strong problem-solving skills in the realm of AI",
    "Ability to collaborate effectively with a multidisciplinary team"
]

for req in requirements:
    label = Label(deep_inner_frame, text=f"• {req}", font=("Arial", 12), wraplength=600, justify=LEFT, anchor="w")
    label.pack(anchor="w")

# Attach CV
attach_label = Label(deep_inner_frame, text="Attach your CV", font=("Arial", 14), anchor="w")
attach_label.pack(anchor="w", pady=(20, 10))

cv_frame = Frame(deep_inner_frame)
cv_frame.pack(anchor="w")

cv_button = Button(cv_frame, text="Browse", font=("Arial", 10),  command=browse_cv)
cv_button.pack(side=LEFT, padx=(5, 0))

# TA Experience
ta_experience_label = Label(deep_inner_frame, text="Do you have experience working as a TA at North University?", font=("Arial", 12), anchor="w")
ta_experience_label.pack(anchor="w")

ta_var = IntVar()
ta_yes = Radiobutton(deep_inner_frame, text="Yes", variable=ta_var, value=1, font=("Arial", 12), anchor="w")
ta_no = Radiobutton(deep_inner_frame, text="No", variable=ta_var, value=0, font=("Arial", 12), anchor="w")
ta_yes.pack(anchor="w")
ta_no.pack(anchor="w")

# Form Buttons
# submit_button = Button(deep_inner_frame, text="Submit", font=("Arial", 12), command=submit_form)
submit_button = Button(deep_inner_frame, text="Submit", command=submit_form)

submit_button.pack(pady=20, anchor="w")


# Set Scrollregion
deep_inner_frame.update_idletasks()
deep_canvas.config(scrollregion=deep_canvas.bbox("all"))

deep_learning.protocol("WM_DELETE_WINDOW", lambda: on_closing(login_window))

login_window.mainloop()