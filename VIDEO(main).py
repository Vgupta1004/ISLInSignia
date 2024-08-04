# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 23:39:51 2020

@author: shara
"""

import imageio
from tkinter import *
from PIL import ImageTk, Image
from pathlib import Path
import time

root = Tk()
frame1=Frame(root)
video = imageio.get_reader('videos/Alphabets/A.mp4')
delay = int(2000 / video.get_meta_data()['fps'])

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

#if __name__ == '__main__':
 

root.geometry ('1250x750')  
my_label = Label(frame1,height=480,width=848)
my_label.place(x=10,y=0)
my_label.after(delay, lambda: stream(my_label))
root.after(40000 ,my_label.destroy)

root.mainloop()