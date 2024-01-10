from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

DATA_FILE = "data.json"


def find_password(website_entry, email_entry, password_entry):
    # Retrieve and display saved credentials for a given website
    website = website_entry.get().lower()
    try:
        with open(DATA_FILE, "r") as data_file:
            data = json.load(data_file)
            credentials = data[website]
            messagebox.showinfo(title=website,
                                message=f"Your credentials are:\n Email: {credentials['email']}\n Password: {credentials['password']}")

            # Populate the entry fields
            email_entry.delete(0, END)
            email_entry.insert(0, credentials['email'])

            password_entry.delete(0, END)
            password_entry.insert(0, credentials['password'])

            # Copy the password to the clipboard
            pyperclip.copy(credentials['password'])

            # Notify the user about the password being copied
            messagebox.showinfo(title="Password Copied", message="Password has been copied to the clipboard.")

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="Data File Not Found")
    except KeyError:
        messagebox.showerror(title="Error", message=f"Unable to find password for the website: {website}")


def generate_password(entry):
    # Generate a random password and copy it to the clipboard
    entry.delete(0, END)
    characters = ['abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '0123456789', '!#$%&()*+']
    password = ''.join([choice(char) for _ in range(randint(10, 10)) for char in characters])
    entry.insert(0, password)
    pyperclip.copy(password)


def save_password(website_entry, email_entry, password_entry):
    # Save entered credentials for a website to a data file
    website = website_entry.get().lower()
    email = email_entry.get()
    password = password_entry.get()

    if not all([website, email, password]):
        messagebox.showerror(title="Error", message="Please fill in all fields.")
        return

    user_confirmed = messagebox.askokcancel(title=website,
                                            message=f"Is this ok?\n Email: {email}\n Password: {password}")

    if user_confirmed:
        try:
            with open(DATA_FILE, "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            data = {}

        data[website] = {"email": email, "password": password}

        with open(DATA_FILE, "w") as data_file:
            json.dump(data, data_file, indent=4)

        # Clear entry fields after saving
        website_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry.delete(0, END)


def setup_ui():
    # Set up the graphical user interface
    window = Tk()
    window.title("Password Manager")
    window.config(pady=50, padx=50)

    canvas = Canvas(width=200, height=200)
    padlock = PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=padlock)
    canvas.grid(column=1, row=0)

    website_entry = Entry(width=33)
    website_entry.grid(column=1, row=1)
    website_entry.focus()

    email_entry = Entry(width=52)
    email_entry.grid(column=1, columnspan=2, row=2)
    email_entry.insert(index=END, string="")

    password_entry = Entry(width=33)
    password_entry.grid(column=1, row=3)

    save_button = Button(text="Save", command=lambda: save_password(website_entry, email_entry, password_entry),
                         width=44)
    save_button.grid(column=1, columnspan=2, row=4)

    generate_password_button = Button(text="Generate Password", command=lambda: generate_password(password_entry),
                                      width=15)
    generate_password_button.grid(column=2, row=3)

    search_button = Button(text="Search", command=lambda: find_password(website_entry, email_entry, password_entry),
                           width=15)
    search_button.grid(column=2, row=1)

    website_label = Label(text="Website: ")
    website_label.grid(column=0, row=1)

    email_label = Label(text="Email/Username: ")
    email_label.grid(column=0, row=2)

    password_label = Label(text="Password: ")
    password_label.grid(column=0, row=3)

    window.mainloop()


if __name__ == "__main__":
    setup_ui()
