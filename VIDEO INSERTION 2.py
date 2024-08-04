# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 12:30:17 2021

@author: shara
"""

import imageio
from tkinter import *
from PIL import ImageTk, Image
from pathlib import Path
import time


ent=input()
list= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ent=ent.lower()
def stream(label):
    
    try:
        image = video.get_next_data()
    
    except:
        video.close()
        return
    label.after(delay, lambda: stream(label))
    frame_image = ImageTk.PhotoImage(Image.fromarray(image))
    label.config(image=frame_image)
    label.image = frame_image
    
    
def call(i):
    global video
    global delay
    root = Tk()
    root.geometry ('1250x2000')  
    print (i)
    vid='videos/Alphabets/'+ i.upper() +'.mp4'
    video = imageio.get_reader(vid)
    delay = int(1000 / video.get_meta_data()['fps'])
    my_label = Label(root,height=780,width=500)
    my_label.place(x=70,y=0)
    my_label.after(delay, lambda: stream(my_label))
    root.after(4000,my_label.destroy)
    #root.after(4000,root.destroy)
    
    time.sleep(1)
    
    return
   
for i in ent:
    call(i)
    
root.mainloop()