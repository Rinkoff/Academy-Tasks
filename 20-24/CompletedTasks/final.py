from random import randint
import tkinter as tk

first_num = True

def new_number():
    global first_num
    if first_num:
        number = ""
        first_num = False
    else:
        number = str(randint(0, 1000))

    number_label.config(text=number)

root = tk.Tk()
root.title("Random Number Generator")

label = tk.Label(root, text="Generate random number")
label.pack()

number_label = tk.Label(root, text="", width=10)
number_label.pack()

button = tk.Button(root, text="Generate new number", command=new_number)
button.pack()

root.mainloop()