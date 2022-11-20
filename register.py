# Import all the required modules
from tkinter import Tk, Label, Entry, Button, messagebox
import sqlite3 as sql

# Create a function to create the new user window
def register():
    # Create the login window
    window = Tk()
    # Set the title of the login window
    window.title("Register")
    # Set the size of the login window
    window.geometry("600x400")
    
    # Create a list to store the data
    data = []
    
    # Create a label for name
    name_label = Label(window, text="Name:")
    name_label.place(x=50, y=50)
    # Create an entry for name
    name_entry = Entry(window, width=20)
    name_entry.place(x=200, y=50)
    # Append the name
    data.append(name_entry)
    
    # Create a label for email
    email_label = Label(window, text="Email:")
    email_label.place(x=50, y=100)
    # Create an entry for email
    email_entry = Entry(window, width=20)
    email_entry.place(x=200, y=100)
    # Append the email
    data.append(email_entry)
        
    # Create a label for Username
    username_label = Label(window, text="Username:")
    username_label.place(x=50, y=150)
    # Create an entry for Username
    username_entry = Entry(window, width=20)
    username_entry.place(x=200, y=150)
    # Append the Username
    data.append(username_entry)
    
    # Create a label for password
    password_label = Label(window, text="Password:")
    password_label.place(x=50, y=200)
    # Create an entry for password
    password_entry = Entry(window, width=20)
    password_entry.place(x=200, y=200)
    # Append the password
    data.append(password_entry)
    
    # Create a button to register
    register_btn = Button(window, text="Register", command=lambda: check_register(window, data))
    register_btn.place(x=200, y=300, width=200)
    
    # Run the login window
    window.mainloop()
    
# Create a function to register the user
def check_register(window, data):
    try:
        # Connect to the database
        db = sql.connect(database="user.db")
        # Create a cursor
        cur = db.cursor()
        
        # Create a table if not exits
        cur.execute("CREATE TABLE IF NOT EXISTS User (name TEXT, email TEXT, username TEXT password TEXt)")
        # Insert the data into the table
        cur.execute(f"INSERT INTO User (name, email, username, password) VALUES('{data[0].get()}', '{data[1].get()}', '{data[2].get()}', '{data[3].get()}')")
        # Commit the changes
        db.commit()
        
        # Show a message
        messagebox.showinfo("Success", "You have successfully registered")
        
        # Close the window
        window.destroy()
    except Exception as e:
        print(e)
        messagebox.showerror("Error", "Something went wrong")
