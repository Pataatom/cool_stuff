import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Progress Bar in Tk")
progressbar = ttk.Progressbar(orient=tk.HORIZONTAL, length=160)
progressbar.place(x=30, y=30)
root.geometry("300x200")
root.mainloop()