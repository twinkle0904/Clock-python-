import tkinter as tk 
from tkinter import ttk 

from time import strftime

root = tk.Tk()
root.title("Clock")

def time():
    string = strftime('%H:%M:%S')
    label.config(text=string)
    label.after(1000,time)

label = tk.Label(root, font=("ds-didgital",80),background = "black", foreground = "cyan")
label.pack(anchor= 'center')
time()

root.mainloop()