# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 18:18:09 2021

@author: shara
"""

import imageio
from tkinter import *
from PIL import ImageTk, Image
from pathlib import Path
import time

root = Tk()
ent=input()
list= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ent=ent.lower()
global delay
global video
global my_label

def stream(label):
  global video
  global delay
  try:
    image = video.get_next_data()
    
  except:
    video.close()
    return
  label.after(delay, lambda: stream(label))
  frame_image = ImageTk.PhotoImage(Image.fromarray(image))
  label.config(image=frame_image)
  label.image = frame_image
  
def call(X):
              global video
              global delay
              global my_label
             
              global ent
              
              if X < len(ent):
                  print (ent[X])
                  vid='videos/Alphabets/'+ ent[X].upper() +'.mp4'
                  video = imageio.get_reader(vid)
                  delay = int(1000 / video.get_meta_data()['fps'])
                  my_label = Label(root,height=780,width=500)
                  my_label.place(x=70,y=0)
                  my_label.after(delay, lambda: stream(my_label))
                  X=X+1
                  root.after(3000 ,call(X))
              
root.geometry ('1250x2000') 
#for x in range(0,len(ent)):
x=0
call(x)
    
root.mainloop()