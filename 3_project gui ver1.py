# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 20:23:01 2020

@author: shara
"""

import tkinter as tk

window1=tk.Tk()
window1.title('Audio to Sign Language')
window1.configure(bg='#FFBC8B')
window1.geometry('1250x700')

user_name=''

def EnterName():
    globals()['user_name']=name_ent.get()
    global nameError_lb
    nameError_lb=tk.Label(frame2,text='*Please enter atleast one character for name',bg='#FFBC8B',fg='red',font=('Cambria',10))

    if len(user_name)<1:
        nameError_lb.place(x=200,y=5)
    else:               
        wlcm_lb=tk.Label(frame2,text='Welcome '+user_name+"!!!",font=('Cambria',20),bg='#FFBC8B')
        wlcm_lb.place(x=210,y=80)
        nameError_lb.destroy()
        name_ent['state']=tk.DISABLED
        

#first window heading
frame1=tk.Frame(window1,highlightcolor='black',highlightbackground='black',highlightthickness=1,bg='#FFBC8B')
frame1.place(x=0,y=20,width=1500,height=180)
heading_lb= tk.Label(frame1,fg='black',bg='#FFBC8B',text='AUDIO TO SIGN LANGUAGE TOOL',padx=30,pady=30,font=('Gabriola',40,'bold'))
heading_lb.place(x=310,y=0)

#name accepting
frame2=tk.Frame(window1,bg='#FFBC8B',highlightcolor='black',highlightbackground='black',highlightthickness=1)
frame2.place(x=300,y=210,width=600,height=150)
name_lb=tk.Label(frame2,bg='#FFBC8B',text="Enter Your Name:",font=('Cambria',14))
name_lb.place(x=15,y=30)
name_ent=tk.Entry(frame2,width=30,font=('Cambria',14))
name_ent.place(x=175,y=28)
name_btn=tk.Button(frame2,text='Enter',bg='#F29062',font=('Cambria',14),command=EnterName)
name_btn.place(x=525,y=22)

#lang check

frame3=tk.Frame(window1,bg='#FFBC8B',highlightcolor='black',highlightbackground='black',highlightthickness=1)
frame3.place(x=300,y=400,width=600,height=150)
lang_lb=tk.Label(frame3,bg='#FFBC8B',text="Select the language in which you would like to give input",font=('Cambria',14))
lang_lb.place(x=20,y=20)



window1.mainloop()

















