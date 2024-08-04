# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 21:44:02 2020

@author: shara
"""

import speech_recognition as sr             #importing package SpeechRecognition to recognise what is being saud

import playsound                             #importing package playsound to play audio

r1 = sr.Recognizer()         #Recognizer class ; r1 is object of class Recognizer


#AudioFile is a function to read audio file
#give path of audio file
#file CANNOT be mp3 

file = sr.AudioFile('C:\\Users\\shara\\Music\\preamble.wav')  

with file as source:        #we are taking audio from file
    audio=r1.record(source)       #we are storing the audio in auido format in variable audio
                                  #record function is used to take audio from source ; here source is file
                                  
                                  
    
print(r1.recognize_google(audio))        #use google speech api to convert audio to text

playsound.playsound('C:\\Users\\shara\\Music\\preamble.wav')   #play the audio file 
