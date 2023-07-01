import tkinter as tk
import time

root = tk.Tk()
root.title("Clock")

def present_time():
    display_time = time.strftime("%I:%M:%S %p")
    digi_clock.config(text=display_time)
    digi_clock.after(200, present_time)

digi_clock = tk.Label(root, font=("Arial", 150), bg="red", fg="black")
digi_clock.pack()

present_time()
root.mainloop()
