# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 20:34:57 2020

@author: shara
"""

import speech_recognition as sr   #imports package SpeechRecogniton
import pyttsx3

# speech 
def SpeakText(command):    #converting text to speech
      
    # Initialize the engine 
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait() 


#creating an instance of class Recognizer
r1 = sr.Recognizer()

with sr.Microphone() as source:
    print('speak now')
    audio = r1.listen(source)
    store= r1.recognize_google(audio)
    print(store)
    SpeakText(store)
        