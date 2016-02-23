from Tkinter import *
import ttk
import os
from parse_pie import plot_pie




master = Tk()


Label(master, text = "Filename:").pack()
e = Entry(master)
e.pack()



def callback():
    s = e.get()
    plot_pie(s)

b = Button(master, text="Pie Graph", command=callback)
b.pack()
mainloop()
root.destroy()











