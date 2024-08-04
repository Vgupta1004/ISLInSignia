

#_______
#importing all modules required throughout program
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
import speech_recognition as sr
import cv2 
import numpy as np
import time
import random
 
#from PyDictionary import PyDictionary
#_______
#defining the main window
window1=tk.Tk()
window1.title('Sign Language Generator')
window1.geometry('1250x700')
window1.iconbitmap('D:/Reliance school/Computer project/Danieledesantis-Audio-Video-Outline-Play.ico')
#_______
#_______
#function for taking name input in homepage
def EnterName():
    global user_name
    user_name=name_ent.get()
    global nameError_lb
    global wlcm_lb
    nameError_lb=tk.Label(frame3,text='*Please enter atleast one character for name',bg='#FFBC8B',fg='red',font=('Cambria',10))

    if len(user_name)<1:
        nameError_lb.place(x=200,y=5)
    else:               
        wlcm_lb=tk.Label(frame3,text='Welcome '+user_name+"!!!",font=('Cambria',20),bg='#FFBC8B')
        wlcm_lb.place(x=210,y=80)
        wlcm_lb2=tk.Label(frame3,text='Please check out the sign langauge generator tab...',font=('Cambria',20),bg='#FFBC8B')
        wlcm_lb2.place(x=60,y=130)
        nameError_lb.place_forget()
        
        name_ent['state']=tk.DISABLED
#_________________        
#function for quitting the program
def windestroy():
     tk.messagebox.showinfo("Quit","You have chosen to exit the program\nThank you for visiting!")
     window1.destroy()        
#_________________
#video display
def call(I):
  
    # Create a VideoCapture object and read from input file 
    cap = cv2.VideoCapture('videos/'+I+'.mp4') 
       
    # Check if camera opened successfully 
    if (cap.isOpened()== False):  
      tk.messagebox.showinfo("Video error!","Error opening video  file") 
       
    # Read until video is completed 
    while(cap.isOpened()): 
          
      # Capture frame-by-frame 
      ret, frame = cap.read() 
      if ret == True: 
       
        # Display the resulting frame
        cv2.moveWindow('Frame',530,140)
        cv2.imshow('Frame', frame) 
       
        # Press Q on keyboard to  exit 
        if cv2.waitKey(25) & 0xFF == ord('q'): 
           break
       
      # Break the loop 
      else:  
        break
       
    # When everything done, release  
    # the video capture object 
    cap.release() 
#_______________
#function to play the hin video
def play_hin():
    global c
    global list1
    global text_mainwords
    global btn_play
    c=0 #to check if all words have been displayed
    for i in list1:
    
        c+=1
        call(i)
    if c==(len(list1)):
      # Closes all the frames 
      time.sleep(1)
      cv2.destroyAllWindows()
      text_mainwords.destroy()
      hin_audio_btn['state']=tk.NORMAL
      hin_audio_ent['state']=tk.NORMAL
      hin_audio_ent.delete('0','end')
      btn_play['state']=tk.DISABLED
      global c1
      c1=0
#_________________
#function to play the eng video
def play_eng():
    
    global c
    global list1
    global text_mainwords
    global btn_play
    global end
    c=0 #to check if all words have been displayed
    for i in list1:
    
        c+=1
        call(i)
    if c==(len(list1)):
      # Closes all the frames 
      time.sleep(1)
      cv2.destroyAllWindows()
      text_mainwords.destroy()
      eng_audio_btn['state']=tk.NORMAL
      eng_audio_ent['state']=tk.NORMAL
      eng_audio_ent.delete('0','end')
      btn_play['state']=tk.DISABLED
      global c1
      c1=0
      
#_________________
#function to bifurcate input hindi sentence into main words
def Submit_hin():
    global start 
    global stop
    global punctuation
    global frame4
    global text_mainwords
    global btn_play
    global list1
    global sentences
    global hin_audio_ent
    
    text = hin_audio_ent.get()
    if len(text)>0:
        hin_audio_btn['state']=tk.DISABLED
        hin_audio_ent['state']=tk.DISABLED
        list1=[]
        for i in text:
            if i in punctuation:
                text=text.replace(i,' ')
        words = text.split()
        text_mainwords = tk.Text(frame4,width=200,height=200,bg='#FFBC8B',font=('Cambria',14),borderwidth=0)
        text_mainwords.pack(padx=20,pady=50)
        c = 0
        for i in words:

            if i in list_hin:
                list1.append(i)
                text_mainwords.insert('insert','-->'+i+'\n')
                c = c + 1
            if c==0:
                    for k in i:
                        if k == '्':
                            continue
                        list1.append(k)
                        text_mainwords.insert('insert','-->'+k+'\n')
            c = 0
                        
        frame5=tk.Frame(Hindi_tab,bg='#FFBC8B')
        frame5.place(x=750,y=350,width=300,height=300)
        btn_play= tk.Button(frame5,text='Play the video',command=play_hin,font=('Cambria',28),bg='#F29062')
        btn_play.place(x=20,y=20)
        
#_________________
#function to bifurcate input english sentence into main words
def Submit_eng():
   
    global frame4
    global text_mainwords
    global btn_play
    global list1
    global sentences
    global eng_audio_ent
    global punctuation
   
    
    text = eng_audio_ent.get().lower()
    if len(text)>0:
        eng_audio_btn['state']=tk.DISABLED
        eng_audio_ent['state']=tk.DISABLED
        list1=[]
        for i in text:
            if i in punctuation:
                text=text.replace(i,' ')
        words = text.split()
        text_mainwords = tk.Text(frame4,width=200,height=200,bg='#FFBC8B',font=('Cambria',14),borderwidth=0)
        text_mainwords.pack(padx=20,pady=50)
        c = 0
        print(words)
        if text in sentences:
                    list1=[text]
                    for i in words:
                        text_mainwords.insert('insert','-->'+i+'\n')
        else:
            for i in words:
                if i in verbs:
                    c = 0
                    continue
                
                else:
                    if i in list_eng:
                        list1.append(i)
                        text_mainwords.insert('insert','-->'+i+'\n')
                        c = c + 1
##                    else:
##                        s = (PyDictionary().synonym(i))
##                        for j in list_eng:
##                            if s!=None:
##                                if j in s:
##                                    list1.append(j)
##                                    text_mainwords.insert('insert','-->'+i+'\n')
##                                    c = c + 1
##                                    break
                                
                    if c==0:
                        for k in i:
                            list1.append(k)
                            text_mainwords.insert('insert','-->'+k+'\n')
                c = 0
                        
                    
        
        frame5=tk.Frame(English_tab,bg='#FFBC8B')
        frame5.place(x=750,y=350,width=300,height=300)
        btn_play= tk.Button(frame5,text='Play the video',command=play_eng,font=('Cambria',28),bg='#F29062')
        btn_play.place(x=20,y=20)
       
    
#_____________
#function for receiving audio in English Sign lanuguage generator
def receive_audio_eng():
    global c1
    global eng_audio_ent
    
    if c1==0:
        c1=1
    else:
        eng_audio_ent.delete('0','end')
        
    sample_rate = 48000
    chunk_size = 2048
    r = sr.Recognizer()
    
            
    with sr.Microphone(sample_rate = sample_rate,  chunk_size = chunk_size) as source:
        
        r.adjust_for_ambient_noise(source,duration=0.5)
        
        audio = r.listen(source) 
              
        try:          
            global speak_text
            global text                                                     
            speak_text = r.recognize_google(audio)   
            speak_text = speak_text[0].upper()+speak_text[1:len(speak_text)]
            eng_audio_ent.insert(0,speak_text)
      
                                 
            
            
        except sr.UnknownValueError: 
            tk.messagebox.showinfo('Input Error!!!',"Google Speech Recognition could not understand audio\nPlease enter again")
            #("Google Speech Recognition could not understand audio") 
      
        except sr.RequestError as e: 
           tk.messagebox.showinfo("Input Error!!!","Could not request results from Google Speech Recognition service; {0}".format(e))    
           #print("Could not request results from Google Speech Recognition service; {0}".format(e))
#__________________________________________________________________________________________________________________________________________
#function for receiving audio in English Sign lanuguage generator
def receive_audio_hin():
    global c1
    global hin_audio_ent
    
    if c1==0:
        c1=1
    else:
        hin_audio_ent.delete('0','end')
        
    sample_rate = 48000
    chunk_size = 2048
    r = sr.Recognizer()
    
            
    with sr.Microphone(sample_rate = sample_rate,  chunk_size = chunk_size) as source:
        
        r.adjust_for_ambient_noise(source,duration=0.5)
        
        audio = r.listen(source) 
              
        try:          
            global speak_text
            global text                                                     
            speak_text = r.recognize_google(audio,language='hi-IN')   
            hin_audio_ent.insert(0,speak_text)
      
                                 
            
            
        except sr.UnknownValueError: 
            tk.messagebox.showinfo('इनपुट त्रुटि !!! ' ,   " गूगल भाषण मान्यता ऑडियो नहीं समझ सका। कृपया फिर से दर्ज करें")
            #("Google Speech Recognition could not understand audio") 
      
        except sr.RequestError as e: 
           tk.messagebox.showinfo('इनपुट त्रुटि !!! ' ," गूगल भाषण मान्यता सेवा से परिणाम का अनुरोध नहीं किया जा सका". format(e))    
           #print("Could not request results from Google Speech Recognition service; {0}".format(e))

#__________________________________________________________________________________________________________________
#to run alphabets for dictionary
def alphabets():
    global frame_alpha
    global window2
    window2=tk.Tk()
    window2.title('Alphabets')
    window2.geometry('1250x700')
    window2.iconbitmap('D:/Reliance school/Computer project/Danieledesantis-Audio-Video-Outline-Play.ico')

    
    frame_alpha=tk.Frame(window2,bg="#FFBC8B")
    frame_alpha.place(x=0,y=0,width=1550,height=700)
    
    global letter_eng
    
    letter_eng = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    global x1
    global y1
    x1 = 50
    y1 = 45     
    global count
    global row
    count = 0
    row = 1
            
        
    for i in letter_eng:
                count+=1
                display_alpha(i)
                if count%6==0:
                    row+=1
                    y1+=110
                    if row==5:
                        x1 = 250
                    else:
                        x1 = 50
                else:
                    x1+=100
    global label_alpha1
    label_alpha1=tk.Label(frame_alpha,text= 'Choose the alphabet whose sign',bg="#FFBC8B",font=('Lucida Calligraphy',20))
    label_alpha1.place(x=700,y=40)
    global label_alpha2
    label_alpha2=tk.Label(frame_alpha,text= 'language you want to learn',bg="#FFBC8B",font=('Lucida Calligraphy',20))
    label_alpha2.place(x=720,y=90)
    

def call2(I):
   
    # Create a VideoCapture object and read from input file 
    cap = cv2.VideoCapture('videos/'+I+'.mp4') 
       
    # Check if camera opened successfully 
    if (cap.isOpened()== False):  
      tk.messagebox.showinfo("Video error!","Error opening video  file") 
       
    # Read until video is completed 
    while(cap.isOpened()): 
          
      # Capture frame-by-frame 
      ret, frame = cap.read() 
      #frame = imutils.resize(frame, width=270)
      if ret == True: 
       
        # Display the resulting frame
        cv2.moveWindow('Frame',820,200)
        cv2.imshow('Frame', frame) 
       
        # Press Q on keyboard to  exit 
        if cv2.waitKey(25) & 0xFF == ord('q'): 
           break
       
      # Break the loop 
      else:  
        break
       
    # When everything done, release  
    # the video capture object 
    cap.release() 


    
    
def which_button(button_press):
        call2(button_press)
        time.sleep(1)
        cv2.destroyAllWindows()
        
def display_alpha(i):
        global frame_alpha
        global element_alpha
        global x1
        global y1
        element_alpha = tk.Button(frame_alpha, text = i, command = lambda m=i:which_button(m), bg='#F29062',font=('Cambria',35))
        element_alpha.place(x = x1,y = y1,width=90)
   
#________________________________________________________________________________________________________________________    
#to run nature for dictionary
def nature():
        window3=tk.Tk()
        window3.title('Nature')
        window3.geometry('1250x700')
        window3.iconbitmap('D:/Reliance school/Computer project/Danieledesantis-Audio-Video-Outline-Play.ico')

        global frame_nature
        frame_nature=tk.Frame(window3,bg="#FFBC8B")
        frame_nature.place(x=0,y=0,width=1550,height=700)
        
        global list_nature
        list_nature=["greenery" ,"tree", "flower", 'environment', 'atmosphere', "rainbow", "grass", "air"]
    
        global x1
        global y1
        x1 = 50
        y1 = 45     
        global count
        global row
        count = 0
        row = 1
                
            
        for i in list_nature:
                    count+=1
                    display_nature(i)
                    if count%2==0:
                        row+=1
                        y1+=150
                        if row==5:
                            x1 = 250
                        else:
                            x1 = 50
                    else:
                        x1+=350
        global label_nature1
        label_nature1=tk.Label(frame_nature,text= 'Choose the word whose sign',bg="#FFBC8B",font=('Lucida Calligraphy',20))
        label_nature1.place(x=750,y=40)
        global label_nature2
        label_nature2=tk.Label(frame_nature,text= 'language you want to learn',bg="#FFBC8B",font=('Lucida Calligraphy',20))
        label_nature2.place(x=750,y=90)
    

def call3(I):
   
    # Create a VideoCapture object and read from input file 
    cap = cv2.VideoCapture('videos/'+I+'.mp4') 
       
    # Check if camera opened successfully 
    if (cap.isOpened()== False):  
      tk.messagebox.showinfo("Video error!","Error opening video  file") 
       
    # Read until video is completed 
    while(cap.isOpened()): 
          
      # Capture frame-by-frame 
      ret, frame = cap.read() 
      #frame = imutils.resize(frame, width=270)
      if ret == True: 
       
        # Display the resulting frame
        cv2.moveWindow('Frame',900,200)
        cv2.imshow('Frame', frame) 
       
        # Press Q on keyboard to  exit 
        if cv2.waitKey(25) & 0xFF == ord('q'): 
           break
       
      # Break the loop 
      else:  
        break
       
    # When everything done, release  
    # the video capture object 
    cap.release() 


    
    
def which_button(button_press):
        call3(button_press)
        time.sleep(1)
        cv2.destroyAllWindows()
        
def display_nature(i):
        global frame_nature
        global element_nature
        global x1
        global y1
        element_nature = tk.Button(frame_nature, text = i, command = lambda m=i:which_button(m), bg='#F29062',font=('Cambria',35))
        element_nature.place(x = x1,y = y1,width=290)
#______________________________________________________________________________________________________________________
#to run  numbers for dictionary
def numbers():
        window4=tk.Tk()
        window4.title('Numbers')
        window4.geometry('1250x700')
        window4.iconbitmap('D:/Reliance school/Computer project/Danieledesantis-Audio-Video-Outline-Play.ico')

        global frame_numbers
        frame_numbers=tk.Frame(window4,bg="#FFBC8B")
        frame_numbers.place(x=0,y=0,width=1550,height=700)
        
        global list_numbers
        list_numbers=['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
        global x1
        global y1
        x1 = 50
        y1 = 45     
        global count
        global row
        count = 0
        row = 1
                
            
        for i in list_numbers:
                    count+=1
                    display_numbers(i)
                    if count%3==0:
                        row+=1
                        y1+=150
                        if row==4:
                            x1 = 270
                        else:
                            x1 = 50
                    else:
                        x1+=220
        global label_numbers1
        label_numbers1=tk.Label(frame_numbers,text= 'Choose the number whose sign',bg="#FFBC8B",font=('Lucida Calligraphy',20))
        label_numbers1.place(x=750,y=40)
        global label_numbers2
        label_numbers2=tk.Label(frame_numbers,text= 'language you want to learn',bg="#FFBC8B",font=('Lucida Calligraphy',20))
        label_numbers2.place(x=750,y=90)
    

def call4(I):
   
    # Create a VideoCapture object and read from input file 
    cap = cv2.VideoCapture('videos/'+I+'.mp4') 
       
    # Check if camera opened successfully 
    if (cap.isOpened()== False):  
      tk.messagebox.showinfo("Video error!","Error opening video  file") 
       
    # Read until video is completed 
    while(cap.isOpened()): 
          
      # Capture frame-by-frame 
      ret, frame = cap.read() 
      #frame = imutils.resize(frame, width=270)
      if ret == True: 
       
        # Display the resulting frame
        cv2.moveWindow('Frame',900,200)
        cv2.imshow('Frame', frame) 
       
        # Press Q on keyboard to  exit 
        if cv2.waitKey(25) & 0xFF == ord('q'): 
           break
       
      # Break the loop 
      else:  
        break
       
    # When everything done, release  
    # the video capture object 
    cap.release() 


    
    
def which_button(button_press):
        call4(button_press)
        time.sleep(1)
        cv2.destroyAllWindows()
        
def display_numbers(i):
        global frame_numbers
        global element_numbers
        global x1
        global y1
        element_numbers = tk.Button(frame_numbers, text = i, command = lambda m=i:which_button(m), bg='#F29062',font=('Cambria',30))
        element_numbers.place(x = x1,y = y1,width=200)
#_____________________________________________________________________________________________________________________________
#to run  music for dictionary
def music():
        window5=tk.Tk()
        window5.title('Music')
        window5.geometry('1250x700')
        window5.iconbitmap('D:/Reliance school/Computer project/Danieledesantis-Audio-Video-Outline-Play.ico')

        global frame_music
        frame_music=tk.Frame(window5,bg="#FFBC8B")
        frame_music.place(x=0,y=0,width=1550,height=700)
        
        global list_music
        list_music=['drum', 'flute', 'sing', 'guitar', 'tabla', 'sound', 'music', 'echo']
    
        global x1
        global y1
        x1 = 50
        y1 = 75     
        global count
        global row
        count = 0
        row = 1
                
            
        for i in list_music:
                    count+=1
                    display_music(i)
                    if count%3==0:
                        row+=1
                        y1+=150
                        if row==3:
                            x1 = 200
                        else:
                            x1 = 50
                    else:
                        x1+=220
        global label_music1
        label_music1=tk.Label(frame_music,text= 'Choose the word whose sign',bg="#FFBC8B",font=('Lucida Calligraphy',20))
        label_music1.place(x=750,y=40)
        global label_music2
        label_music2=tk.Label(frame_music,text= 'language you want to learn',bg="#FFBC8B",font=('Lucida Calligraphy',20))
        label_music2.place(x=750,y=90)
    

def call5(I):
   
    # Create a VideoCapture object and read from input file 
    cap = cv2.VideoCapture('videos/'+I+'.mp4') 
       
    # Check if camera opened successfully 
    if (cap.isOpened()== False):  
      tk.messagebox.showinfo("Video error!","Error opening video  file") 
       
    # Read until video is completed 
    while(cap.isOpened()): 
          
      # Capture frame-by-frame 
      ret, frame = cap.read() 
      #frame = imutils.resize(frame, width=270)
      if ret == True: 
       
        # Display the resulting frame
        cv2.moveWindow('Frame',900,200)
        cv2.imshow('Frame', frame) 
       
        # Press Q on keyboard to  exit 
        if cv2.waitKey(25) & 0xFF == ord('q'): 
            break
       
      # Break the loop 
      else:  
        break
       
    # When everything done, release  
    # the video capture object 
    cap.release() 


    
    
def which_button(button_press):
        call5(button_press)
        time.sleep(1)
        cv2.destroyAllWindows()
        
def display_music(i):
        global frame_music
        global element_music
        global x1
        global y1
        element_music = tk.Button(frame_music, text = i, command = lambda m=i:which_button(m), bg='#F29062',font=('Cambria',30))
        element_music.place(x = x1,y = y1,width=200)
#_____________________________________________________________________________________________________________________________
#to run  sports for dictionary
def sports():
        window6=tk.Tk()
        window6.title('Music')
        window6.geometry('1250x700')
        window6.iconbitmap('D:/Reliance school/Computer project/Danieledesantis-Audio-Video-Outline-Play.ico')

        global frame_sports
        frame_sports=tk.Frame(window6,bg="#FFBC8B")
        frame_sports.place(x=0,y=0,width=1550,height=700)
        
        global list_sports
        list_sports=['swimming', 'running', 'goal', 'game', 'badminton']
    
        global x1
        global y1
        x1 = 80
        y1 = 125     
        global count
        global row
        count = 0
        row = 1
                
            
        for i in list_sports:
                    count+=1
                    display_sports(i)
                    if count%2==0:
                        row+=1
                        y1+=150
                        if row==3:
                            x1 = 170
                        else:
                            x1 = 80
                    else:
                        x1+=220
        global label_sports1
        label_sports1=tk.Label(frame_sports,text= 'Choose the word whose sign',bg="#FFBC8B",font=('Lucida Calligraphy',20))
        label_sports1.place(x=750,y=40)
        global label_sports2
        label_sports2=tk.Label(frame_sports,text= 'language you want to learn',bg="#FFBC8B",font=('Lucida Calligraphy',20))
        label_sports2.place(x=750,y=90)
    

def call6(I):
   
    # Create a VideoCapture object and read from input file 
    cap = cv2.VideoCapture('videos/'+I+'.mp4') 
       
    # Check if camera opened successfully 
    if (cap.isOpened()== False):  
      tk.messagebox.showinfo("Video error!","Error opening video  file") 
       
    # Read until video is completed 
    while(cap.isOpened()): 
          
      # Capture frame-by-frame 
      ret, frame = cap.read() 
      #frame = imutils.resize(frame, width=270)
      if ret == True: 
       
        # Display the resulting frame
        cv2.moveWindow('Frame',900,200)
        cv2.imshow('Frame', frame) 
       
        # Press Q on keyboard to  exit 
        if cv2.waitKey(25) & 0xFF == ord('q'): 
            break
       
      # Break the loop 
      else:  
        break
       
    # When everything done, release  
    # the video capture object 
    cap.release() 


    
    
def which_button(button_press):
        call6(button_press)
        time.sleep(1)
        cv2.destroyAllWindows()
        
def display_sports(i):
        global frame_sports
        global element_sports
        global x1
        global y1
        element_sports = tk.Button(frame_sports, text = i, command = lambda m=i:which_button(m), bg='#F29062',font=('Cambria',30))
        element_sports.place(x = x1,y = y1,width=200)
#_____________________________________________________________________________________________________________________________

#to run  colours for dictionary
def colours():
        window6=tk.Tk()
        window6.title('Colours')
        window6.geometry('1250x700')
        window6.iconbitmap('D:/Reliance school/Computer project/Danieledesantis-Audio-Video-Outline-Play.ico')

        global frame_colours
        frame_colours=tk.Frame(window6,bg="#FFBC8B")
        frame_colours.place(x=0,y=0,width=1550,height=700)
        
        global list_colours
        list_colours=['colour', 'pink', 'yellow', 'black', 'blue', 'green', 'orange', 'red', 'white','purple', 'pink', 'orange', 'grey', 'green', 'golden', 'silver', 'brown']
    
        global x1
        global y1
        x1 = 50
        y1 = 75     
        global count
        global row
        count = 0
        row = 1
                
            
        for i in list_colours:
                    count+=1
                    display_colours(i)
                    if count%4==0:
                        row+=1
                        y1+=120
                        if row==5:
                            x1 = 280
                        else:
                            x1 = 50
                    else:
                        x1+=160
        global label_colours1
        label_colours1=tk.Label(frame_colours,text= 'Choose the word whose sign',bg="#FFBC8B",font=('Lucida Calligraphy',20))
        label_colours1.place(x=750,y=40)
        global label_colours2
        label_colours2=tk.Label(frame_colours,text= 'language you want to learn',bg="#FFBC8B",font=('Lucida Calligraphy',20))
        label_colours2.place(x=750,y=90)
    

def call7(I):
   
    # Create a VideoCapture object and read from input file 
    cap = cv2.VideoCapture('videos/'+I+'.mp4') 
       
    # Check if camera opened successfully 
    if (cap.isOpened()== False):  
      tk.messagebox.showinfo("Video error!","Error opening video  file") 
       
    # Read until video is completed 
    while(cap.isOpened()): 
          
      # Capture frame-by-frame 
      ret, frame = cap.read() 
      #frame = imutils.resize(frame, width=270)
      if ret == True: 
       
        # Display the resulting frame
        cv2.moveWindow('Frame',900,200)
        cv2.imshow('Frame', frame) 
       
        # Press Q on keyboard to  exit 
        if cv2.waitKey(25) & 0xFF == ord('q'): 
            break
       
      # Break the loop 
      else:  
        break
       
    # When everything done, release  
    # the video capture object 
    cap.release() 


    
    
def which_button(button_press):
        call7(button_press)
        time.sleep(1)
        cv2.destroyAllWindows()
        
def display_colours(i):
        global frame_colours
        global element_colours
        global x1
        global y1
        element_colours = tk.Button(frame_colours, text = i, command = lambda m=i:which_button(m), bg='#F29062',font=('Cambria',20))
        element_colours.place(x = x1,y = y1,width=120)
#_____________________________________________________________________________________________________________________________________________
#to run  action for dictionary
def action():
        window7=tk.Tk()
        window7.title('Action')
        window7.geometry('1250x700')
        window7.iconbitmap('D:/Reliance school/Computer project/Danieledesantis-Audio-Video-Outline-Play.ico')

        global frame_action
        frame_action=tk.Frame(window7,bg="#FFBC8B")
        frame_action.place(x=0,y=0,width=1550,height=700)
        
        global list_action
        list_action=['open', 'whistle', 'start', 'stop', 'sing', 'visit', 'wait', 'wash', 'wear', 'concentrate', 'run', 'see', 'sit', 'sleep', 'smell', 'stand', 'talk', 'speak', 'trust', 'trouble', 'record', 'lie', 'study', 'snows', 'mix', 'introduce', 'interest', 'increase', 'help', 'hear', 'go', 'fall', 'fail', 'enjoy', 'eat', 'earn' , 'doubt', 'dance', 'cry' , 'copy', 'come', 'change', 'cancel', 'can', 'call', 'buy', 'born', 'beat', 'ball', 'ask', 'advance', 'add', 'like', 'grow', 'build']    
        global x1
        global y1
        x1 = 30
        y1 = 25     
        global count
        global row
        count = 0
        row = 1
                
            
        for i in list_action:
                    count+=1
                    display_action(i)
                    if count%6==0:
                        row+=1
                        y1+=60
                        if row==10:
                            x1 = 300
                        else:
                            x1 = 30
                    else:
                        x1+=120
        global label_action1
        label_action1=tk.Label(frame_action,text= 'Choose the word whose sign',bg="#FFBC8B",font=('Lucida Calligraphy',20))
        label_action1.place(x=780,y=40)
        global label_action2
        label_action2=tk.Label(frame_action,text= 'language you want to learn',bg="#FFBC8B",font=('Lucida Calligraphy',20))
        label_action2.place(x=780,y=90)
    

def call8(I):
   
    # Create a VideoCapture object and read from input file 
    cap = cv2.VideoCapture('videos/'+I+'.mp4') 
       
    # Check if camera opened successfully 
    if (cap.isOpened()== False):  
      tk.messagebox.showinfo("Video error!","Error opening video  file") 
       
    # Read until video is completed 
    while(cap.isOpened()): 
          
      # Capture frame-by-frame 
      ret, frame = cap.read() 
      #frame = imutils.resize(frame, width=270)
      if ret == True: 
       
        # Display the resulting frame
        cv2.moveWindow('Frame',900,200)
        cv2.imshow('Frame', frame) 
       
        # Press Q on keyboard to  exit 
        if cv2.waitKey(25) & 0xFF == ord('q'): 
            break
       
      # Break the loop 
      else:  
        break
       
    # When everything done, release  
    # the video capture object 
    cap.release() 


    
    
def which_button(button_press):
        call8(button_press)
        time.sleep(1)
        cv2.destroyAllWindows()
        
def display_action(i):
        global frame_action
        global element_action
        global x1
        global y1
        element_action = tk.Button(frame_action, text = i, command = lambda m=i:which_button(m), bg='#F29062',font=('Cambria',15))
        element_action.place(x = x1,y = y1,width=110)
#___________________________________________________________________________________________________________________________________________

#to run  question for dictionary
def question():
        window8=tk.Tk()
        window8.title('question')
        window8.geometry('1250x700')
        window8.iconbitmap('D:/Reliance school/Computer project/Danieledesantis-Audio-Video-Outline-Play.ico')

        global frame_question
        frame_question=tk.Frame(window8,bg="#FFBC8B")
        frame_question.place(x=0,y=0,width=1550,height=700)
        
        global list_question
        list_question=['what','when','where','which','who','why', 'how']    
        global x1
        global y1
        x1 = 50
        y1 = 75     
        global count
        global row
        count = 0
        row = 1
                
            
        for i in list_question:
                    count+=1
                    display_question(i)
                    if count%3==0:
                        row+=1
                        y1+=150
                        if row==3:
                            x1 = 200
                        else:
                            x1 = 50
                    else:
                        x1+=220
        global label_question1
        label_question1=tk.Label(frame_question,text= 'Choose the word whose sign',bg="#FFBC8B",font=('Lucida Calligraphy',20))
        label_question1.place(x=750,y=40)
        global label_question2
        label_question2=tk.Label(frame_question,text= 'language you want to learn',bg="#FFBC8B",font=('Lucida Calligraphy',20))
        label_question2.place(x=750,y=90)
    

def call9(I):
   
    # Create a VideoCapture object and read from input file 
    cap = cv2.VideoCapture('videos/'+I+'.mp4') 
       
    # Check if camera opened successfully 
    if (cap.isOpened()== False):  
      tk.messagebox.showinfo("Video error!","Error opening video  file") 
       
    # Read until video is completed 
    while(cap.isOpened()): 
          
      # Capture frame-by-frame 
      ret, frame = cap.read() 
      #frame = imutils.resize(frame, width=270)
      if ret == True: 
       
        # Display the resulting frame
        cv2.moveWindow('Frame',900,200)
        cv2.imshow('Frame', frame) 
       
        # Press Q on keyboard to  exit 
        if cv2.waitKey(25) & 0xFF == ord('q'): 
            break
       
      # Break the loop 
      else:  
        break
       
    # When everything done, release  
    # the video capture object 
    cap.release() 


    
    
def which_button(button_press):
        call9(button_press)
        time.sleep(1)
        cv2.destroyAllWindows()
        
def display_question(i):
        global frame_question
        global element_question
        global x1
        global y1
        element_question = tk.Button(frame_question, text = i, command = lambda m=i:which_button(m), bg='#F29062',font=('Cambria',30))
        element_question.place(x = x1,y = y1,width=200)
#____________________________________________________________________________________________________________________________________________

#to run  art for dictionary
def art():
        window8=tk.Tk()
        window8.title('Art and Entertainment')
        window8.geometry('1250x700')
        window8.iconbitmap('D:/Reliance school/Computer project/Danieledesantis-Audio-Video-Outline-Play.ico')

        global frame_art
        frame_art=tk.Frame(window8,bg="#FFBC8B")
        frame_art.place(x=0,y=0,width=1550,height=700)
        
        global list_art
        list_art=['art', 'cinema', 'entertainment', 'magic', 'sculpture', 'stage', 'tv', 'television', 'radio', 'music', 'film'] 
        global x1
        global y1
        x1 = 30
        y1 = 75     
        global count
        global row
        count = 0
        row = 1
                
            
        for i in list_art:
                    count+=1
                    display_art(i)
                    if count%3==0:
                        row+=1
                        y1+=150
                        if row==4:
                            x1 = 180
                        else:
                            x1 = 30
                    else:
                        x1+=240
        global label_art1
        label_art1=tk.Label(frame_art,text= 'Choose the word whose sign',bg="#FFBC8B",font=('Lucida Calligraphy',20))
        label_art1.place(x=760,y=45)
        global label_art2
        label_art2=tk.Label(frame_art,text= 'language you want to learn',bg="#FFBC8B",font=('Lucida Calligraphy',20))
        label_art2.place(x=760,y=95)
    

def call10(I):
   
    # Create a VideoCapture object and read from input file 
    cap = cv2.VideoCapture('videos/'+I+'.mp4') 
       
    # Check if camera opened successfully 
    if (cap.isOpened()== False):  
      tk.messagebox.showinfo("Video error!","Error opening video  file") 
       
    # Read until video is completed 
    while(cap.isOpened()): 
          
      # Capture frame-by-frame 
      ret, frame = cap.read() 
      #frame = imutils.resize(frame, width=270)
      if ret == True: 
       
        # Display the resulting frame
        cv2.moveWindow('Frame',900,200)
        cv2.imshow('Frame', frame) 
       
        # Press Q on keyboard to  exit 
        if cv2.waitKey(25) & 0xFF == ord('q'): 
            break
       
      # Break the loop 
      else:  
        break
       
    # When everything done, release  
    # the video capture object 
    cap.release() 


    
    
def which_button(button_press):
        call10(button_press)
        time.sleep(1)
        cv2.destroyAllWindows()
        
def display_art(i):
        global frame_art
        global element_art
        global x1
        global y1
        element_art = tk.Button(frame_art, text = i, command = lambda m=i:which_button(m), bg='#F29062',font=('Cambria',25))
        element_art.place(x = x1,y = y1,width=220)
#____________________________________________________________________________________________________________________________________

#to run  object for dictionary
def object():
        window8=tk.Tk()
        window8.title('Objects')
        window8.geometry('1250x700')
        window8.iconbitmap('D:/Reliance school/Computer project/Danieledesantis-Audio-Video-Outline-Play.ico')

        global frame_object
        frame_object=tk.Frame(window8,bg="#FFBC8B")
        frame_object.place(x=0,y=0,width=1550,height=700)
        
        global list_object
        list_object=[ 'balloon', 'doll', 'spoon', 'plate', 'towel', 'umbrella', 'window', 'clocks', 'sofa', 'electronic', 'battery', 'tv', 'television', 'telescope', 'pendulum', 'light', 'house', 'glass', 'gate', 'floor', 'fire', 'document', 'desk', 'chair', 'cap', 'camera', 'boat', 'thing'] 
        global x1
        global y1
        x1 = 30
        y1 = 45     
        global count
        global row
        count = 0
        row = 1
                
            
        for i in list_object:
                    count+=1
                    display_object(i)
                    if count%5==0:
                        row+=1
                        y1+=100
                        if row==6:
                            x1 = 170
                        else:
                            x1 = 30
                    else:
                        x1+=140
        global label_object1
        label_object1=tk.Label(frame_object,text= 'Choose the word whose sign',bg="#FFBC8B",font=('Lucida Calligraphy',20))
        label_object1.place(x=750,y=40)
        global label_object2
        label_object2=tk.Label(frame_object,text= 'language you want to learn',bg="#FFBC8B",font=('Lucida Calligraphy',20))
        label_object2.place(x=750,y=90)
    

def call11(I):
   
    # Create a VideoCapture object and read from input file 
    cap = cv2.VideoCapture('videos/'+I+'.mp4') 
       
    # Check if camera opened successfully 
    if (cap.isOpened()== False):  
      tk.messagebox.showinfo("Video error!","Error opening video  file") 
       
    # Read until video is completed 
    while(cap.isOpened()): 
          
      # Capture frame-by-frame 
      ret, frame = cap.read() 
      #frame = imutils.resize(frame, width=270)
      if ret == True: 
       
        # Display the resulting frame
        cv2.moveWindow('Frame',900,200)
        cv2.imshow('Frame', frame) 
       
        # Press Q on keyboard to  exit 
        if cv2.waitKey(25) & 0xFF == ord('q'): 
            break
       
      # Break the loop 
      else:  
        break
       
    # When everything done, release  
    # the video capture object 
    cap.release() 


    
    
def which_button(button_press):
        call11(button_press)
        time.sleep(1)
        cv2.destroyAllWindows()
        
def display_object(i):
        global frame_object
        global element_object
        global x1
        global y1
        element_object = tk.Button(frame_object, text = i, command = lambda m=i:which_button(m), bg='#F29062',font=('Cambria',18))
        element_object.place(x = x1,y = y1,width=130)
#____________________________________________________________________________________________________________________________________
#to run  adjective for dictionary
def adjective():
        window8=tk.Tk()
        window8.title('adjectives')
        window8.geometry('1250x700')
        window8.iconbitmap('D:/Reliance school/Computer project/Danieledesantis-Audio-Video-Outline-Play.ico')

        global frame_adjective
        frame_adjective=tk.Frame(window8,bg="#FFBC8B")
        frame_adjective.place(x=0,y=0,width=1550,height=700)
        
        global list_adjective
        list_adjective=[ 'wet', 'common', 'young', 'old', 'brave', 'busy', 'intelligent', 'confident', 'wrong', 'right', 'patient', 'map', 'hardworking', 'expert', 'strong', 'sad','proud', 'nice', 'lazy', 'happy', 'good', 'fat', 'free', 'hot', 'empty', 'difficult', 'dark', 'cold', 'clever', 'careless', 'calm', 'bright', 'beautiful', 'bad', 'powerful', 'easy']
        global x1
        global y1
        x1 = 30
        y1 = 45     
        global count
        global row
        count = 0
        row = 1
                
            
        for i in list_adjective:
                    count+=1
                    display_adjective(i)
                    if count%4==0:
                        row+=1
                        y1+=60
                        if row==17:
                            x1 = 200
                        else:
                            x1 = 30
                    else:
                        x1+=180
        global label_adjective1
        label_adjective1=tk.Label(frame_adjective,text= 'Choose the word whose sign',bg="#FFBC8B",font=('Lucida Calligraphy',20))
        label_adjective1.place(x=750,y=40)
        global label_adjective2
        label_adjective2=tk.Label(frame_adjective,text= 'language you want to learn',bg="#FFBC8B",font=('Lucida Calligraphy',20))
        label_adjective2.place(x=750,y=90)
    

def call12(I):
   
    # Create a VideoCapture adjective and read from input file 
    cap = cv2.VideoCapture('videos/'+I+'.mp4') 
       
    # Check if camera opened successfully 
    if (cap.isOpened()== False):  
      tk.messagebox.showinfo("Video error!","Error opening video  file") 
       
    # Read until video is completed 
    while(cap.isOpened()): 
          
      # Capture frame-by-frame 
      ret, frame = cap.read() 
      #frame = imutils.resize(frame, width=270)
      if ret == True: 
       
        # Display the resulting frame
        cv2.moveWindow('Frame',900,200)
        cv2.imshow('Frame', frame) 
       
        # Press Q on keyboard to  exit 
        if cv2.waitKey(25) & 0xFF == ord('q'): 
            break
       
      # Break the loop 
      else:  
        break
       
    # When everything done, release  
    # the video capture adjective 
    cap.release() 


    
    
def which_button(button_press):
        call12(button_press)
        time.sleep(1)
        cv2.destroyAllWindows()
        
def display_adjective(i):
        global frame_adjective
        global element_adjective
        global x1
        global y1
        element_adjective = tk.Button(frame_adjective, text = i, command = lambda m=i:which_button(m), bg='#F29062',font=('Cambria',18))
        element_adjective.place(x = x1,y = y1,width=150)
#___________________________________________________________________

#to run  body for dictionary
def body():
        window8=tk.Tk()
        window8.title('Body Parts')
        window8.geometry('1250x700')
        window8.iconbitmap('D:/Reliance school/Computer project/Danieledesantis-Audio-Video-Outline-Play.ico')

        global frame_body
        frame_body=tk.Frame(window8,bg="#FFBC8B")
        frame_body.place(x=0,y=0,width=1550,height=700)
        
        global list_body
        list_body=['nose', 'hairs', 'heart', 'face', 'eye', 'elbow', 'arm']
        global x1
        global y1
        x1 = 50
        y1 = 75     
        global count
        global row
        count = 0
        row = 1
                
            
        for i in list_body:
                    count+=1
                    display_body(i)
                    if count%3==0:
                        row+=1
                        y1+=150
                        if row==3:
                            x1 = 270
                        else:
                            x1 = 50
                    else:
                        x1+=220
        global label_body1
        label_body1=tk.Label(frame_body,text= 'Choose the word whose sign',bg="#FFBC8B",font=('Lucida Calligraphy',20))
        label_body1.place(x=750,y=40)
        global label_body2
        label_body2=tk.Label(frame_body,text= 'language you want to learn',bg="#FFBC8B",font=('Lucida Calligraphy',20))
        label_body2.place(x=750,y=90)
    

def call13(I):
   
    # Create a VideoCapture body and read from input file 
    cap = cv2.VideoCapture('videos/'+I+'.mp4') 
       
    # Check if camera opened successfully 
    if (cap.isOpened()== False):  
      tk.messagebox.showinfo("Video error!","Error opening video  file") 
       
    # Read until video is completed 
    while(cap.isOpened()): 
          
      # Capture frame-by-frame 
      ret, frame = cap.read() 
      #frame = imutils.resize(frame, width=270)
      if ret == True: 
       
        # Display the resulting frame
        cv2.moveWindow('Frame',900,200)
        cv2.imshow('Frame', frame) 
       
        # Press Q on keyboard to  exit 
        if cv2.waitKey(25) & 0xFF == ord('q'): 
            break
       
      # Break the loop 
      else:  
        break
       
    # When everything done, release  
    # the video capture body 
    cap.release() 


    
    
def which_button(button_press):
        call13(button_press)
        time.sleep(1)
        cv2.destroyAllWindows()
        
def display_body(i):
        global frame_body
        global element_body
        global x1
        global y1
        element_body = tk.Button(frame_body, text = i, command = lambda m=i:which_button(m), bg='#F29062',font=('Cambria',30))
        element_body.place(x = x1,y = y1,width=200)
#____________________________________
        
#to run  emotion for dictionary
def emotion():
        window8=tk.Tk()
        window8.title('Emotions')
        window8.geometry('1250x700')
        window8.iconbitmap('D:/Reliance school/Computer project/Danieledesantis-Audio-Video-Outline-Play.ico')

        global frame_emotion
        frame_emotion=tk.Frame(window8,bg="#FFBC8B")
        frame_emotion.place(x=0,y=0,width=1550,height=700)
        
        global list_emotion
        list_emotion=['pain', 'hope','happy', 'sad', 'feel', 'fear', 'anger']
        global x1
        global y1
        x1 = 50
        y1 = 75     
        global count
        global row
        count = 0
        row = 1
                
            
        for i in list_emotion:
                    count+=1
                    display_emotion(i)
                    if count%3==0:
                        row+=1
                        y1+=150
                        if row==3:
                            x1 = 270
                        else:
                            x1 = 50
                    else:
                        x1+=220
        global label_emotion1
        label_emotion1=tk.Label(frame_emotion,text= 'Choose the word whose sign',bg="#FFBC8B",font=('Lucida Calligraphy',20))
        label_emotion1.place(x=750,y=40)
        global label_emotion2
        label_emotion2=tk.Label(frame_emotion,text= 'language you want to learn',bg="#FFBC8B",font=('Lucida Calligraphy',20))
        label_emotion2.place(x=750,y=90)
    

def call14(I):
   
    # Create a VideoCapture emotion and read from input file 
    cap = cv2.VideoCapture('videos/'+I+'.mp4') 
       
    # Check if camera opened successfully 
    if (cap.isOpened()== False):  
      tk.messagebox.showinfo("Video error!","Error opening video  file") 
       
    # Read until video is completed 
    while(cap.isOpened()): 
          
      # Capture frame-by-frame 
      ret, frame = cap.read() 
      #frame = imutils.resize(frame, width=270)
      if ret == True: 
       
        # Display the resulting frame
        cv2.moveWindow('Frame',900,200)
        cv2.imshow('Frame', frame) 
       
        # Press Q on keyboard to  exit 
        if cv2.waitKey(25) & 0xFF == ord('q'): 
            break
       
      # Break the loop 
      else:  
        break
       
    # When everything done, release  
    # the video capture emotion 
    cap.release() 


    
    
def which_button(button_press):
        call14(button_press)
        time.sleep(1)
        cv2.destroyAllWindows()
        
def display_emotion(i):
        global frame_emotion
        global element_emotion
        global x1
        global y1
        element_emotion = tk.Button(frame_emotion, text = i, command = lambda m=i:which_button(m), bg='#F29062',font=('Cambria',30))
        element_emotion.place(x = x1,y = y1,width=200)
#_______________________________________________________________________
    
#to run  food for dictionary
def food():
        window8=tk.Tk()
        window8.title('Foods')
        window8.geometry('1250x700')
        window8.iconbitmap('D:/Reliance school/Computer project/Danieledesantis-Audio-Video-Outline-Play.ico')

        global frame_food
        frame_food=tk.Frame(window8,bg="#FFBC8B")
        frame_food.place(x=0,y=0,width=1550,height=700)
        
        global list_food
        list_food=['tea', 'milk', 'wada', 'sambhar', 'roti', 'idli', 'dosa', 'dinner']
        global x1
        global y1
        x1 = 50
        y1 = 75     
        global count
        global row
        count = 0
        row = 1
                
            
        for i in list_food:
                    count+=1
                    display_food(i)
                    if count%3==0:
                        row+=1
                        y1+=150
                        if row==3:
                            x1 = 200
                        else:
                            x1 = 50
                    else:
                        x1+=220
        global label_food1
        label_food1=tk.Label(frame_food,text= 'Choose the word whose sign',bg="#FFBC8B",font=('Lucida Calligraphy',20))
        label_food1.place(x=750,y=40)
        global label_food2
        label_food2=tk.Label(frame_food,text= 'language you want to learn',bg="#FFBC8B",font=('Lucida Calligraphy',20))
        label_food2.place(x=750,y=90)
    

def call15(I):
   
    # Create a VideoCapture food and read from input file 
    cap = cv2.VideoCapture('videos/'+I+'.mp4') 
       
    # Check if camera opened successfully 
    if (cap.isOpened()== False):  
      tk.messagebox.showinfo("Video error!","Error opening video  file") 
       
    # Read until video is completed 
    while(cap.isOpened()): 
          
      # Capture frame-by-frame 
      ret, frame = cap.read() 
      #frame = imutils.resize(frame, width=270)
      if ret == True: 
       
        # Display the resulting frame
        cv2.moveWindow('Frame',900,200)
        cv2.imshow('Frame', frame) 
       
        # Press Q on keyboard to  exit 
        if cv2.waitKey(25) & 0xFF == ord('q'): 
            break
       
      # Break the loop 
      else:  
        break
       
    # When everything done, release  
    # the video capture food 
    cap.release() 


    
    
def which_button(button_press):
        call15(button_press)
        time.sleep(1)
        cv2.destroyAllWindows()
        
def display_food(i):
        global frame_food
        global element_food
        global x1
        global y1
        element_food = tk.Button(frame_food, text = i, command = lambda m=i:which_button(m), bg='#F29062',font=('Cambria',30))
        element_food.place(x = x1,y = y1,width=200)
#___________________________________________________________________________________________________________________

#to run  times for dictionary
def times():
        window8=tk.Tk()
        window8.title('Time')
        window8.geometry('1250x700')
        window8.iconbitmap('D:/Reliance school/Computer project/Danieledesantis-Audio-Video-Outline-Play.ico')

        global frame_times
        frame_times=tk.Frame(window8,bg="#FFBC8B")
        frame_times.place(x=0,y=0,width=1550,height=700)
        
        global list_times
        list_times=['morning', 'evening', 'night', 'day' , 'month', 'year', 'date', 'afternoon']
        global x1
        global y1
        x1 = 50
        y1 = 75     
        global count
        global row
        count = 0
        row = 1
                
            
        for i in list_times:
                    count+=1
                    display_times(i)
                    if count%3==0:
                        row+=1
                        y1+=150
                        if row==3:
                            x1 = 200
                        else:
                            x1 = 50
                    else:
                        x1+=220
        global label_times1
        label_times1=tk.Label(frame_times,text= 'Choose the word whose sign',bg="#FFBC8B",font=('Lucida Calligraphy',20))
        label_times1.place(x=750,y=40)
        global label_times2
        label_times2=tk.Label(frame_times,text= 'language you want to learn',bg="#FFBC8B",font=('Lucida Calligraphy',20))
        label_times2.place(x=750,y=90)
    

def call16(I):
   
    # Create a VideoCapture times and read from input file 
    cap = cv2.VideoCapture('videos/'+I+'.mp4') 
       
    # Check if camera opened successfully 
    if (cap.isOpened()== False):  
      tk.messagebox.showinfo("Video error!","Error opening video  file") 
       
    # Read until video is completed 
    while(cap.isOpened()): 
          
      # Capture frame-by-frame 
      ret, frame = cap.read() 
      #frame = imutils.resize(frame, width=270)
      if ret == True: 
       
        # Display the resulting frame
        cv2.moveWindow('Frame',900,200)
        cv2.imshow('Frame', frame) 
       
        # Press Q on keyboard to  exit 
        if cv2.waitKey(25) & 0xFF == ord('q'): 
            break
       
      # Break the loop 
      else:  
        break
       
    # When everything done, release  
    # the video capture times 
    cap.release() 


    
    
def which_button(button_press):
        call16(button_press)
        time.sleep(1)
        cv2.destroyAllWindows()
        
def display_times(i):
        global frame_times
        global element_times
        global x1
        global y1
        element_times = tk.Button(frame_times, text = i, command = lambda m=i:which_button(m), bg='#F29062',font=('Cambria',30))
        element_times.place(x = x1,y = y1,width=200)
#__________________________________________________________________________________________________________________________________

#to run  geography for dictionary
def geography():
        window8=tk.Tk()
        window8.title('Geography')
        window8.geometry('1250x700')
        window8.iconbitmap('D:/Reliance school/Computer project/Danieledesantis-Audio-Video-Outline-Play.ico')

        global frame_geography
        frame_geography=tk.Frame(window8,bg="#FFBC8B")
        frame_geography.place(x=0,y=0,width=1550,height=700)
        
        global list_geography
        list_geography=['universe', 'equator', 'eclipse', 'atmosphere', 'world', 'sun', 'stars', 'moon', 'india', 'west', 'south', 'north', 'map', 'east', 'earth']
        global x1
        global y1
        x1 = 50
        y1 = 45     
        global count
        global row
        count = 0
        row = 1
                
            
        for i in list_geography:
                    count+=1
                    display_geography(i)
                    if count%3==0:
                        row+=1
                        y1+=120
                        if row==13:
                            x1 = 200
                        else:
                            x1 = 50
                    else:
                        x1+=220
        global label_geography1
        label_geography1=tk.Label(frame_geography,text= 'Choose the word whose sign',bg="#FFBC8B",font=('Lucida Calligraphy',20))
        label_geography1.place(x=750,y=40)
        global label_geography2
        label_geography2=tk.Label(frame_geography,text= 'language you want to learn',bg="#FFBC8B",font=('Lucida Calligraphy',20))
        label_geography2.place(x=750,y=90)
    

def call16(I):
   
    # Create a VideoCapture geography and read from input file 
    cap = cv2.VideoCapture('videos/'+I+'.mp4') 
       
    # Check if camera opened successfully 
    if (cap.isOpened()== False):  
      tk.messagebox.showinfo("Video error!","Error opening video  file") 
       
    # Read until video is completed 
    while(cap.isOpened()): 
          
      # Capture frame-by-frame 
      ret, frame = cap.read() 
      #frame = imutils.resize(frame, width=270)
      if ret == True: 
       
        # Display the resulting frame
        cv2.moveWindow('Frame',900,200)
        cv2.imshow('Frame', frame) 
       
        # Press Q on keyboard to  exit 
        if cv2.waitKey(25) & 0xFF == ord('q'): 
            break
       
      # Break the loop 
      else:  
        break
       
    # When everything done, release  
    # the video capture geography 
    cap.release() 


    
    
def which_button(button_press):
        call16(button_press)
        time.sleep(1)
        cv2.destroyAllWindows()
        
def display_geography(i):
        global frame_geography
        global element_geography
        global x1
        global y1
        element_geography = tk.Button(frame_geography, text = i, command = lambda m=i:which_button(m), bg='#F29062',font=('Cambria',25))
        element_geography.place(x = x1,y = y1,width=200)
#________________________________________________________________________________________________________________________________________-

#to run  continents for dictionary
def continents():
        window8=tk.Tk()
        window8.title('continents')
        window8.geometry('1250x700')
        window8.iconbitmap('D:/Reliance school/Computer project/Danieledesantis-Audio-Video-Outline-Play.ico')

        global frame_continents
        frame_continents=tk.Frame(window8,bg="#FFBC8B")
        frame_continents.place(x=0,y=0,width=1550,height=700)
        
        global list_continents
        list_continents=['continent', 'australia', 'asia', 'antartica', 'africa','europe','south america', 'north america']
        global x1
        global y1
        x1 = 140
        y1 = 55     
        global count
        global row
        count = 0
        row = 1
                
            
        for i in list_continents:
                    count+=1
                    display_continents(i)
                    if count%1==0:
                        row+=1
                        y1+=70
                        if row==10:
                            x1 = 200
                        else:
                            x1 = 140
                    else:
                        x1+=220
        global label_continents1
        label_continents1=tk.Label(frame_continents,text= 'Choose the word whose sign',bg="#FFBC8B",font=('Lucida Calligraphy',20))
        label_continents1.place(x=750,y=40)
        global label_continents2
        label_continents2=tk.Label(frame_continents,text= 'language you want to learn',bg="#FFBC8B",font=('Lucida Calligraphy',20))
        label_continents2.place(x=750,y=90)
    

def call17(I):
   
    # Create a VideoCapture continents and read from input file 
    cap = cv2.VideoCapture('videos/'+I+'.mp4') 
       
    # Check if camera opened successfully 
    if (cap.isOpened()== False):  
      tk.messagebox.showinfo("Video error!","Error opening video  file") 
       
    # Read until video is completed 
    while(cap.isOpened()): 
          
      # Capture frame-by-frame 
      ret, frame = cap.read() 
      #frame = imutils.resize(frame, width=270)
      if ret == True: 
       
        # Display the resulting frame
        cv2.moveWindow('Frame',900,200)
        cv2.imshow('Frame', frame) 
       
        # Press Q on keyboard to  exit 
        if cv2.waitKey(25) & 0xFF == ord('q'): 
            break
       
      # Break the loop 
      else:  
        break
       
    # When everything done, release  
    # the video capture continents 
    cap.release() 


    
    
def which_button(button_press):
        call17(button_press)
        time.sleep(1)
        cv2.destroyAllWindows()
        
def display_continents(i):
        global frame_continents
        global element_continents
        global x1
        global y1
        element_continents = tk.Button(frame_continents, text = i, command = lambda m=i:which_button(m), bg='#F29062',font=('Cambria',20))
        element_continents.place(x = x1,y = y1,width=400)
#___________________________________________________________________________-       
#To run the levels of Game


def makeList(levelNo):
    level = levelNo
    global list_eng
    global level_words
    for i in list_eng:
        if level==1:
            if len(i)==1:
                level_words.append(i)
        elif level==2:
            if len(i)>1 and len(i)<=3:
                level_words.append(i)
        elif level==3:
            if len(i)>3 and len(i)<=5:
                level_words.append(i)
        elif level==4:
            if len(i)>5 and len(i)<=7:
                level_words.append(i)
        elif level==5:
            if len(i)>7:
                level_words.append(i)

                
def selectQ(level_words1):
    global windows50
    global Q
    vid = random.randint(0, (len(level_words1)-1))
    Q = level_words1[vid]
              
    
    
    
def call_game(I):
    global windows50
    global video
    video = tk.Label(windows50,bg='#FFBC8B')
    video.place(x = 610, y = 200) 
    #global end
    #end = timeit.default_timer()
    #print("time :", end-start)
    # Create a VideoCapture object and read from input file 
    cap = cv2.VideoCapture('videos/'+I+'.mp4') 
       
    # Check if camera opened successfully 
    if (cap.isOpened()== False):  
      tk.messagebox.showinfo("Video error!","Error opening video  file") 
       
    # Read until video is completed 
    while(cap.isOpened()): 
          
      # Capture frame-by-frame 
      ret, frame = cap.read() 
      #frame = imutils.resize(frame, width=270)
      
      cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
      img = Image.fromarray(cv2image)
      imgtk = ImageTk.PhotoImage(image=img)
      
      # if ret == True: 
       
      #   # Display the resulting frame
      #   cv2.moveWindow('Frame',750,160)
      #   cv2.imshow('Frame', frame) 
       
      #   # Press Q on keyboard to  exit 
      #   if cv2.waitKey(25) & 0xFF == ord('q'): 
      #      break
       
      # # Break the loop 
      # else:  
      #   break
       
      video.config(image=imgtk)

      windows50.update()
      time.sleep(0.02)
      
    
    # When everything done, release  
    # the video capture object 
    cap.release() 

def playVid():
    global windows50
    global Q
    global level_words
    selectQ(level_words)
    call_game(Q)

def displayQ():
    global windows50
    global playVid_btn
    playVid_btn = tk.Button(windows50, text = "Play the video", command = playVid, font=('Cambria',40),bg='#F29062')
    playVid_btn.place(x = 100, y = 250)
    
def accept_ans():
    global windows50
    global score
    global total
    global answer_ent
    global answer_btn
    global answer_lb
    global Q
    global answer
    global score2_lb
    global total2_lb
    global answerRight_lb
    
    total+=1
    answer = answer_ent.get().lower()
    ansCorrect_lb = tk.Label(windows50, text = "Correct Answer!",font=('Cambria',25),bg='#FFBC8B')
    ansWrong_lb = tk.Label(windows50, text = 'Incorrect Answer\nCorrect answer is :', font=('Cambria',14),bg='#FFBC8B')
    answerRight_lb = tk.Label(windows50, text = Q, font=('Cambria',14),bg='#FFBC8B')
    if answer==Q:
        ansCorrect_lb.place(x = 975, y = 400, width = 300)
        score+=1
    else:   
        ansWrong_lb.place(x = 975, y = 400, width = 300)
        answerRight_lb.place(x = 1205, y=422)
    score2_lb = tk.Label(windows50, text = score, font=('Cambria',35),bg='#FFBC8B')
    total2_lb = tk.Label(windows50, text = total, font=('Cambria',35),bg='#FFBC8B')
    score2_lb.place(x = 1250, y = 125)
    total2_lb.place(x = 1250, y = 175)
    
    
def enter_ans():
    global windows50
    global answer_btn
    global Q
    global answer_ent
    answer_lb = tk.Label(windows50, text = "Enter your Answer",font=('Cambria',14),bg='#FFBC8B')
    answer_lb.place(x = 975, y = 300)
    answer_ent = tk.Entry(windows50, width = 30,font=('Cambria',14))
    answer_ent.place(x=975, y=360)
    answer_btn = tk.Button(windows50, text = "Enter", font=('Cambria',14), command=accept_ans,bg='#F29062')
    answer_btn.place(x = 1250, y = 354)


def next_func():
    global windows50
    global video
    global answer_ent
    answer_ent.delete('0','end')
    cv2.destroyAllWindows()
    video.destroy()
    clear_lb = tk.Label(windows50, font=('Cambria',30),bg='#FFBC8B')
    clear_lb.place(x = 975, y = 400, width = 300)

    
    
def display_next():
    global windows50
    global next_btn
    next_btn = tk.Button(windows50, text = "Next Question", font=('Cambria',16), command=next_func,bg='#F29062')
    next_btn.place(x = 975, y = 500)

def playAgain_func():
    global windows50
    global Q
    call_game(Q)
    
def playAgain():
    global windows50
    global playAgain_btn
    playAgain_btn = tk.Button(windows50, text = "Play Again", command = playAgain_func, font=('Cambria',40),bg='#F29062')
    playAgain_btn.place(x = 100, y = 450)
    
def quit_func():
    global windows50
    windows50.destroy()
    
def display_quit():
    global windows50
    global quit_btn
    quit_btn = tk.Button(windows50, text = "Quit", command = quit_func, font=('Cambria',16),bg='#F29062')
    quit_btn.place(x = 1150, y = 500)

def gameRun(j):
    global windows50
    windows50=tk.Tk()
    windows50.title('Level 1')
    windows50.geometry('1250x700')
    windows50.configure(bg='#FFBC8B')
    windows50.iconbitmap('D:/Reliance school/Computer project/Danieledesantis-Audio-Video-Outline-Play.ico')


    global total
    global score
    score = 0
    total = 0
     
    global title_lb
    global title2_lb
    title_lb = tk.Label(windows50, text = "It's Game Time", font=('Gabriola',68,'bold'),bg='#FFBC8B')
    title_lb.place(x = 15, y = 20)
    title2_lb = tk.Label(windows50, text = "Test your knowledge of Indian Sign Language", font=('Cambria',12,'italic'),bg='#FFBC8B')
    title2_lb.place(x = 135, y = 135)
    
    global letter_eng
    global list_eng
    list_eng= ["build", 'built','building', 'builds', 'easily','easy','grew','grow','growth','growing','grows','like','likes','liked','liking','object','objects','our','ours','us','power','powers','powerful','them','themselves','those','these', 'thing','things','how','hey','best','everyone','mobile','mobiles','what','when','where','which','who','why', "above", "absent", "across", "add", 'added','adding','adds',"address",'addresses', "advance", 'advanced','advances','advancing','advancement',"africa", "after", 'afterwards',"afternoon", "age",'aged','aging', 'ages',"air", "airport",'airports', "all", "ambulance",'ambulances', "among", 'amongst',"angry",'anger', "animal",'animals', "antartica", "apple",'apples', "april", "area", 'areas',"arm",'arms', "asia", "ask", 'asks','asked','asking',"august", "australia", "baby", 'babies',"back",'backwards', "bad", "badminton", "ball",'balls',"banana",'bananas', "bank", 'banking','banks',"bathroom",'bathrooms', "beat", 'beats', 'beating', "beautiful", 'beautifully', "behind", "bird", 'birds',"birthday", 'birthdays',"black", "blue", "boat", 'boating','boats',"book",'books', "born", 'birth', "boy",'boys', "brain", 'brains', "breeze", "bright", 'brighten', 'brightness', 'brightly', "brown", "buy", 'buys','buying','bought',"bye", 'goodbye',"call", 'calls','called','calling',"calm",'calming', "camera", 'cameras', "can", 'could', "cancel", 'cancelled', 'cancelling', "cap", 'caps', 'car', 'cars', "careless", 'carelessness', "carrot", 'carrots', "cash", 'money', "cat", 'cats', "chair", 'chairs', "change", 'changing', 'changed', 'changes', "chapter", 'chapters', "chicken", 'chickens', 'child', "children", "circle", 'circles', "clever", 'cleverness', 'cleverly', "clouds", 'cloud', "coffee", "cold", "college", 'colleges', "colour", 'colours', 'color', 'colors', 'colouring', 'coloured', "come",'comes', 'came', 'coming', "cone", 'cones', "continent", 'continents', "copy", 'copies', 'copied', 'copying', "cry", 'cries', 'cried', 'crying', "cube", 'cubes', 'cuboids', "cuboid", 'cylinders', "cylinder", "dance", 'dances', 'dancing', 'danced', "dark", "darkness", "date", "dates", "daughter","daughters", "day", "days", "deaf", "deafness", "december", "desk", "desks", "diabetes", "die", "dies", "died", "difficult", 'difficulty', "dinner", "dinners", "dirty", "doctor", "doctors", "document", "documents", "dog", "dogs", "dosa", "dosas", "doubt", "doubts", "doubtful", "earn", "earns", "earned", "earning", "earth", "east", "eat", "eats", "eating", "ate", "eaten", "echo", "echos", "echoed", "echoing", "eight", "elbow", "elbows", "email", "emails", "empty", "emptiness", "empties", "emptied", "emptying", "engineer", "engineers", "enjoy", "enjoying", "enjoys", "enjoyed", "europe", "evening", "evenings", "exam", "exams", "eye", "eyes", "face", "faces", "fail", "failing", "fails", "failed", "fall", "falling", "falls", "fell", "fallen", "false", "family", "families", "fat", "father", "father's","fathers", "fear", "fears", "feared", "fearful", "fearing", "february", "feel", "feeling", "feels", "felt", "film", "films", "fire", "fish", "fishes", "five", "floor", "floors", "four", "free", "frees", "freed", "friday", "friend", "friends", "fruit", "fruits", "game", "games", "gas", "gases", "gate", "gates", "girl", "girls", "glass", "glasses", "go", "going", "went", "gone", "goes", "goal", "goals", "goaling", 'goaled',"god", "gods", "golden", "good", "goodness", "grandfather", "grandfather's","grandfathers", "grandmother's","grandmother", "grandmothers", "grass", "green", "grey", "happy", "happiness",'happily', "he", "his", "hear", "hearing", "heard", "hears", "hello", "hi", "help", "helps", "helping", "helped", "hindi", "home", "homes", "hope", "hopes", "hopeful", "hoping", "hoped", "hot", "house", "houses", "husband", "husbands", "idli", "idlis", "in", "income", "incomes", "increase", "increasing", "increased", "increases", "india", "information", "insect", "insects", "interest", "interesting", "interested", "interests", "introduction", "intrductions", "jail", "jails", "january", "jeep", "jeeps", "july", "june", "lazy", "laziness", "lazily", "lemon", "lemons", "light", "lights", "lighting", "lighten", "lighted", "mango", "mangoes", "march", "me", "mix", "mixing", "mixed", "mixes", "monday", "month", "months", "monthly", "moon", "moons", "morning", "mornings", "mother","mother's", "mothers", "music", "musical", "musically", "my", "name", "names", "nice", "nicely", "night", "nights", "nine", "no", "not", "november", "october", "office", "offices", "one", "orange", "oranges", "pendulum", "pendulums", "phone", "phones", "pink", "please", "proud", "pride", "purple", "railway", "railways", "rain", "rains", "raining", "rained", "rainy", "rainbow", "rainbows", "rectangle", "rectangles", "red", "reflection", "reflections", "roti", "rotis", "sad", "sadness", "sadly", "sambhar", "saturday", "school", "schools", "september", "seven", "she", "her", "shop", "shops", "shopping", "shopped", "silver", "sister", "sisters", "six", "snow", "snowy", "snowing", "snowed", "snows", "son", "sons", "sorry", "sphere", "spheres", "square", "squares", "star", "stars", "starry", "strong", "strength", "study", "studies", "studying", "studied" , "summer", "summers", "sun", "sunday", "telephone", "telephones", "telescope", "telescopes", "thank", "thanks", "three", "thursday", "triangle", "triangles", "tuesday", "two", "wada", "wadas", "weather", "wednesday", "welcome", "welcomes", "welcoming", "welcomed", "white", "whitish", "wife", "wives", "wind", "winds", "windy", "winter", "winters", "work", "world", "x-ray", "x-rays", "year", 'years', "yellow", "yes", "you", "your", "yours", "yourself", "yourselves", "zero", "zoo", "zoos", 'atmosphere', 'eclipse', "eclipses", 'environment', 'equator', 'expert', "experts", 'hardworking', 'lie', "lies", "lying", "lied", 'map', "maps", 'north', 'patience', 'patient','radio', "radios", 'record', "records", 'right', 'sound', "sounds", 'south', 'television', "televisions", 'tv', "tvs", 'trouble', "troubles", "troubled", "troubling", 'trust', "trusted", "trusting", "trusts", 'universe', 'west', 'wrong', 'confident', "confidence", 'intelligent', "intellegence", 'knowledge', 'busy', 'brave', "bravery", 'tea', 'milk', 'heart', "hearts", 'talk', 'speak','speaking','speaks','spoke',"talking", "talks", "talked", 'stand', "standing", "stands", "stood", 'smell', "smelling", "smells", "smelt", 'sleep', "sleeping", "sleeps", "slept", 'sit', "sits", "sat", "sitting", 'see','seen', "seeing", "saw", "sees", 'run', "running", "runs", "ran", 'pain', "paining", "pains", "pained", 'hair', "hairs", 'nose', "noses", 'concentrate', "concentrated", "concentrating", "concentrates", 'old', 'young', 'battery', "batteries", 'electronics', "electronic", 'sofa', "sofas", 'clock', "clocks", 'window', "windows", 'umbrella', "umbrellas",'towel', "towels", 'plate', "plates", 'spoon', "spoons", 'flower', "flowers", 'tree', "trees", 'common', 'wet', "wetness", 'wear', "wears", "wearing", "wore", "worn", 'wash', "washes", "washed", "washing", 'wait', "waiting", "waited", "waits", 'visit', "visits", "visiting", "visited", 'swim', "swims", "swimming", "swam", 'stop', "stops", "stopped", "stopping", 'start', "starts", "starting", "started", 'whistle', "whistling", "whistles", "whistled", 'tabla', "tablas", 'stage', "stages", 'guitar', "guitars", 'sing', "sings", "singing", "sang", 'sculpture', "sculptures", 'magic', "magical", "magically", 'flute', "flutes", 'entertainment', 'drum', "drums", 'doll', "dolls", 'cinema', "cinemas", 'balloon', "balloons", 'art', "first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "zeroth", "open", "opened", "opens", "opening",'reddish','orangish','greenish','greenery','bluish','blackish','yellowish','pinkish', 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', '1','2','3','4','5','6','7','8','9','0']
    #letterNum = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', '1','2','3','4','5','6','7','8','9','0']
    #print(len(list_eng))
    global level_words
    level_words = []
    global Q 
    Q = ""
    global score1_lb
    global total1_lb
    score1_lb = tk.Label(windows50, text = "Score:", font=('Cambria',35),bg='#FFBC8B')
    total1_lb = tk.Label(windows50, text = "Total Questions:", font=('Cambria',35),bg='#FFBC8B')
    score1_lb.place(x = 900, y = 125)
    total1_lb.place(x = 900, y = 175)
    global score2_lb
    global total2_lb
    score2_lb = tk.Label(windows50, text = score, font=('Cambria',35),bg='#FFBC8B')
    total2_lb = tk.Label(windows50, text = total, font=('Cambria',35),bg='#FFBC8B')
    score2_lb.place(x = 1250, y = 125)
    total2_lb.place(x = 1250, y = 175)
    
    
    if j=='level 1':
        makeList(1)
    elif j=='level 2':
        makeList(2)
    elif j=='level 3':
        makeList(3)
    elif j=='level 4':
        makeList(4)
    elif j=='level 5':
        makeList(5)
                   
    displayQ()
    display_next()
    playAgain()
    display_quit()
    enter_ans()










#_____________________________________________________________________________________________________________

#designing Sign lanuguage generator page
def english_gen():
    
    audio_nb.select(1) #opening Sign lanuguage generator tab
    #_______
    #window heading
    frame1=tk.Frame(English_tab,bg='#FFBC8B')
    frame1.place(x=0,y=10,width=1500,height=120)
    heading_lb1= tk.Label(frame1,fg='black',bg='#FFBC8B',text='IN',font=('Gabriola',65,))
    heading_lb1.place(x=480,y=5)
    heading_lb2= tk.Label(frame1,fg='black',bg='#FFBC8B',text='SIGN',font=('Gabriola',68,'bold'))
    heading_lb2.place(x=550,y=0)
    heading_lb3= tk.Label(frame1,fg='black',bg='#FFBC8B',text='IA',font=('Gabriola',65,))
    heading_lb3.place(x=700,y=5)
    #_________________
    #displaying menu bar
    frame2=tk.Frame(English_tab,bg='#5B524A')
    frame2.place(x=0,y=150,width=1500,height=50)
    homepage_btn=tk.Button(frame2,text='Homepage',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=homepage)
    homepage_btn.pack(side='left')
    English_btn=tk.Button(frame2,text='English Sign lanuguage generator',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=english_gen)
    English_btn.pack(side='left')
    Hindi_btn=tk.Button(frame2,text='Hindi Sign lanuguage generator',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=hindi_gen)
    Hindi_btn.pack(side='left')
    Dict_btn=tk.Button(frame2,text='Dictionary',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=dictionary)
    Dict_btn.pack(side='left')
    Game_btn=tk.Button(frame2,text='Game',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=game)
    Game_btn.pack(side='left')
    About_btn=tk.Button(frame2,text='About',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=about_page)
    About_btn.pack(side='left')
    Quit_btn=tk.Button(frame2,text='Quit',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=windestroy)
    Quit_btn.pack(side='left')
    #_________________
    #audio/text input form user either by typing in entry box or by using mic
    global eng_audio_ent
    global eng_audio_btn
    global english_pic1
    global english_pic2
    global english_pic3
    global frame3
    frame3=tk.Frame(English_tab,bg='#FFBC8B')
    frame3.place(x=650,y=220,width=570,height=125)
    input_audio_lb=tk.Label(frame3,text='Press on the mic button to enter audio\n(Please wait for 2 seconds before speaking into your mic)',bg='#FFBC8B',font=('Cambria',14,'bold'))
    input_audio_lb.place(x=10,y=10)
    
    eng_audio_ent=tk.Entry(frame3,font=16,borderwidth=1,relief='solid')
    eng_audio_ent.place(x=10,y=60,width=400,height=37)
    
    english_pic1=Image.open('images/mic1.png')
    english_pic2 = english_pic1.resize((35,35),Image.ANTIALIAS)
    english_pic3=ImageTk.PhotoImage(english_pic2)
    
    eng_audio_btn= tk.Button(frame3, image = english_pic3 ,command=receive_audio_eng, borderwidth = 0)
    eng_audio_btn.place(x=410,y=60)
    
    eng_submit = tk.Button(frame3, text = 'Submit',bg='#F29062',font=('Cambria',14),command = Submit_eng)
    eng_submit.place(x=460,y=60)
    #_______________
    #start displaying main words
    global list_eng
    global verbs
    global text
    global frame4
    global sentences
    global punctuation
    frame4=tk.Frame(English_tab,bg='#FFBC8B')
    frame4.place(x=60,y=220,width=550,height=400)
    list_eng= ["build", 'built','building', 'builds', 'easily','easy','grew','grow','growth','growing','grows','like','likes','liked','liking','object','objects','our','ours','us','power','powers','powerful','them','themselves','those','these', 'thing','things','1','2','3','4','5','6','7','8','9','0','how','hey','best','everyone','mobile','mobiles','what','when','where','which','who','why','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', "above", "absent", "across", "add", 'added','adding','adds',"address",'addresses', "advance", 'advanced','advances','advancing','advancement',"africa", "after", 'afterwards',"afternoon", "age",'aged','aging', 'ages',"air", "airport",'airports', "all", "ambulance",'ambulances', "among", 'amongst',"angry",'anger', "animal",'animals', "antartica", "apple",'apples', "april", "area", 'areas',"arm",'arms', "asia", "ask", 'asks','asked','asking',"august", "australia", "baby", 'babies',"back",'backwards', "bad", "badminton", "ball",'balls',"banana",'bananas', "bank", 'banking','banks',"bathroom",'bathrooms', "beat", 'beats', 'beating', "beautiful", 'beautifully', "behind", "bird", 'birds',"birthday", 'birthdays',"black", "blue", "boat", 'boating','boats',"book",'books', "born", 'birth', "boy",'boys', "brain", 'brains', "breeze", "bright", 'brighten', 'brightness', 'brightly', "brown", "buy", 'buys','buying','bought',"bye", 'goodbye',"call", 'calls','called','calling',"calm",'calming', "camera", 'cameras', "can", 'could', "cancel", 'cancelled', 'cancelling', "cap", 'caps', 'car', 'cars', "careless", 'carelessness', "carrot", 'carrots', "cash", 'money', "cat", 'cats', "chair", 'chairs', "change", 'changing', 'changed', 'changes', "chapter", 'chapters', "chicken", 'chickens', 'child', "children", "circle", 'circles', "clever", 'cleverness', 'cleverly', "clouds", 'cloud', "coffee", "cold", "college", 'colleges', "colour", 'colours', 'color', 'colors', 'colouring', 'coloured', "come",'comes', 'came', 'coming', "cone", 'cones', "continent", 'continents', "copy", 'copies', 'copied', 'copying', "cry", 'cries', 'cried', 'crying', "cube", 'cubes', 'cuboids', "cuboid", 'cylinders', "cylinder", "dance", 'dances', 'dancing', 'danced', "dark", "darkness", "date", "dates", "daughter","daughters", "day", "days", "deaf", "deafness", "december", "desk", "desks", "diabetes", "die", "dies", "died", "difficult", 'difficulty', "dinner", "dinners", "dirty", "doctor", "doctors", "document", "documents", "dog", "dogs", "dosa", "dosas", "doubt", "doubts", "doubtful", "earn", "earns", "earned", "earning", "earth", "east", "eat", "eats", "eating", "ate", "eaten", "echo", "echos", "echoed", "echoing", "eight", "elbow", "elbows", "email", "emails", "empty", "emptiness", "empties", "emptied", "emptying", "engineer", "engineers", "enjoy", "enjoying", "enjoys", "enjoyed", "europe", "evening", "evenings", "exam", "exams", "eye", "eyes", "face", "faces", "fail", "failing", "fails", "failed", "fall", "falling", "falls", "fell", "fallen", "false", "family", "families", "fat", "father", "father's","fathers", "fear", "fears", "feared", "fearful", "fearing", "february", "feel", "feeling", "feels", "felt", "film", "films", "fire", "fish", "fishes", "five", "floor", "floors", "four", "free", "frees", "freed", "friday", "friend", "friends", "fruit", "fruits", "game", "games", "gas", "gases", "gate", "gates", "girl", "girls", "glass", "glasses", "go", "going", "went", "gone", "goes", "goal", "goals", "goaling", 'goaled',"god", "gods", "golden", "good", "goodness", "grandfather", "grandfather's","grandfathers", "grandmother's","grandmother", "grandmothers", "grass", "green", "grey", "happy", "happiness",'happily', "he", "his", "hear", "hearing", "heard", "hears", "hello", "hi", "help", "helps", "helping", "helped", "hindi", "home", "homes", "hope", "hopes", "hopeful", "hoping", "hoped", "hot", "house", "houses", "husband", "husbands", "idli", "idlis", "in", "income", "incomes", "increase", "increasing", "increased", "increases", "india", "information", "insect", "insects", "interest", "interesting", "interested", "interests", "introduction", "intrductions", "jail", "jails", "january", "jeep", "jeeps", "july", "june", "lazy", "laziness", "lazily", "lemon", "lemons", "light", "lights", "lighting", "lighten", "lighted", "mango", "mangoes", "march", "me", "mix", "mixing", "mixed", "mixes", "monday", "month", "months", "monthly", "moon", "moons", "morning", "mornings", "mother","mother's", "mothers", "music", "musical", "musically", "my", "name", "names", "nice", "nicely", "night", "nights", "nine", "no", "not", "november", "october", "office", "offices", "one", "orange", "oranges", "pendulum", "pendulums", "phone", "phones", "pink", "please", "proud", "pride", "purple", "railway", "railways", "rain", "rains", "raining", "rained", "rainy", "rainbow", "rainbows", "rectangle", "rectangles", "red", "reflection", "reflections", "roti", "rotis", "sad", "sadness", "sadly", "sambhar", "saturday", "school", "schools", "september", "seven", "she", "her", "shop", "shops", "shopping", "shopped", "silver", "sister", "sisters", "six", "snow", "snowy", "snowing", "snowed", "snows", "son", "sons", "sorry", "sphere", "spheres", "square", "squares", "star", "stars", "starry", "strong", "strength", "study", "studies", "studying", "studied" , "summer", "summers", "sun", "sunday", "telephone", "telephones", "telescope", "telescopes", "thank", "thanks", "three", "thursday", "triangle", "triangles", "tuesday", "two", "wada", "wadas", "weather", "wednesday", "welcome", "welcomes", "welcoming", "welcomed", "white", "whitish", "wife", "wives", "wind", "winds", "windy", "winter", "winters", "work", "world", "x-ray", "x-rays", "year", 'years', "yellow", "yes", "you", "your", "yours", "yourself", "yourselves", "zero", "zoo", "zoos", 'atmosphere', 'eclipse', "eclipses", 'environment', 'equator', 'expert', "experts", 'hardworking', 'lie', "lies", "lying", "lied", 'map', "maps", 'north', 'patience', 'patient','radio', "radios", 'record', "records", 'right', 'sound', "sounds", 'south', 'television', "televisions", 'tv', "tvs", 'trouble', "troubles", "troubled", "troubling", 'trust', "trusted", "trusting", "trusts", 'universe', 'west', 'wrong', 'confident', "confidence", 'intelligent', "intellegence", 'knowledge', 'busy', 'brave', "bravery", 'tea', 'milk', 'heart', "hearts", 'talk', 'speak','speaking','speaks','spoke',"talking", "talks", "talked", 'stand', "standing", "stands", "stood", 'smell', "smelling", "smells", "smelt", 'sleep', "sleeping", "sleeps", "slept", 'sit', "sits", "sat", "sitting", 'see','seen', "seeing", "saw", "sees", 'run', "running", "runs", "ran", 'pain', "paining", "pains", "pained", 'hair', "hairs", 'nose', "noses", 'concentrate', "concentrated", "concentrating", "concentrates", 'old', 'young', 'battery', "batteries", 'electronics', "electronic", 'sofa', "sofas", 'clock', "clocks", 'window', "windows", 'umbrella', "umbrellas",'towel', "towels", 'plate', "plates", 'spoon', "spoons", 'flower', "flowers", 'tree', "trees", 'common', 'wet', "wetness", 'wear', "wears", "wearing", "wore", "worn", 'wash', "washes", "washed", "washing", 'wait', "waiting", "waited", "waits", 'visit', "visits", "visiting", "visited", 'swim', "swims", "swimming", "swam", 'stop', "stops", "stopped", "stopping", 'start', "starts", "starting", "started", 'whistle', "whistling", "whistles", "whistled", 'tabla', "tablas", 'stage', "stages", 'guitar', "guitars", 'sing', "sings", "singing", "sang", 'sculpture', "sculptures", 'magic', "magical", "magically", 'flute', "flutes", 'entertainment', 'drum', "drums", 'doll', "dolls", 'cinema', "cinemas", 'balloon', "balloons", 'art', "first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "zeroth", "open", "opened", "opens", "opening",'reddish','orangish','greenish','greenery','bluish','blackish','yellowish','pinkish']    
    sentences = ['how are you','what is your name', 'i am fine', 'you are wrong', 'where is the police station', 'where is the hospital', 'where is the bathroom', 'where is the restroom', 'where is the washroom', 'where do you stay', "where do you live", 'when will we go', 'what is your moblie number', "what is your phone number", 'what is your job', 'what is your age', "how old are you", 'what date is it today', 'what is the problem', 'what are you doing', 'wait i am thinking', 'that is good', 'take care', 'stand up', 'sit down', 'shall i help you', 'can i help you', 'please call me later', 'please call an ambulance', "please call the ambulance", 'open the door', "open the doors", 'no smoking please', 'nice to meet you', 'let us go for lunch', 'keep quite', 'i have headache', 'i do not understand anything', 'i am tired', 'i am thinking', 'i am sorry', 'happy journey', 'good question', 'do not worry', 'be careful', 'are you sick', 'are you hungry', 'are you busy', 'all the best']
    verbs=['the','an','is','are','was','were','will','am','be','being','been','has','have','had','having','do','does','did', "may", "might", "must", "ought", "shall","should", 'would','to','and','or','on','of']
    punctuation=['!','@','#','$','%','^','&','*','(',')','_','-','+','=','~','`','{','[','}',']', '\\','|', ':',';', '"' , "'", ',' , '<', '.', '>' , '?', '/']
    lbl_display=tk.Label(frame4,text='The Main Words/Characters Are:',bg='#FFBC8B',font=('Cambria',20,'bold'))
    lbl_display.place(x=10,y=10)
#designing english_gen ends here
#_________________
#designing hindi sign language generator
def hindi_gen():
    audio_nb.select(2)  #opening Hindi tab
    #_________________
    #window heading
    frame1=tk.Frame(Hindi_tab,bg='#FFBC8B')
    frame1.place(x=0,y=10,width=1500,height=120)
    heading_lb1= tk.Label(frame1,fg='black',bg='#FFBC8B',text='IN',font=('Gabriola',65,))
    heading_lb1.place(x=480,y=5)
    heading_lb2= tk.Label(frame1,fg='black',bg='#FFBC8B',text='SIGN',font=('Gabriola',68,'bold'))
    heading_lb2.place(x=550,y=0)
    heading_lb3= tk.Label(frame1,fg='black',bg='#FFBC8B',text='IA',font=('Gabriola',65,))
    heading_lb3.place(x=700,y=5)
    #_______
    #displaying menu bar
    frame2=tk.Frame(Hindi_tab,bg='#5B524A')
    frame2.place(x=0,y=150,width=1500,height=50)
    homepage_btn=tk.Button(frame2,text='Homepage',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=homepage)
    homepage_btn.pack(side='left')
    English_btn=tk.Button(frame2,text='English Sign lanuguage generator',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=english_gen)
    English_btn.pack(side='left')
    Hindi_btn=tk.Button(frame2,text='Hindi Sign lanuguage generator',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=hindi_gen)
    Hindi_btn.pack(side='left')
    Dict_btn=tk.Button(frame2,text='Dictionary',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=dictionary)
    Dict_btn.pack(side='left')
    Game_btn=tk.Button(frame2,text='Game',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=game)
    Game_btn.pack(side='left')
    About_btn=tk.Button(frame2,text='About',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=about_page)
    About_btn.pack(side='left')
    Quit_btn=tk.Button(frame2,text='Quit',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=windestroy)
    Quit_btn.pack(side='left')
    #________
    #audio/text input form user either by typing in entry box or by using mic
    global hin_audio_ent
    global hin_audio_btn
    global hindi_pic1
    global hindi_pic2
    global hindi_pic3
    global frame3
    frame3=tk.Frame(Hindi_tab,bg='#FFBC8B')
    frame3.place(x=650,y=220,width=570,height=125)
    input_audio_lb=tk.Label(frame3,text='ऑडियो दर्ज करने के लिए माइक बटन पर दबाएँ  \n कृपया अपने माइक में बोलने से पहले 2  सेकंड प्रतीक्षा करें'      ,   bg='#FFBC8B',font=('Cambria',14,'bold'))
    input_audio_lb.place(x=10,y=10)
    
    hin_audio_ent=tk.Entry(frame3,font=16,borderwidth=1,relief='solid')
    hin_audio_ent.place(x=10,y=60,width=400,height=37)
    
    hindi_pic1=Image.open('images/mic1.png')
    hindi_pic2 = hindi_pic1.resize((35,35),Image.ANTIALIAS)
    hindi_pic3=ImageTk.PhotoImage(hindi_pic2)
    
    hin_audio_btn= tk.Button(frame3, image = hindi_pic3 ,command=receive_audio_hin, borderwidth = 0)
    hin_audio_btn.place(x=410,y=60)
    
    hin_submit = tk.Button(frame3, text = 'दर्ज करे',  bg='#F29062',font=('Cambria',14),command = Submit_hin)
    hin_submit.place(x=460,y=60)
    #_____________________
    global list_hin
    global punctuation
    global verbs
    global text
    global frame4
    global sentences
    frame4=tk.Frame(Hindi_tab,bg='#FFBC8B')
    frame4.place(x=60,y=220,width=550,height=400)
    list_hin=['०',  'शून्य', ' १', 'एक', '२', 'दो', '३', 'तीन', '४', 'चार', '५', 'पांच', '६', 'छह', '७', 'सात', '८',  'आठ', '९', 'नौ', 'मां', 'माता', 'मम्मी', 'मम्मा', 'माताश्री', 'पिता' , 'बाप', 'पिताजी', 'पापा'  ,'पिताश्री',    'अ'  ,  'आ'  ,   'इ'   ,  'ई' , 'उ'  , 'ऊ' , 'ए' , "ऐ", 'ओ' , 'औ' , "अं", "अः", 'ा' , 'ि' , 'ी' , 'ु' , 'ू' , 'े' , 'ै' , 'ो' , 'ौ' , 'ं' , 'ः'   , 'ृ' , "क", "ख", "ग", "घ", "ङ", "च", "छ", "ज", "झ", "ञ", "ट", "ठ", "ड", "ढ", "ण", "त", "थ", "द", "ध", "न", "प", "फ", "ब", "भ", "म", "य", "र", "ल", "व", "ह", "श", "ष", "स", "क्ष", "त्र", "ज्ञ", "अपना", "अपनी", "अपने", "अवकाश", "आप", "आपका", "आपको", "कक्षा", "कर", "करना", "करिये", "करे", "करो", "कहना", "किताब", "किताबें", "कुछ", "कृप्या", "कौन", "क्या", "खड़ा", "खड़े", "गणित", "चाहिए", "छुट्टी", "जगह", "जाइये", "जाओ", "तुम", "तुमको", "तुम्हारा", "दोस्त", "नमस्कार", "नाम", "निकले", "निकालना", "पंक्ति", "पठन", "पढ़ाना", "पढ़ाई", "परिवार", "पाठ", "पुस्तक", "पुस्तकें", "प्रार्थना", "पढ़ना", "बंद", "बही", "बैठ", "बैठा", "बैठिये", "बैठी", "बैठे", "बोलना", "भीड़", "मत", "मित्र", "में", "मेरा", "मैं", "राम", "रिहा", "रिहाई", "रेखा", "लाइन", "लिखा", "लिखना", "लिखे", "लिखो", "लेखन", "विज्ञान", "श्यामपट्ट", "सबको", "सहेली", "स्थान", "हिंदी", "हूं", "है", "हो" , "स्थानों" , "सहेलियां", "लाइने", "रेखाएं", "बोल", "मित्रों", "बैठना", "परिवारों", "पंक्तियां", "दोस्तों", "छुट्टियां", "छुट्टियों", "किताबी", "पढ़ता", "पढ़ती", "किताबों", "हैं", "पढ़ते"] 
    punctuation=['!','@','#','$','%','^','&','*','(',')','_','-','+','=','~','`','{','[','}',']', '\\','|', ':',';', '"' , "'", ',' , '<', '.', '>' , '?', '/']
    lbl_display=tk.Label(frame4,text='मुख्य शब्द / वर्ण हैं:'   ,    bg='#FFBC8B',font=('Cambria',20,'bold'))
    lbl_display.place(x=10,y=10)
#designing hindi_gen ends here
#_____________________
#_____________________
#designing about page
def about_page():
    audio_nb.select(4) #opening about page tab
    #______________________
    #window heading
    frame1=tk.Frame(About_tab,bg='#FFBC8B')
    frame1.place(x=0,y=10,width=1500,height=120)
    heading_lb1= tk.Label(frame1,fg='black',bg='#FFBC8B',text='IN',font=('Gabriola',65,))
    heading_lb1.place(x=480,y=5)
    heading_lb2= tk.Label(frame1,fg='black',bg='#FFBC8B',text='SIGN',font=('Gabriola',68,'bold'))
    heading_lb2.place(x=550,y=0)
    heading_lb3= tk.Label(frame1,fg='black',bg='#FFBC8B',text='IA',font=('Gabriola',65,))
    heading_lb3.place(x=700,y=5)
    #_________________
    #displaying menu bar
    frame2=tk.Frame(About_tab,bg='#5B524A')
    frame2.place(x=0,y=150,width=1500,height=50)
    homepage_btn=tk.Button(frame2,text='Homepage',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=homepage)
    homepage_btn.pack(side='left')
    English_btn=tk.Button(frame2,text='English Sign lanuguage generator',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=english_gen)
    English_btn.pack(side='left')
    Hindi_btn=tk.Button(frame2,text='Hindi Sign lanuguage generator',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=hindi_gen)
    Hindi_btn.pack(side='left')
    Dict_btn=tk.Button(frame2,text='Dictionary',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=dictionary)
    Dict_btn.pack(side='left')
    Game_btn=tk.Button(frame2,text='Game',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=game)
    Game_btn.pack(side='left')
    About_btn=tk.Button(frame2,text='About',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=about_page)
    About_btn.pack(side='left')
    Quit_btn=tk.Button(frame2,text='Quit',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=windestroy)
    Quit_btn.pack(side='left')
    #_________________
    info1='A sign language generator\nCan help make communication clear\nBecause sign language is the mother tongue\nFor those who have the inability to speak or hear'
    info2='             All humans being social animals wish to express their thoughts to each other.\n                                                   However, this task may become a bit challenging for the people who are hard of hearing or aphonic.\n                                                  Thus, this audio to sign language converter can convert audio to required visuals. These include the\ncombination of hand movements, arms or body and facial expressions.'
    info3='This program has been developed using Python programming language.\n                      In this program, the input may be given by speaking or typing. If audio input is given,\n                                       then the audio is converted to text using Google speech API. The main words from the text are \n     identified and the videos can be played by the user on the click of a button.'
    frame3=tk.Frame(About_tab,bg='#FFBC8B',width=1100,height=100)
    frame3.place(x=50,y=230)
    lbl_info1=tk.Label(frame3,bg='#FFBC8B',text=info1,font=('Cambria',14,'bold','italic'))
    lbl_info1.place(x=300,y=0)
    frame4=tk.Frame(About_tab,bg='#FFBC8B',width=500,height=100)
    frame4.place(x=0,y=350)
    lbl_info2=tk.Label(frame4,bg='#FFBC8B',text=info2,font=('Cambria',12))
    lbl_info2.pack()
    frame5=tk.Frame(About_tab,bg='#FFBC8B',width=1100,height=100)
    frame5.place(x=48,y=435)
    lbl_info3=tk.Label(frame5,bg='#FFBC8B',text=info3,font=('Cambria',12))
    lbl_info3.pack()
    #_______________
    
    global about_pic1
    global about_pic2
    
    frame4=tk.Frame(About_tab,bg='#FFBC8B',width=500,height=500)
    frame4.place(x=930,y=300)
    about_pic1=Image.open('E:/Python Programs/CS project/about.jpg')
    about_pic2=ImageTk.PhotoImage(about_pic1)
    lbl= tk.Label(frame4, image = about_pic2)
    lbl.place(x=0,y=0)
#designing about page ends here
#__________________
#_________________
#function for designing the homepage
def homepage():
    audio_nb.select(0)
    #__________________
    #window heading
    frame1=tk.Frame(Homepage_tab,bg='#FFBC8B')
    frame1.place(x=0,y=10,width=1500,height=120)
    heading_lb1= tk.Label(frame1,fg='black',bg='#FFBC8B',text='IN',font=('Gabriola',65,))
    heading_lb1.place(x=480,y=5)
    heading_lb2= tk.Label(frame1,fg='black',bg='#FFBC8B',text='SIGN',font=('Gabriola',68,'bold'))
    heading_lb2.place(x=550,y=0)
    heading_lb3= tk.Label(frame1,fg='black',bg='#FFBC8B',text='IA',font=('Gabriola',65,))
    heading_lb3.place(x=700,y=5)
    #_________________
    #displaying menu bar
    frame2=tk.Frame(Homepage_tab,bg='#5B524A')
    frame2.place(x=0,y=150,width=1500,height=50)
    homepage_btn=tk.Button(frame2,text='Homepage',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=homepage)
    homepage_btn.pack(side='left')
    English_btn=tk.Button(frame2,text='English Sign lanuguage generator',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=english_gen)
    English_btn.pack(side='left')
    Hindi_btn=tk.Button(frame2,text='Hindi Sign lanuguage generator',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=hindi_gen)
    Hindi_btn.pack(side='left')
    Dict_btn=tk.Button(frame2,text='Dictionary',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=dictionary)
    Dict_btn.pack(side='left')
    Game_btn=tk.Button(frame2,text='Game',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=game)
    Game_btn.pack(side='left')
    About_btn=tk.Button(frame2,text='About',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=about_page)
    About_btn.pack(side='left')
    Quit_btn=tk.Button(frame2,text='Quit',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=windestroy)
    Quit_btn.pack(side='left')
    #__________________
    #name accepting
    global name_ent
    global frame3
    global name_btn
    global c_homepage
    frame3=tk.Frame(Homepage_tab,bg='#FFBC8B')
    frame3.place(x=5,y=280,width=700,height=250)
    name_lb=tk.Label(frame3,bg='#FFBC8B',text="Enter Your Name:",font=('Cambria',14))
    name_lb.place(x=15,y=30)
    name_ent=tk.Entry(frame3,width=30,font=('Cambria',14))
    name_ent.place(x=175,y=28)
    name_btn=tk.Button(frame3,text='Enter',bg='#F29062',font=('Cambria',14),command=EnterName)
    
    #checking if the user is visiting the home page for the first time
    if c_homepage==0:
        c_homepage=1
        
    elif c_homepage==1 and user_name=='':
        pass   
    else:
        name_btn['state']=tk.DISABLED
        wlcm_lb=tk.Label(frame3,text='Welcome '+user_name+"!!!",font=('Cambria',20),bg='#FFBC8B')
        wlcm_lb.place(x=210,y=80)
        wlcm_lb2=tk.Label(frame3,text='Please check out the sign langauge generator tab...',font=('Cambria',20),bg='#FFBC8B')
        wlcm_lb2.place(x=60,y=130)
        name_ent.insert(0,user_name)
        name_ent['state']=tk.DISABLED
        
    name_btn.place(x=525,y=22) 
    #________________
    
    #side animation
    global homepage_pic1
    global homepage_pic2
    global homepage_pic3
    frame4=tk.Frame(Homepage_tab,highlightcolor='black',highlightbackground='black',highlightthickness=1)
    frame4.place(x=800,y=250,height=350,width=350)
    homepage_pic1 = Image.open('images/boy.png')
    homepage_pic2 = homepage_pic1.resize ((300,375), Image.ANTIALIAS)
    homepage_pic3 = ImageTk.PhotoImage(homepage_pic2)
    pic_lb = tk.Label(frame4, image = homepage_pic3)
    pic_lb.pack()
    #________________
    
    #designing homepage ends here
#___________________________________________________________________________________________________
#designing Dictionary
def dictionary():
    audio_nb.select(3)
    #___________________________________________________________________________________________________________
    #window heading
    frame1=tk.Frame(Dict_tab,bg='#FFBC8B')
    frame1.place(x=0,y=10,width=1500,height=120)
    heading_lb1= tk.Label(frame1,fg='black',bg='#FFBC8B',text='IN',font=('Gabriola',65,))
    heading_lb1.place(x=480,y=5)
    heading_lb2= tk.Label(frame1,fg='black',bg='#FFBC8B',text='SIGN',font=('Gabriola',68,'bold'))
    heading_lb2.place(x=550,y=0)
    heading_lb3= tk.Label(frame1,fg='black',bg='#FFBC8B',text='IA',font=('Gabriola',65,))
    heading_lb3.place(x=700,y=5)
    #______________________________________________________________________________________________________________
    #displaying menu bar
    frame2=tk.Frame(Dict_tab,bg='#5B524A')
    frame2.place(x=0,y=150,width=1500,height=50)
    homepage_btn=tk.Button(frame2,text='Homepage',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=homepage)
    homepage_btn.pack(side='left')
    English_btn=tk.Button(frame2,text='English Sign lanuguage generator',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=english_gen)
    English_btn.pack(side='left')
    Hindi_btn=tk.Button(frame2,text='Hindi Sign lanuguage generator',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=hindi_gen)
    Hindi_btn.pack(side='left')
    Dict_btn=tk.Button(frame2,text='Dictionary',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=dictionary)
    Dict_btn.pack(side='left')
    Game_btn=tk.Button(frame2,text='Game',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=game)
    Game_btn.pack(side='left')
    About_btn=tk.Button(frame2,text='About',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=about_page)
    About_btn.pack(side='left')
    Quit_btn=tk.Button(frame2,text='Quit',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=windestroy)
    Quit_btn.pack(side='left')
    #___________________________________________________________________________________________________________
    #place buttons for alphabets,words,etc.
    frame3=tk.Frame(Dict_tab,bg="#FFBC8B")
    frame3.place(x=0,y=220,width=1400,height=450)
    
    Alphabet_btn=tk.Button(frame3,text='Alphabets',bg='#F29062',font=('Cambria',20),command=alphabets)
    Alphabet_btn.place(x=10,y=10)
    Nature_btn=tk.Button(frame3,text='Nature',bg='#F29062',font=('Cambria',20),command=nature)
    Nature_btn.place(x=160,y=10)
    Numbers_btn=tk.Button(frame3,text='Numbers',bg='#F29062',font=('Cambria',20),command=numbers)
    Numbers_btn.place(x=280,y=10)
    Music_btn=tk.Button(frame3,text='Music',bg='#F29062',font=('Cambria',20),command=music)
    Music_btn.place(x=420,y=10)
    Sports_btn=tk.Button(frame3,text='Sports',bg='#F29062',font=('Cambria',20),command=sports)
    Sports_btn.place(x=525,y=10)
    Colours_btn=tk.Button(frame3,text='Colours',bg='#F29062',font=('Cambria',20),command=colours)
    Colours_btn.place(x=630,y=10)
    action_btn=tk.Button(frame3,text='Action',bg='#F29062',font=('Cambria',20),command=action)
    action_btn.place(x=750,y=10) 
    question_btn=tk.Button(frame3,text='Question',bg='#F29062',font=('Cambria',20),command=question)
    question_btn.place(x=860,y=10)  
    art_btn=tk.Button(frame3,text='Art and Entertainment',bg='#F29062',font=('Cambria',20),command=art)
    art_btn.place(x=10,y=80)
    object_btn=tk.Button(frame3,text='Objects',bg='#F29062',font=('Cambria',20),command=object)
    object_btn.place(x=1000,y=10)
    adjective_btn=tk.Button(frame3,text='Adjectives',bg='#F29062',font=('Cambria',20),command=adjective)
    adjective_btn.place(x=310,y=80)
    body_btn=tk.Button(frame3,text='Body Parts',bg='#F29062',font=('Cambria',20),command=body)
    body_btn.place(x=470,y=80)   
    emotion_btn=tk.Button(frame3,text='Emotions',bg='#F29062',font=('Cambria',20),command=emotion)
    emotion_btn.place(x=640,y=80)
    food_btn=tk.Button(frame3,text='Foods',bg='#F29062',font=('Cambria',20),command=food)
    food_btn.place(x=790,y=80)
    times_btn=tk.Button(frame3,text='Time',bg='#F29062',font=('Cambria',20),command=times)
    times_btn.place(x=900,y=80)
    geography_btn=tk.Button(frame3,text='Geopraphy',bg='#F29062',font=('Cambria',20),command=geography)
    geography_btn.place(x=1000,y=80)
    continents_btn=tk.Button(frame3,text='Continents',bg='#F29062',font=('Cambria',20),command=continents)
    continents_btn.place(x=10,y=150)
    
    #_____________________________________________________________________________________________________________
#designing Dictionary ends here
#___________________________________________________________________________________________________________________
#designing Game
def game():
    audio_nb.select(4)
    #___________________________________________________________________________________________________________
    #window heading
    frame1=tk.Frame(Game_tab,bg='#FFBC8B')
    frame1.place(x=0,y=10,width=1500,height=120)
    heading_lb1= tk.Label(frame1,fg='black',bg='#FFBC8B',text='IN',font=('Gabriola',65,))
    heading_lb1.place(x=480,y=5)
    heading_lb2= tk.Label(frame1,fg='black',bg='#FFBC8B',text='SIGN',font=('Gabriola',68,'bold'))
    heading_lb2.place(x=550,y=0)
    heading_lb3= tk.Label(frame1,fg='black',bg='#FFBC8B',text='IA',font=('Gabriola',65,))
    heading_lb3.place(x=700,y=5)
    #______________________________________________________________________________________________________________
    #displaying menu bar
    frame2=tk.Frame(Game_tab,bg='#5B524A')
    frame2.place(x=0,y=150,width=1500,height=50)
    homepage_btn=tk.Button(frame2,text='Homepage',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=homepage)
    homepage_btn.pack(side='left')
    English_btn=tk.Button(frame2,text='English Sign lanuguage generator',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=english_gen)
    English_btn.pack(side='left')
    Hindi_btn=tk.Button(frame2,text='Hindi Sign lanuguage generator',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=hindi_gen)
    Hindi_btn.pack(side='left')
    Dict_btn=tk.Button(frame2,text='Dictionary',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=dictionary)
    Dict_btn.pack(side='left')
    Game_btn=tk.Button(frame2,text='Game',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=game)
    Game_btn.pack(side='left')
    About_btn=tk.Button(frame2,text='About',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=about_page)
    About_btn.pack(side='left')
    Quit_btn=tk.Button(frame2,text='Quit',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=windestroy)
    Quit_btn.pack(side='left')
    #______________________________________________________________________________________________________________
    #Making buttons for Levels
    frame3=tk.Frame(Game_tab,bg="#FFBC8B")
    frame3.place(x=0,y=220,width=1400,height=450)
    level1_btn = tk.Button(frame3,text='Level 1',bg='#F29062',font=('Cambria',20),command=lambda m="level 1":gameRun(m))
    level1_btn.pack()
    level2_btn = tk.Button(frame3,text='Level 2',bg='#F29062',font=('Cambria',20),command=lambda m="level 2":gameRun(m))
    level2_btn.pack()
    level3_btn = tk.Button(frame3,text='Level 3',bg='#F29062',font=('Cambria',20),command=lambda m="level 3":gameRun(m))
    level3_btn.pack()
    level4_btn = tk.Button(frame3,text='Level 4',bg='#F29062',font=('Cambria',20),command=lambda m="level 4":gameRun(m))
    level4_btn.pack()
    level5_btn = tk.Button(frame3,text='Level 5',bg='#F29062',font=('Cambria',20),command=lambda m="level 5":gameRun(m))
    level5_btn.pack()











#_________________
#creating tk notebook with tabs to switch between pages
audio_nb=ttk.Notebook(window1)
audio_nb.pack(fill='both',expand=1)

Homepage_tab = tk.Frame(audio_nb,width=1250,height=750,bg='#FFBC8B')
English_tab = tk.Frame(audio_nb,width=1250,height=750,bg='#FFBC8B')
Hindi_tab = tk.Frame(audio_nb,width=1250,height=750,bg='#FFBC8B')
About_tab = tk.Frame(audio_nb,width=1250,height=750,bg='#FFBC8B')
Game_tab = tk.Frame(audio_nb,width=1250,height=750,bg='#FFBC8B')
Dict_tab = tk.Frame(audio_nb,width=1250,height=750,bg='#FFBC8B')



audio_nb.add (Homepage_tab , text="Homepage")
audio_nb.add (English_tab , text="English Sign lanuguage generator")
audio_nb.add (Hindi_tab, text='Hindi Sign Language generator')
audio_nb.add (Dict_tab,text="Dictionary")
audio_nb.add (Game_tab, text="Game")
audio_nb.add (About_tab , text="About")



audio_nb.hide(1)
audio_nb.hide(2)
audio_nb.hide(3)
audio_nb.hide(4)
audio_nb.hide(5)
#__________________
user_name=''  #for accepting the name of the user in the homepage
text=''
c1=0
c_homepage=0 #this c is used for keeping track whether the person is visiting the home page for the first time 
#this is because if the user is visitng the homepage for the second time after already inputing his name then that info should only be displayed

homepage() #the first page which should always open is home page


    

window1.mainloop()
