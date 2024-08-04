# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 17:21:40 2020

@author: shara
"""


import tkinter as tk

window1=tk.Tk()
window1.title('Audio to Sign Language')
window1.configure(bg='#FFBC8B')
window1.geometry('1250x700')
window1.iconbitmap('C:\\Users\\shara\\Downloads\\Danieledesantis-Audio-Video-Outline-Play.ico')



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
frame1=tk.Frame(window1,bg='#FFBC8B')
frame1.place(x=0,y=20,width=1500,height=120)
heading_lb= tk.Label(frame1,fg='black',bg='#FFBC8B',text='AUDIO TO SIGN LANGUAGE TOOL',padx=25,pady=5,font=('Gabriola',40,'bold'))
heading_lb.place(x=310,y=0)

#name accepting
frame2=tk.Frame(window1,bg='#FFBC8B')
frame2.place(x=10,y=280,width=600,height=150)
name_lb=tk.Label(frame2,bg='#FFBC8B',text="Enter Your Name:",font=('Cambria',14))
name_lb.place(x=15,y=30)
name_ent=tk.Entry(frame2,width=30,font=('Cambria',14))
name_ent.place(x=175,y=28)
name_btn=tk.Button(frame2,text='Enter',bg='#F29062',font=('Cambria',14),command=EnterName)
name_btn.place(x=525,y=22)

#side animation
icon=tk.PhotoImage(file='C:\\Users\\shara\\Downloads\\unnamed.png')
pic_lb=tk.Label(window1,image=icon)
pic_lb.place(x=800,y=150)

#displaying menu bar
frame3=tk.Frame(window1,bg='#5B524A')
frame3.place(x=0,y=150,width=1500,height=50)
homepage_btn=tk.Button(frame3,text='Homepage',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14))
homepage_btn.pack(side='left')
English_btn=tk.Button(frame3,text='English converter',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14))
English_btn.pack(side='left')
Hindi_btn=tk.Button(frame3,text='Hindi converter',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14))
Hindi_btn.pack(side='left')
About_btn=tk.Button(frame3,text='About',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14))
About_btn.pack(side='left')
Quit_btn=tk.Button(frame3,text='Quit',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14))
Quit_btn.pack(side='left')


window1.mainloop()

















