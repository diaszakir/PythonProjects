import random
import string
from tkinter import *
from tkinter import ttk
import pyperclip

root = Tk()
root.title("Password Generator")
root.geometry("500x250")

main_text = "Hello!" + '\n' + "Select length of password (8-32): "

label = Label(text=main_text)
label.pack()

entry = ttk.Entry(root)
entry.pack(anchor=NW, padx=10, pady=6)


def Generate():
    global new_password
    try:
        n = int(entry.get())
        if 8 <= n <= 32:
            characters = string.ascii_letters + string.digits
            new_password = ''.join(random.choice(characters) for _ in range(n))
            label["text"] = main_text + '\n' + "Password is " + new_password + '\n' + "Copied!"
            write(new_password)
        elif n < 8:
            label["text"] = "I only can create password between 8 and 32"
        elif n > 32:
            label["text"] = "I only can create password between 8 and 32"
    except ValueError:
        label["text"] = "Enter the number!"

def write(pasw):
    pyperclip.copy(pasw)



btn = Button(text="Generate", command=Generate)
btn.pack()

lab = ttk.Label()
lab.pack(anchor=NW, padx=10, pady=6)

root.mainloop()
