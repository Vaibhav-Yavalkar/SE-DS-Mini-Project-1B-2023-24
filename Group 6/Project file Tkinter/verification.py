import smtplib
import sqlite3
import secrets


def register_user(name, role, email, password, otp):
    email_token = secrets.token_urlsafe(16)

    # Connect to the database
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()

    # Check if the user already exists with any role
    c.execute("SELECT * FROM users WHERE email = ?", (email,))
    existing_user = c.fetchone()

    if existing_user:
        # If the user already exists, check if they are trying to register with a different role
        if existing_user[1] != role:  # Assuming role is in the 1st column
            conn.close()
            return "Error: User with the same email already exists with a different role."

        # If the existing user is already an admin, disallow registration with any other role
        if existing_user[1] == 'admin':  # Assuming 'admin' is the role of the admin user
            conn.close()
            return "Error: User with the same email already exists as an admin."

        # If the existing user is not an admin and is not verified, update their data and send verification
        if not existing_user[6]:  # Assuming email_verified is in the 6th column
            c.execute("UPDATE users SET name = ?, role = ?, password = ?, email_token = ? WHERE email = ?",
                      (name, role, password, email_token, email))
            conn.commit()
            conn.close()
            # Send email verification
            send_email_verification(email, otp)
            return "User already exists but is not verified. Check email for verification."

        conn.close()
        return "Error: User with the same email already exists and is verified."

    # Send email verification
    send_email_verification(email, otp)

    return "Registration successful."

def send_email_verification(email, otp):
    sender_email = 'sayyednouman02@gmail.com'  
    sender_password = 'bwrttnynfwcmzfjo'       
    
    # Initialize SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    
    # Compose email
    receiver_email = email
    subject = 'Email Verification'
    body = f'Enter this otp to verify your email: verify_email\n\n{otp}'
    message = f'Subject: {subject}\n\n{body}'
    
    # Send email
    server.sendmail(sender_email, receiver_email, message)

    # Quit server
    server.quit()

def resend_otp(email, otp):
    # Send email verification with the provided OTP
    send_email_verification(email, otp)
    return "New OTP sent successfully. Please check your email to verify your account."

def authenticate_user(email, password):
    # Connect to the database
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()

    # Query the database to find the user with the provided email and password
    c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    user = c.fetchone()

    if user:
        if user[2] == 'admin':  # Assuming role is in the 2nd column
            # If the user is an admin, allow login and verify the account
            c.execute("UPDATE users SET login_status = 1, user_verified = 1 WHERE email = ?", (email,))
            conn.commit()
            conn.close()
            return True
        elif user[7]:  # Assuming user_verified is in the 6th column
            # If the user is not an admin but the account is verified, allow login
            c.execute("UPDATE users SET login_status = 1 WHERE email = ?", (email,))
            conn.commit()
            conn.close()
            return True
        else:
            # If the user is not an admin and the account is not verified, deny login
            conn.close()
            return False
    else:
        # If no user is found with the provided email and password, deny login
        conn.close()
        return False
    
    
def is_admin(email):
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()
    c.execute("SELECT role FROM users WHERE email = ?", (email,))
    result = c.fetchone()
    conn.close()
    if result and result[0] == 'admin':
        return True
    else:
        return False

def is_applicant(email):
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()
    c.execute("SELECT role FROM users WHERE email = ?", (email,))
    result = c.fetchone()
    conn.close()
    if result and result[0] == 'applicant':
        return True
    else:
        return False

def logout_user(email):
    if email:
        conn = sqlite3.connect('user_database.db')
        c = conn.cursor()
        c.execute("UPDATE users SET login_status = 0 WHERE email = ?", (email,))
        conn.commit()
        conn.close()
        print("Logged out successfully")
    else:
        print("No user logged in")
        