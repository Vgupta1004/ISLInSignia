# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 22:35:53 2020

@author: shara
"""

import speech_recognition as sr            #import package SpeechRecognition

mic_name = "Microphone Array (Synaptics Aud"         #mic name of Sukriti lenovo 

mic_list = sr.Microphone.list_microphone_names()   #list_microphone_names() is used for printing the list of available mics on your device

for i, microphone_name in enumerate(mic_list):    
    
    '''
    enumerate helps to access both the index and the items of the list at the same time.
    first it accesses the index
    second it accesses the data item in the sequence
    so here i is storing the index whereas microphone_name is storing the items
    '''
    print(i)
    print(microphone_name)
    
   