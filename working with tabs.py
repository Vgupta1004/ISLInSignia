# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 12:46:51 2020

@author: shara
"""

import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

root=tk.Tk()

root.geometry=('1200x750')

my_nb=ttk.Notebook(root)
my_nb.pack(fill='both',expand=1)

frame1=tk.Frame(my_nb,width=1200,height=750,bg='blue')
frame2=tk.Frame(my_nb,width=1200,height=750,bg='red')

#frame1.pack(fill='both',expand=1)
#frame2.pack(fill='both',expand=1)

my_nb.add(frame1,text='Blue tab')
my_nb.add(frame2,text='Red tab')

fr1= tk.Frame(frame1,bg='#FFBC8B')

my_pic=Image.open('images/mic1.png')

resized = my_pic.resize((50,50),Image.ANTIALIAS)
new_pic=ImageTk.PhotoImage(resized)

label=tk.Label(frame1, image = new_pic)
label.pack()

button=tk.Button(frame1, image = new_pic)
button.pack()
#my_nb.hide(0)
#my_nb.hide(1)




root.mainloop()