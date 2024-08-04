# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 01:08:09 2020

@author: shara
"""

import speech_recognition as sr
import tkinter as tk


def windestroy():
     tk.messagebox.showinfo("Quit","You have chosen to exit the program\nThank you for visiting")
     window1.destroy()      

def receive_audio():
    sample_rate = 48000
    chunk_size = 2048
    r = sr.Recognizer()
    
            
    with sr.Microphone(sample_rate = sample_rate,  chunk_size = chunk_size) as source:
        
        r.adjust_for_ambient_noise(source,duration=0.5)
        
        audio = r.listen(source) 
              
        try:                                                               
            text = r.recognize_google(audio)   
            
            ent1.insert(0,text) 
                                 
            
            
        except sr.UnknownValueError: 
            print("Google Speech Recognition could not understand audio") 
      
        except sr.RequestError as e: 
           print("Could not request results from Google Speech Recognition service; {0}".format(e))
           
           
           
window1=tk.Tk()
window1.title('Audio to Sign Language')
window1.configure(bg='#FFBC8B')
window1.geometry('1250x700')
window1.iconbitmap('C:\\Users\\shara\\Downloads\\Danieledesantis-Audio-Video-Outline-Play.ico')

#window heading
frame1=tk.Frame(window1,bg='#FFBC8B')
frame1.place(x=0,y=20,width=1500,height=120)
heading_lb= tk.Label(frame1,fg='black',bg='#FFBC8B',text='AUDIO TO SIGN LANGUAGE TOOL',padx=25,pady=5,font=('Gabriola',40,'bold'))
heading_lb.place(x=310,y=0)


#displaying menu bar
frame2=tk.Frame(window1,bg='#5B524A')
frame2.place(x=0,y=150,width=1500,height=50)
homepage_btn=tk.Button(frame2,text='Homepage',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14))
homepage_btn.pack(side='left')
English_btn=tk.Button(frame2,text='English converter',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14))
English_btn.pack(side='left')
Hindi_btn=tk.Button(frame2,text='Hindi converter',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14))
Hindi_btn.pack(side='left')
About_btn=tk.Button(frame2,text='About',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14))
About_btn.pack(side='left')
Quit_btn=tk.Button(frame2,text='Quit',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=windestroy)
Quit_btn.pack(side='left')


#audio input
frame3=tk.Frame(window1,bg='#FFBC8B',highlightcolor='black',highlightbackground='black',highlightthickness=1)
frame3.place(x=5,y=220,width=530,height=125)
input_audio_lb=tk.Label(frame3,text='Enter Text by Using Mic or by Typing in the Space Provided',bg='#FFBC8B',font=('Cambria',14,'bold'))
input_audio_lb.place(x=10,y=10)
eng_audio_ent=tk.Entry(frame3,font=16)
eng_audio_ent.place(x=10,y=50,width=400,height=35)

eng_audio_btn= tk.Button(frame3,text='click to input sound',command=receive_audio)
eng_audio_btn.place(x=410,y=50)

window1.mainloop()













