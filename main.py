import random
import tkinter.messagebox
from tkinter import *
from data import letters, numbers, symbols
import pyperclip

# ---------------------------- CONSTANTS -----------------------------------#
WEBSITE_EMAIL_WIDTH = 65
PASSWORD_ENTRY_WIDTH = 30
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    """function to generate a password of random length"""

    # gets 8-10 random letters(a-Z)
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    # gets 2-4 random numbers(0-9)
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    # gets 2-4 random symbols
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    # put all the characters in a list
    password_list = password_letters + password_numbers + password_symbols

    # shuffle and join characters to make the password
    random.shuffle(password_list)
    password = "".join(password_list)
    # insert the password into the password entry
    pass_entry.insert(index=0, string=password)
    # copy the password to clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    """function to save the contents into a text file"""

    # get the content from the entries
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    # check whether any entry is blank
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        tkinter.messagebox.showinfo(title="password manager", message="No data entered!")
    else:
        # display confirmation dialog box
        confirmation = tkinter.messagebox.askokcancel(title="password manager",
                                                      message="Do you want to continue?")

        # if user clicks "ok" then save data
        if confirmation:
            with open("data.txt", mode='a') as content:
                content.write(website + " | " + email + " | " + password + '\n')
                content.write("\n")
            tkinter.messagebox.showinfo(title="password manager",
                                        message="your password was successfully saved")
            # reset entries after saving
            website_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


# Creating the Window
window = Tk()
window.title("Password Manager")
window.minsize(width=700, height=500)
window.config(padx=100, pady=70, bg="#161853")


# Creating a canvas for the image
canvas = Canvas(width=200, height=225, bg="#161853", highlightthickness=False)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 90, image=logo)
canvas.grid(row=0, column=1)


# Creating entry for website
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)
website_entry = Entry(width=WEBSITE_EMAIL_WIDTH)
# website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)


# Creating entry for Email/Username
email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)
email_entry = Entry(width=WEBSITE_EMAIL_WIDTH)
email_entry.insert(index=0, string="example@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)


# Creating entry for the password
pass_label = Label(text="Password: ")
pass_label.grid(row=3, column=0)
pass_entry = Entry(width=PASSWORD_ENTRY_WIDTH)
pass_entry.grid(row=3, column=0, columnspan=2)


# Creating a password generate button
gen_pass_button = Button(text="Generate Password", command=password_generator, bg="#EBE645")
gen_pass_button.grid(row=3, column=2, columnspan=2)


# Creating a button to write data into .txt file
add_button = Button(text="Add", width=55, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)


# To keep the window running
window.mainloop()
