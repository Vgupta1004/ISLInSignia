# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 14:19:47 2021

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
list1=[]
c=0

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

def call(I):
              global video
              global delay
              global my_label
              
              print (I)
              vid='videos/Alphabets/'+ I.upper() +'.mp4'
              
              video = imageio.get_reader(vid)
              delay = int(1000 / video.get_meta_data()['fps'])
              my_label = Label(root,height=780,width=500)
              my_label.place(x=70,y=0)
              my_label.after(delay, lambda: stream(my_label))
              root.after(3000 ,my_label.destroy)
def myClick():
    global c
    i=list1[c]
    c+=1
    call(i)

root.geometry ('1250x2000') 

print('The letters are:') 
for i in ent:
    print(i)
    list1.append(i)
    
btn= Button(root,text='click me',command=myClick)
btn.pack()

root.mainloop()