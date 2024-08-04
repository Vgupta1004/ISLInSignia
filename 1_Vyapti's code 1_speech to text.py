# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 22:09:19 2020

@author: shara
"""
import speech_recognition as sr

sample_rate = 48000
chunk_size = 2048
r = sr.Recognizer()


        
with sr.Microphone(sample_rate = sample_rate,  chunk_size = chunk_size) as source:
    
    r.adjust_for_ambient_noise(source) #removing background noise
    print ("Say Something")
    audio = r.listen(source) 
          
    try:                                                               #if there is no error
        text = r.recognize_google(audio,language='hi-IN')              #default language is English
        #we can change the language to hindi by using the BCP 47 tag list
        print( "आपने कहा",  end=":")
        print(text)
        #every maatraa is a different character
        #हेलो has 4 chrs
        
    except sr.UnknownValueError: 
        print("Google Speech Recognition could not understand audio") 
      
    except sr.RequestError as e: 
        print("Could not request results from Google Speech Recognition service; {0}".format(e))