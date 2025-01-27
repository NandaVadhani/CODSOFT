import tkinter as tk
from tkinter import messagebox

def add():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result.set(num1 + num2)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

def subtract():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result.set(num1 - num2)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

def multiply():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result.set(num1 * num2)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

def divide():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 == 0:
            messagebox.showerror("Error", "Cannot divide by zero")
        else:
            result.set(num1 / num2)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

app = tk.Tk()
app.title("Simple Calculator")

tk.Label(app, text="Number 1:").grid(row=0, column=5)
entry1 = tk.Entry(app)
entry1.grid(row=0, column=6)

tk.Label(app, text="Number 2:").grid(row=1, column=5)
entry2 = tk.Entry(app)
entry2.grid(row=1, column=6)

tk.Button(app, text="Add", command=add).grid(row=4, column=5)
tk.Button(app, text="Subtract", command=subtract).grid(row=4, column=6)
tk.Button(app, text="Multiply", command=multiply).grid(row=5, column=5)
tk.Button(app, text="Divide", command=divide).grid(row=5, column=6)

result = tk.StringVar()
tk.Label(app, text="Result:").grid(row=13, column=5)
tk.Entry(app, textvariable=result, state='readonly', width=30).grid(row=13, column=6)  
app.mainloop()