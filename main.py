from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip
import json

NUM_OF_CHARACTERS = 16

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_pw():
    global NUM_OF_CHARACTERS
    character_bank = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(character_bank, k=NUM_OF_CHARACTERS))
    pyperclip.copy(password)
    password_entry.delete(0, END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_entry.get()
    email = email_username_entry.get()
    pw = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": pw,
        }
    }
    if website == "" or email == "" or pw == "":
        messagebox.showinfo("Warning", "Do not leave any fields empty.")
    else:
        try:
            with open("pw.json", mode="r") as passwords:
                data = json.load(passwords)
        except FileNotFoundError:
            with open("pw.json", mode="w") as new_file:
                json.dump(new_data, new_file, indent=4)
        else:
            data.update(new_data)
            with open("pw.json", mode="w") as passwords:
                json.dump(data, passwords, indent=4)
        finally:
            website_entry.delete(0, END)
            email_username_entry.delete(0, END)
            password_entry.delete(0, END)


# -------------------------- SEARCH WEBSITE --------------------------- #


def search():
    website = website_entry.get()
    try:
        with open("pw.json", mode="r") as passwords:
            data = json.load(passwords)
            website_email = data[website]["email"]
            website_password = data[website]["password"]
    except KeyError:
        messagebox.showinfo("Warning", "Website not found.")
    except FileNotFoundError:
        messagebox.showinfo("Warning", "File not found.")
    else:
        pyperclip.copy(website_password)
        messagebox.showinfo(f"{website}", f"Email: {website_email}\nPassword: {website_password}")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("MyPass")
window.config(padx=50, pady=50)

website_label = Label(text="Website:")
website_label.grid(column=1, row=2)

canvas_logo = Canvas()
canvas_logo.config(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas_logo.create_image(70, 100, image=logo)
canvas_logo.grid(column=2, row=1, columnspan=2)

website_entry = Entry(width=21)
website_entry.grid(column=2, row=2)

search_button = Button(text="Search", width=10, command=search)
search_button.grid(column=3, row=2)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=1, row=3)

email_username_entry = Entry(width=35)
email_username_entry.grid(column=2, row=3, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=1, row=4)

password_entry = Entry(width=21)
password_entry.grid(column=2, row=4)

pw_generate_button = Button(text="Generate", width=10, command=generate_pw)
pw_generate_button.grid(column=3, row=4)

add_button = Button(text="Add", width=30, command=save_password)
add_button.grid(column=2, row=5, columnspan=2)

window.mainloop()

