import tkinter as tk

WINDOW_WIDTH = 300
WINDOW_HEIGHT = 300

root = tk.Tk()

root.title("Login Screen")

root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

email_label = tk.Label(root,text = "Enter your E-mail:")
email_label.place(x = 10,y=30)

email_entry = tk.Entry(root)
email_entry.place(x = 130,y=30)

username_label = tk.Label(root,text = "Enter your username:")
username_label.place(x = 10,y=70)

username_entry = tk.Entry(root)
username_entry.place(x = 130,y=70)

password_label = tk.Label(root,text = "Enter your password:")
password_label.place(x = 10,y=110)

password_entry = tk.Entry(root)
password_entry.place(x = 130,y=110)

password_confirm_label = tk.Label(root,text = "Confirm your password:")
password_confirm_label.place(x = 10,y=150)

password_confirm_entry = tk.Entry(root)
password_confirm_entry.place(x = 140,y=150)

var = tk.BooleanVar()

checkbox = tk.Checkbutton(root, text="I'am over 18", variable=var)
checkbox.place(x = 110,y= 190)


button = tk.Button(root, text="Register")
button.place(x = 130,y = 240)


root.mainloop()