import sqlite3
import os

def verify_user(email):
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()
    c.execute("UPDATE users SET user_verified = ? WHERE email = ?", (True, email))
    conn.commit()  # Commit the changes to the database
    print(f"User with email {email} verified")
    conn.close()  # Close database connection

def reload_data(table):
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()
    # Clear the current table
    table.delete(*table.get_children())

    # Fetch data from users table excluding admin emails
    c.execute("SELECT email, name, role FROM users WHERE user_verified = 0 AND role != 'admin'")  
    rows = c.fetchall()

    # Insert data into the table
    for row in rows:
        email, name, role = row
        table.insert("", "end", values=(email, name, role, "Verify"), tags=("unverified",)) 
    conn.close()  # Close database connection



def unverify_user(email):
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()
    c.execute("UPDATE users SET user_verified = ? WHERE email = ?", (False, email))
    conn.commit()  # Commit the changes to the database
    print(f"User with email {email} unverified")
    conn.close()  # Close database connection


def Re_unverified_user(table):
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()
    # Clear the current table
    table.delete(*table.get_children())

    # Fetch data from users table excluding admin emails
    c.execute("SELECT email, name, role FROM users WHERE user_verified = 1 AND role != 'admin'")  
    rows = c.fetchall()

    # Insert data into the table
    for row in rows:
        email, name, role = row
        table.insert("", "end", values=(email, name, role, "unverified"), tags=("unverified",)) 
    conn.close()
    

def applicant_data(table):
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()
    # Clear the current table
    table.delete(*table.get_children())

    # Fetch data from applicants table
    c.execute("SELECT Email, Course_Name, Experience, cv_path FROM applicants")
    rows = c.fetchall()

    # Insert data into the table
    for row in rows:
        email,course_name, experience, cv_path = row
        table.insert("", "end", values=(email, course_name, experience, "CV"))
    
    conn.close() # Close database connection
    

def verify_cv(email):
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()

    # Fetch CV path from applicants table based on email
    c.execute("SELECT cv_path FROM applicants WHERE email = ?", (email,))
    result = c.fetchone()
    
    conn.close()

    if result:
        cv_path = result[0]
        if os.path.exists(cv_path):
            return cv_path
        else:
            print("CV file not found.")
            return None
    else:
        print("No applicant found with the provided email.")
        return None


def applicant_file(table):
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()
    # Clear the current table
    table.delete(*table.get_children())

    # Fetch email from users table where login_status is true
    c.execute("SELECT email FROM users WHERE login_status = 1")
    result = c.fetchone()

    if result:
        email = result[0]
        # Fetch data from applicants table based on email
        c.execute("SELECT Email, Course_Name, Experience, cv_path FROM applicants WHERE Email = ?", (email,))
        rows = c.fetchall()

        # Insert data into the table
        for row in rows:
            email, course_name, experience, cv_path = row
            table.insert("", "end", values=(email, course_name, experience, "CV"))
    else:
        print("No user found with login status true.")

    conn.close()

