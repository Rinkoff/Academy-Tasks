import tkinter as tk

WINDOW_WIDTH = 300
WINDOW_HEIGHT = 200

root = tk.Tk()

root.title("Login Screen")

root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

username_label = tk.Label(root,text = "Enter your username:")
username_label.place(x = 10,y=30)

username_entry = tk.Entry(root)
username_entry.place(x = 130,y=30)

password_label = tk.Label(root,text = "Enter your password:")
password_label.place(x = 10,y=70)

password_entry = tk.Entry(root)
password_entry.place(x = 130,y=70)

var = tk.BooleanVar()

checkbox = tk.Checkbutton(root, text="Do you want to save your password", variable=var)
checkbox.place(x = 30,y= 120)

button = tk.Button(root, text="Login")
button.place(x = 130,y = 160)

root.mainloop()