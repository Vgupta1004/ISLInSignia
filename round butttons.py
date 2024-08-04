# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 22:34:26 2020

@author: shara
"""

from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.geometry('400x400')

def thing():
    my_label.config(text='You clicked the button...')

login_btn=ImageTk.PhotoImage(Image.open('images/boy.png'))


img_label=Label(image=login_btn)
#img_label.pack(pady=20)

my_button=Button(root,image=login_btn,command=thing,borderwidth=0)
my_button.pack(pady=20)


my_label=Label(root,text='')
my_label.pack()












root.mainloop()