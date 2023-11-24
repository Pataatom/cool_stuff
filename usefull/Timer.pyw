import time
import tkinter as tk
import winsound
root = tk.Tk()


num60 = 60
num45 = 45


def time_45():
    button1.destroy()
    button2.destroy()
    global num45
    if num45 > 0:
        number_label["text"] = str(num45)
        num45 -= 1
        root.after(60000, time_45)
    else:
        number_label["text"] = "Time's up"
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        time.sleep(5)
        root.destroy()




def time_60():
    button1.destroy()
    button2.destroy()
    global num60
    if num60 > 0:
        number_label["text"] = str(num60)
        num60 -= 1
        root.after(60000, time_60)
    else:
        number_label["text"] = "Time's up"
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        time.sleep(5)
        root.destroy()

number_label = tk.Label(root, text="0", font=("Arial", 24))
number_label.pack()
button1 = tk.Button(root, text="45 min", command=time_45)
button2 = tk.Button(text="60 min", command=time_60)
button1.pack()
button2.pack()

root.mainloop()