# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 20:34:57 2020

@author: shara
"""

import speech_recognition as sr   #imports package SpeechRecogniton
import webbrowser  as wb          #imports package webbrowser
import pyaudio as py              #imprts package pyaudio

#creating three instances of class Recognizer

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()




with sr.Microphone() as source:
    print("[search edureka: search youtube]")
    print('speak now')
    audio = r1.listen(source)
    store=sr.Recognizer().recognize_google(audio)
    print(store)
        