# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 13:20:39 2020

@author: shara
"""

import speech_recognition as sr

sample_rate = 48000
chunk_size = 2048
r = sr.Recognizer()



        
with sr.Microphone(sample_rate = sample_rate,  chunk_size = chunk_size) as source:
    r.adjust_for_ambient_noise(source) 
    print ("Say Something")
    audio = r.listen(source) 
          
    try: 
        text = r.recognize_google(audio,language='hi-IN') 
        print( "आपने कहा",  end=":")
        print(text)
        print(type(text))
        print(len(text))
        for i in text:
            print(i)
    except sr.UnknownValueError: 
        print("Google Speech Recognition could not understand audio") 
      
    except sr.RequestError as e: 
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        