# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 23:16:08 2020

@author: shara
"""

from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.geometry('800x500')


my_pic=Image.open('images/mic1.png')

resized = my_pic.resize((50,50),Image.ANTIALIAS)
new_pic=ImageTk.PhotoImage(resized)



my_label=Label(root,image=new_pic)
my_label.pack(pady=20)
















root.mainloop()