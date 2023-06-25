from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip

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
    if website == "" or email == "" or pw == "":
        messagebox.showinfo("Warning", "Do not leave any fields empty.")
    else:
        answer = messagebox.askquestion(f"{website}", f"Email:{email}\nPassword:{pw}\nIs this okay?")
        if answer == 'yes':
            with open('pw.txt') as pw_file:
                data = pw_file.read()

            with open("pw.txt", mode="a") as passwords:
                passwords.write(website)
                passwords.write(" | ")
                passwords.write(email)
                passwords.write(" | ")
                passwords.write(pw)
                passwords.write("\n")
                website_entry.delete(0, END)
                email_username_entry.delete(0, END)
                password_entry.delete(0, END)

        elif answer == 'no':
            pass


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

website_entry = Entry(width=35)
website_entry.grid(column=2, row=2, columnspan=2)

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

