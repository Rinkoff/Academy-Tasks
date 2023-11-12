import tkinter as tk

def say_hello():
    print("Hello")

root = tk.Tk()

root.title("My first app")

label = tk.Label(text= "Click this button").pack()

button = tk.Button(text="Click Me",command=say_hello)
button.pack()

root.mainloop()