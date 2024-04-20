from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
               'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    random_letters = [choice(letters) for letter in range(randint(8, 10))]
    random_symbols = [choice(symbols) for symbol in range(randint(2, 4))]
    random_nums = [choice(numbers) for num in range(randint(2, 4))]

    password_list = random_letters + random_symbols + random_nums
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="passwords.json",
                            message="No Data File Found.")
    else:
        website = website_input.get()
        if website in data.keys():
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,
                                message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title=website,
                                message="No details for the website exists.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("passwords.json", "r") as pass_data:
                # Reading data at last data file
                data = json.load(pass_data)
                passwords = [site_data["password"] for site_data in data.values()]
                if password in passwords:
                    messagebox.showinfo(title="PasswordError",
                                        message="Password is already used. \nPlease, create a unique password.")
                    return
        except FileNotFoundError:
            pass  # If file not found, it will be created below

        try:
            with open("passwords.json", "w") as pass_data:
                if "data" in locals():
                    # Updating new data in existing JSON data
                    data.update(new_data)
                    json.dump(data, pass_data, indent=4)
                else:
                    # Writing new data to the JSON file
                    json.dump(new_data, pass_data, indent=4)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message=f"File not found")
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Row 1
website_label = Label(text="Website:", font=("Arial", 16))
website_label.grid(column=0, row=1)

website_input = Entry(width=20)
website_input.grid(column=1, row=1)
website_input.focus()

search = Button(text="Search", width=12, command=find_password)
search.grid(column=2, row=1)

# Row 2
email_label = Label(text="Email/Username:", font=("Arial", 16))
email_label.grid(column=0, row=2)

email_input = Entry(width=37)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, string="di.yu777@gmail.com")

# Row 3
password_label = Label(text="Password:", font=("Arial", 16))
password_label.grid(column=0, row=3)

password_input = Entry(width=20)
password_input.grid(column=1, row=3)

generator = Button(text="Generate Password", width=12, command=password_generator)
generator.grid(column=2, row=3)

# Row 4
add_to_file = Button(text="Add", width=35, command=save)
add_to_file.grid(column=1, row=4, columnspan=2)

window.mainloop()
