import random
import string
from tkinter import *
from tkinter import messagebox

def generate_password():
    password_length = int(entry.get())
    password_characters = ''
    if var_uppercase.get():
        password_characters += string.ascii_uppercase
    if var_lowercase.get():
        password_characters += string.ascii_lowercase
    if var_digits.get():
        password_characters += string.digits
    if var_punctuation.get():
        password_characters += string.punctuation
    if var_avoid_similar.get():
        password_characters = password_characters.translate(str.maketrans('', '', 'l1O0'))
    if custom_entry.get():
        password_characters = custom_entry.get()
    password = ''.join(random.choice(password_characters) for i in range(password_length))
    label.config(text=password)
    strength = get_password_strength(password)
    strength_label.config(text=f"Strength: {strength}")
    strength_label.config(fg=get_strength_color(strength))
    history_listbox.insert(END, password)
    hint = get_password_hint(password)
    hint_label.config(text=f"Hint: {hint}")

def get_password_strength(password):
    if len(password) < 6:
        return "Weak"
    elif len(password) < 10:
        return "Moderate"
    else:
        return "Strong"

def get_strength_color(strength):
    if strength == "Weak":
        return "red"
    elif strength == "Moderate":
        return "orange"
    else:
        return "green"

def get_password_hint(password):
    hint = ''
    for char in password:
        if char.isalpha():
            hint += char.lower()
        else:
            hint += '*'
    return hint

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(label.cget("text"))
    messagebox.showinfo("Password Generator", "Password copied to clipboard!")

def save_password():
    with open("passwords.txt", "a") as f:
        f.write(label.cget("text") + "\n")
    messagebox.showinfo("Password Generator", "Password saved to file!")

def copy_history():
    selected = history_listbox.curselection()
    if selected:
        root.clipboard_clear()
        root.clipboard_append(history_listbox.get(selected[0]))
        messagebox.showinfo("Password Generator", "Password copied to clipboard!")

def save_history():
    selected = history_listbox.curselection()
    if selected:
        with open("passwords.txt", "a") as f:
            f.write(history_listbox.get(selected[0]) + "\n")
        messagebox.showinfo("Password Generator", "Password saved to file!")

def confirm_password():
    if confirm_entry.get() == label.cget("text"):
        messagebox.showinfo("Password Generator", "Password confirmed!")
    else:
        messagebox.showerror("Password Generator", "Passwords do not match!")

root = Tk()
root.title("Advanced Password Generator")

label = Label(root, text="Enter password length:")
label.pack()

entry = Entry(root)
entry.pack()

var_uppercase = IntVar(value=1)
check_uppercase = Checkbutton(root, text="Include uppercase letters", variable=var_uppercase)
check_uppercase.pack()

var_lowercase = IntVar(value=1)
check_lowercase = Checkbutton(root, text="Include lowercase letters", variable=var_lowercase)
check_lowercase.pack()

var_digits = IntVar(value=1)
check_digits = Checkbutton(root, text="Include digits", variable=var_digits)
check_digits.pack()

var_punctuation = IntVar(value=1)
check_punctuation = Checkbutton(root, text="Include punctuation", variable=var_punctuation)
check_punctuation.pack()

var_avoid_similar = IntVar(value=0)
check_avoid_similar = Checkbutton(root, text="Avoid similar characters (l1O0)", variable=var_avoid_similar)
check_avoid_similar.pack()

custom_label = Label(root, text="Custom character set (leave blank to use default):")
custom_label.pack()

custom_entry = Entry(root)
custom_entry.pack()

button = Button(root, text="Generate Password", command=generate_password)
button.pack()

label = Label(root, text="")
label.pack()

strength_label = Label(root, text="")
strength_label.pack()

hint_label = Label(root, text="")
hint_label.pack()

copy_button = Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack()

save_button = Button(root, text="Save Password", command=save_password)
save_button.pack()

confirm_label = Label(root, text="Re-enter password to confirm:")
confirm_label.pack()

confirm_entry = Entry(root, show="*")
confirm_entry.pack()

confirm_button = Button(root, text="Confirm Password", command=confirm_password)
confirm_button.pack()

history_label = Label(root, text="Password History:")
history_label.pack()

history_listbox = Listbox(root)
history_listbox.pack()

copy_history_button = Button(root, text="Copy Selected Password", command=copy_history)
copy_history_button.pack()

save_history_button = Button(root, text="Save Selected Password", command=save_history)
save_history_button.pack()

root.mainloop()
