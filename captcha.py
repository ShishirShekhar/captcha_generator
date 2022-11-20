# Import all required module
from tkinter import Tk, PhotoImage, Entry, Label, Button, messagebox
import random


# Create a function to run the captcha window
def captcha(login_window):
    # Destroy the login window
    login_window.destroy()
    # Create the window
    window = Tk()
    # Add window title
    window.title("Captcha")
    # Add window size
    window.geometry('800x500')

    # Create a list of name and picture of letters
    data = [
        ['infinite', PhotoImage(file='./images/infinite.png').zoom(7).subsample(10)],
        ['b1a4', PhotoImage(file='./images/b1a4.png').zoom(7).subsample(10)],
        ['smwm', PhotoImage(file='./images/smwm.png').zoom(7).subsample(10)]
    ]

    # Run a new captcha on the window
    new_captcha(window, data)
    # Update the screen
    window.mainloop()


# Create a function to run the new captcha on the window
def new_captcha(window, data):
    # Select an item from the data list
    question = random.choice(data)
    # Get the word from the list
    word = question[0]
    # Get the image from the list
    image = question[1]

    # Generate the display
    generate_display(window, data, word, image)


# Create a function to generate the display
def generate_display(window, data, word, image):
    # Add captcha image to the screen
    image_label = Label(window)
    image_label.config(image=image)
    image_label.place(x=250, y=50)

    # Create a button to start new captcha
    new_word = Button(window, text="New Word", command=lambda: new_captcha(window, data), width=17)
    new_word.place(x=300, y=220)

    # Take the input from the user
    user_word = Entry(window)
    user_word.insert(0, "Enter the captcha")
    user_word.place(x=300, y=250)

    # Create a submit button and check if player input is correct or not
    submit_button = Button(window, text="Submit",
                           command=lambda: check(window, word, user_word),
                           width=17)
    submit_button.place(x=300, y=280)


# Create a function to check the player input
def check(window, word, user_word):
    # Check if word matches or not
    if user_word.get().lower() == word:
        # Show a message
        messagebox.showinfo("Captcha", "Login Successful")
        window.destroy()
    else:
        # Show the error and destroy the window
        messagebox.showerror("Captcha", "Only humans are allowed!")

