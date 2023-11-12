import tkinter as tk


def on_entry_click(event,searchbar,text):
    if searchbar.get() == text:
        searchbar.delete(0, "end")
        searchbar.insert(0, "")
        searchbar.config(foreground="#080808")

def on_entry_focusout(event,searchbar,text):
    if searchbar.get() == "":
        searchbar.insert(0, text)
        searchbar.config(foreground="#b8b8b8")



WINDOW_WIDTH = 300
WINDOW_HEIGHT = 200

root = tk.Tk()

root.title("Login Screen")

root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

username_entry = tk.Entry(root,foreground="#b8b8b8")
username_entry.place(x = 90,y=30)
username_entry.insert(0, "Enter your username")
username_entry.bind("<FocusIn>",lambda event: on_entry_click(event,username_entry,"Enter your username"))
username_entry.bind("<FocusOut>",lambda event: on_entry_focusout(event,username_entry,"Enter your username"))


password_entry = tk.Entry(root,foreground="#b8b8b8")
password_entry.place(x = 90,y=70)
password_entry.insert(0, "Enter your password")
password_entry.bind("<FocusIn>",lambda event: on_entry_click(event,password_entry,"Enter your password"))
password_entry.bind("<FocusOut>",lambda event: on_entry_focusout(event,password_entry,"Enter your password"))



var = tk.BooleanVar()

checkbox = tk.Checkbutton(root, text="Do you want to save your password", variable=var)
checkbox.place(x = 30,y= 120)

button = tk.Button(root, text="Login")
button.place(x = 130,y = 160)

root.mainloop()