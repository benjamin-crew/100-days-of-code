from tkinter import *
from tkinter import messagebox
import pandas
import random
import pyperclip
import json

FONT="Courier"
FONTSIZE = 14

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    total_num = 0

    while total_num != 16:
        nr_letters = random.randint(1,6)
        nr_symbols = random.randint(1,6)
        nr_numbers = random.randint(1,6)
        total_num = nr_letters + nr_symbols + nr_numbers
        password = ""

    for n in range(nr_letters):
        password += random.choice(letters)
    for n in range(nr_symbols):
        password += random.choice(symbols)
    for n in range(nr_numbers):
        password += random.choice(numbers)

    password = list(password)
    random.shuffle(password)
    password = "".join(password)
    pyperclip.copy(password)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def clear_text():
   website_entry.delete(0, END)
   password_entry.delete(0, END)

def add_password():
    if any([len(a.get()) == 0 for a in (website_entry, password_entry, emailusername_entry)]):
        messagebox.showerror(title="Missing Information!", message="Credentials not saved as not all entry boxes populated.")
    else:

        data = {
                website_entry.get(): {
                    "email": emailusername_entry.get(),
                    "password": password_entry.get(),
            }
        }

        try:
            with open("data.json", "r") as data_file:
                # Read
                loaded_json = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        else:
            # Update
            loaded_json.update(data)

            # Save
            with open("data.json", "w") as data_file:
                json.dump(loaded_json, data_file, indent=4)
        finally:            
            clear_text()
            messagebox.showinfo(title="Password saved.", message="Your password has been stored in the database.")


# ---------------------------- SEARCH ------------------------------- #
def search_json():

    website = website_entry.get()

    try:
        with open("data.json") as data_file:
            loaded_json = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="No file detected.", message="There are no passwords currently stored in the database.")
    else:
        for key in loaded_json:
            if website.lower() == key.lower():
                email = loaded_json[key]["email"]
                password = loaded_json[key]["password"]
                messagebox.showinfo(title=key, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Website not in database", message=f"{website} is not in the database.")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(bg="white", padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=(FONT, FONTSIZE))
emailusername_label = Label(text="Email/Username:", font=(FONT, FONTSIZE))
password_label = Label(text="Password:", font=(FONT, FONTSIZE))

website_label.grid(column=0, row=1)
emailusername_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

website_entry = Entry(width=21)
emailusername_entry = Entry(width=43)
password_entry = Entry(width=21)

website_entry.grid(column=1, row=1, columnspan=1)
emailusername_entry.grid(column=1, row=2, columnspan=2)
password_entry.grid(column=1, row=3)

website_entry.focus()
emailusername_entry.insert(0, "benncrew94@gmail.com")

generate_button = Button(text="Generate Password", width=18, command=generate_password)
add_button = Button(text="Add", width=36, command=add_password)
search_button = Button(text="Search", width=18, command=search_json)

generate_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)
search_button.grid(column=2, row=1)

window.mainloop()
