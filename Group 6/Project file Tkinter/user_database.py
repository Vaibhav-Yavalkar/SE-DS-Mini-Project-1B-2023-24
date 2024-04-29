import sqlite3

# Create a SQLite database
conn = sqlite3.connect('user_database.db')
c = conn.cursor()

# Modify the users table to add a login_status column
c.execute('''CREATE TABLE IF NOT EXISTS users (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             role TEXT NOT NULL,
             email TEXT NOT NULL,
             password TEXT NOT NULL,
             email_token TEXT NOT NULL,
             email_verified INTEGER DEFAULT 0,
             user_verified INTEGER DEFAULT 0,
             login_status INTEGER DEFAULT 0)''')

# Commit changes to the users table
conn.commit()

# Create a new table to store applicant information
c.execute('''CREATE TABLE IF NOT EXISTS applicants (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             email TEXT NOT NULL,
             cv_path TEXT NOT NULL,
             experience INTEGER NOT NULL,
             course_name TEXT NOT NULL)''')


# Commit changes to the applicants table
conn.commit()

# Close connection to the database
conn.close()
