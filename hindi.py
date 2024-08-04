# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 14:57:29 2021

@author: shara
"""
#importing all modules required throughout program
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
import speech_recognition as sr
import cv2 
import numpy as np 
import time
from PyDictionary import PyDictionary

#video display
def call(I):
     
    # Create a VideoCapture object and read from input file 
    cap = cv2.VideoCapture('videos/'+I+'.mp4') 
       
    # Check if camera opened successfully 
    if (cap.isOpened()== False):  
      print("Video error!","Error opening video  file") 
       
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

#function for receiving audio in Sign lanuguage generator
def receive_audio():
       
    sample_rate = 48000
    chunk_size = 2048
    r = sr.Recognizer()
    
            
    with sr.Microphone(sample_rate = sample_rate,  chunk_size = chunk_size) as source:
        
        r.adjust_for_ambient_noise(source,duration=0.5)
        print('Speak now')
        audio = r.listen(source) 
              
        try:          
            global speak_text
            global text                                                     
            speak_text = r.recognize_google(audio, language='hi-IN')   
            speak_text = speak_text[0].upper()+speak_text[1:len(speak_text)]
            print(speak_text)
      
                                 
            
            
        except sr.UnknownValueError: 
            print('Input Error!!!',"Google Speech Recognition could not understand audio\nPlease enter again")
            #("Google Speech Recognition could not understand audio") 
      
        except sr.RequestError as e: 
           print("Input Error!!!","Could not request results from Google Speech Recognition service; {0}".format(e))    
           #print("Could not request results from Google Speech Recognition service; {0}".format(e))
           
receive_audio()          

print(speak_text.split())
a='मेरा'
if a in speak_text:
    call(a)
else:
    print('False')
    
for i in speak_text:
    print(i)