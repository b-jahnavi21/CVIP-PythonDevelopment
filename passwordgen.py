import random
import tkinter as tk
from tkinter import Label, Entry, Button

def generate_password():
    len_pass = int(length_entry.get())
    password = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*'
    generated_password = "".join(random.sample(password, len_pass))
    result_label.config(text=f"Your password is {generated_password}")

root = tk.Tk()
root.title("Password Generator")

instruction_label = Label(root, text="Enter the length of the password:")
instruction_label.pack()

length_entry = Entry(root)
length_entry.pack()

generate_button = Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

result_label = Label(root, text="")
result_label.pack()

root.mainloop()
