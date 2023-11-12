import tkinter as tk

root = tk.Tk()

root.title("My first app")

label = tk.Label(text= "Click this button").pack()

button = tk.Button(text="Click Me")
button.pack()

root.mainloop()