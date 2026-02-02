from tkinter import *
from pathlib import Path
from tkinter import messagebox
import pyperclip
import json

BASE_DIR = Path(__file__).resolve().parent

# JSON basic commnads.
# json.dump()
# json.load()
# json.update()

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
import random
import pyperclip

def generate_password():
    letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers = list("0123456789")
    symbols = list("!#$%&()*+")

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)  # ✅ correct

    password_string = "".join(password_list)

    # password_input.delete(0, END)          # optional: clear old password
    password_input.insert(0, password_string)
    pyperclip.copy(password_string)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_information():
    file_path = BASE_DIR / "data.json"
    website_text = website_input.get()
    email_text = email_input.get()
    password_text = password_input.get()
    
    
    # is_ok = messagebox.askokcancel(
    #     title="Confirm Save",
    #     message=f"These are the details entered:\n\nEmail: {email_text}\nPassword: {password_text}\n\nSave?"
    # )
    
    new_data = {
        website_text:{
            "email": email_text,
            "password": password_text,
        }
    }
    
    if len(website_text) == 0 or len(password_text) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open(file_path, "r", encoding="utf-8") as data_file:
                # Reading old data.
                data = json.load(data_file)
                # Updating old data.
                data.update(new_data)
                
        except FileNotFoundError:
            with open(file_path, "w", encoding="utf-8") as data_file:
                # Saving the updated data.
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open(file_path, "w", encoding="utf-8") as data_file:
                json.dump(new_data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
            
def search_credentials():
    file_path = BASE_DIR / "data.json"
    website_text = website_input.get()

    try: 
        with open(file_path, "r", encoding="utf-8") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"No Data file Found.")
    else:
        if website_text in data.keys():
            email_used = data[website_text].get("email")
            password_used = data[website_text].get("password")
            messagebox.showinfo(title=website_text, message=f"Email: {email_used}\n Password: {password_used}")
        else:
            messagebox.showinfo(title=f"{website_text}", message=f"Website: {website_text} has not been found.")
    finally:
        website_input.delete(0, END)
        password_input.delete(0, END)
        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

# Make column 1 expand (this is KEY)
window.grid_columnconfigure(0, weight=0)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=0)

logo_img = PhotoImage(file=BASE_DIR / "logo.png")

# Canvas (logo) centered
my_pass_canvas = Canvas(window, width=200, height=200, bg="white", highlightthickness=0)
my_pass_canvas.create_image(100, 100, image=logo_img)
my_pass_canvas.grid(column=1, row=0, pady=(0, 20))  # centered above inputs

# Website row
website_label = Label(text="Website:", bg="white")
website_label.grid(column=0, row=1, sticky="e", padx=(0, 10), pady=5)

website_input = Entry(width=35)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=1, sticky="ew", pady=5)

search_button = Button(text="Search", command=search_credentials)
search_button.grid(column=2, row=1, columnspan=1, sticky="ew", padx=(10, 0), pady=(10, 0))
search_button.config(activebackground="blue")

# Email/Username row
email_label = Label(text="Email/Username:", bg="white")
email_label.grid(column=0, row=2, sticky="e", padx=(0, 10), pady=5)

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2, sticky="ew", pady=5)
email_input.insert(0, "example@email.com")  # optional, like the course

# Password row
password_label = Label(text="Password:", bg="white")
password_label.grid(column=0, row=3, sticky="e", padx=(0, 10), pady=5)

password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky="ew", pady=5)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="ew", padx=(10, 0), pady=5)

# Add button
add_button = Button(text="Add", command=save_information)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew", pady=(10, 0))

window.mainloop()
