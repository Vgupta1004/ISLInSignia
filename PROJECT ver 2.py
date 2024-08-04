# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 17:21:40 2020
Updated on Sun Dec 27 
@author: shara
"""
#_________________________________________________________________________________________________________________________________________________________________
#importing all modules required throughout program
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
import speech_recognition as sr
import imageio
from pathlib import Path
import time
#_________________________________________________________________________________________________________________________________________________________________
#defining the main window
window1=tk.Tk()
window1.title('Audio to Sign Language')
window1.geometry('1250x700')
window1.iconbitmap('D:/Reliance school/Computer project/Danieledesantis-Audio-Video-Outline-Play.ico')
#_________________________________________________________________________________________________________________________________________________________________

user_name=''  #for accepting the name of the user in the homepage
#_________________________________________________________________________________________________________________________________________________________________
#function for taking name input in homepage
def EnterName():
    globals()['user_name']=name_ent.get()
    global nameError_lb
    global wlcm_lb
    nameError_lb=tk.Label(frame3,text='*Please enter atleast one character for name',bg='#FFBC8B',fg='red',font=('Cambria',10))

    if len(user_name)<1:
        nameError_lb.place(x=200,y=5)
    else:               
        wlcm_lb=tk.Label(frame3,text='Welcome '+user_name+"!!!",font=('Cambria',20),bg='#FFBC8B')
        wlcm_lb.place(x=210,y=80)
        
        nameError_lb.place_forget()
        
        name_ent['state']=tk.DISABLED
#_________________________________________________________________________________________________________________________________________________________________        
#function for quitting the program
def windestroy():
     tk.messagebox.showinfo("Quit","You have chosen to exit the program\nThank you for visiting")
     window1.destroy()        
#_________________________________________________________________________________________________________________________________________________________________
















































#_________________________________________________________________________________________________________________________________________________________________
#function for receiving audio in english converter
def receive_audio():
    sample_rate = 48000
    chunk_size = 2048
    r = sr.Recognizer()
    
            
    with sr.Microphone(sample_rate = sample_rate,  chunk_size = chunk_size) as source:
        
        r.adjust_for_ambient_noise(source,duration=0.5)
        
        audio = r.listen(source) 
              
        try:          
            global speak_text
            global text                                                     
            apeak_text = r.recognize_google(audio)   
            eng_audio_ent.insert(0,speak_text)
            text = text.eng_audio_ent.get().lower()
                                 
            if len(text)>0:
                eng_audio_btn['state']=tk.DISABLED
            
        except sr.UnknownValueError: 
            tk.messagebox.showinfo('Input Error!!!',"Google Speech Recognition could not understand audio\nPlease enter again")
            #("Google Speech Recognition could not understand audio") 
      
        except sr.RequestError as e: 
           tk.messagebox.showinfo("Input Error!!!","Could not request results from Google Speech Recognition service; {0}".format(e))    
           #print("Could not request results from Google Speech Recognition service; {0}".format(e))
#_________________________________________________________________________________________________________________________________________________________________

#designing English converter page
def eng_converter():
    
    audio_nb.select(1) #opening english converter tab
    #_________________________________________________________________________________________________________________________________________________________________
    #window heading
    frame1=tk.Frame(English_tab,bg='#FFBC8B')
    frame1.place(x=0,y=20,width=1500,height=120)
    heading_lb= tk.Label(frame1,fg='black',bg='#FFBC8B',text='AUDIO TO SIGN LANGUAGE TOOL',padx=25,pady=5,font=('Gabriola',40,'bold'))
    heading_lb.place(x=310,y=0)
    #_________________________________________________________________________________________________________________________________________________________________
    #displaying menu bar
    frame2=tk.Frame(English_tab,bg='#5B524A')
    frame2.place(x=0,y=150,width=1500,height=50)
    homepage_btn=tk.Button(frame2,text='Homepage',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=homepage)
    homepage_btn.pack(side='left')
    English_btn=tk.Button(frame2,text='English converter',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=eng_converter)
    English_btn.pack(side='left')
    Hindi_btn=tk.Button(frame2,text='Hindi converter',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14))
    Hindi_btn.pack(side='left')
    About_btn=tk.Button(frame2,text='About',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14))
    About_btn.pack(side='left')
    Quit_btn=tk.Button(frame2,text='Quit',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=windestroy)
    Quit_btn.pack(side='left')
    #____________________________________________________________________________________________________________________________________________________________________
    #audio/text input form user either by typing in entry box or by using mic
    global eng_audio_ent
    global eng_audio_btn
    global english_pic1
    global english_pic2
    global english_pic3
    global frame3
    frame3=tk.Frame(English_tab,bg='#FFBC8B',highlightcolor='black',highlightbackground='black',highlightthickness=1)
    frame3.place(x=5,y=220,width=530,height=125)
    input_audio_lb=tk.Label(frame3,text='Enter Text by Using Mic or by Typing in the Space Provided',bg='#FFBC8B',font=('Cambria',14,'bold'))
    input_audio_lb.place(x=10,y=10)
    
    eng_audio_ent=tk.Entry(frame3,font=16,borderwidth=1,relief='solid')
    eng_audio_ent.place(x=10,y=50,width=400,height=37)
    
    '''english_pic1=Image.open('images/mic1.png')
    english_pic2 = english_pic1.resize((35,35),Image.ANTIALIAS)
    english_pic3=ImageTk.PhotoImage(english_pic2)'''
    
    eng_audio_btn= tk.Button(frame3,command=receive_audio, borderwidth = 0)
    eng_audio_btn.place(x=410,y=50)
    #_________________________________________________________________________________________________________________________________________________________________





#_________________________________________________________________________________________________________________________________________________________________
#function for designing the homepage
def homepage():
    audio_nb.select(0)
    #_________________________________________________________________________________________________________________________________________________________________
    #window heading
    frame1=tk.Frame(Homepage_tab,bg='#FFBC8B')
    frame1.place(x=0,y=20,width=1500,height=120)
    heading_lb= tk.Label(frame1,fg='black',bg='#FFBC8B',text='AUDIO TO SIGN LANGUAGE TOOL',padx=25,pady=5,font=('Gabriola',40,'bold'))
    heading_lb.place(x=310,y=0)
    #_________________________________________________________________________________________________________________________________________________________________
    #displaying menu bar
    frame2=tk.Frame(Homepage_tab,bg='#5B524A')
    frame2.place(x=0,y=150,width=1500,height=50)
    homepage_btn=tk.Button(frame2,text='Homepage',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=homepage)
    homepage_btn.pack(side='left')
    English_btn=tk.Button(frame2,text='English converter',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=eng_converter)
    English_btn.pack(side='left')
    Hindi_btn=tk.Button(frame2,text='Hindi converter',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14))
    Hindi_btn.pack(side='left')
    About_btn=tk.Button(frame2,text='About',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14))
    About_btn.pack(side='left')
    Quit_btn=tk.Button(frame2,text='Quit',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=windestroy)
    Quit_btn.pack(side='left')
    #_________________________________________________________________________________________________________________________________________________________________
    #name accepting
    global name_ent
    global frame3
    global name_btn
    frame3=tk.Frame(Homepage_tab,bg='#FFBC8B')
    frame3.place(x=10,y=280,width=600,height=150)
    name_lb=tk.Label(frame3,bg='#FFBC8B',text="Enter Your Name:",font=('Cambria',14))
    name_lb.place(x=15,y=30)
    name_ent=tk.Entry(frame3,width=30,font=('Cambria',14))
    name_ent.place(x=175,y=28)
    name_btn=tk.Button(frame3,text='Enter',bg='#F29062',font=('Cambria',14),command=EnterName)
    
    #checking if the user is visiting the home page for the first time
    if globals()['c']==0:
        globals()['c']=1
        
    elif globals()['c']==1 and user_name=='':
        pass   
    else:
        name_btn['state']=tk.DISABLED
        wlcm_lb=tk.Label(frame3,text='Welcome '+user_name+"!!!",font=('Cambria',20),bg='#FFBC8B')
        wlcm_lb.place(x=210,y=80)
        name_ent.insert(0,user_name)
        name_ent['state']=tk.DISABLED
        
    name_btn.place(x=525,y=22) 
    #___________________________________________________________________________________________________________________________________________________________________________
    
    #side animation
    '''global homepage_pic1
    global homepage_pic2
    global homepage_pic3
    frame4=tk.Frame(Homepage_tab,highlightcolor='black',highlightbackground='black',highlightthickness=1)
    frame4.place(x=800,y=250,height=350,width=350)
    homepage_pic1 = Image.open('images/boy.png')
    homepage_pic2 = homepage_pic1.resize ((300,375), Image.ANTIALIAS)
    homepage_pic3 = ImageTk.PhotoImage(homepage_pic2)
    pic_lb = tk.Label(frame4, image = homepage_pic3)
    pic_lb.pack()'''
    #_____________________________________________________________________________________________________________________________________________________________
    
    #designing homepage ends here
#_________________________________________________________________________________________________________________________________________________________________


#_________________________________________________________________________________________________________________________________________________________________
#creating tk notebook with tabs to switch between pages
audio_nb=ttk.Notebook(window1)
audio_nb.pack(fill='both',expand=1)

Homepage_tab = tk.Frame(audio_nb,width=1250,height=750,bg='#FFBC8B')
English_tab = tk.Frame(audio_nb,width=1250,height=750,bg='#FFBC8B')
Hindi_tab = tk.Frame(audio_nb,width=1250,height=750,bg='#FFBC8B')
About_tab = tk.Frame(audio_nb,width=1250,height=750,bg='#FFBC8B')


audio_nb.add (Homepage_tab , text="Homepage")
audio_nb.add (English_tab , text="English Converter")
audio_nb.add (Hindi_tab , text="Hindi Converter")
audio_nb.add (About_tab , text="About")

audio_nb.hide(1)
audio_nb.hide(2)
audio_nb.hide(3)
#_________________________________________________________________________________________________________________________________________________________________

c=0 #this c is used for keeping track whether the person is visiting the home page for the first time 
#this is because if the user is visitng the homepage for the second time after already inputing his name then that info should only be dsplayed

homepage() #the first page which should always open is home page


    





window1.mainloop()













