# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 12:16:30 2021

@author: shara
"""
import imageio
from tkinter import *
from PIL import ImageTk, Image
from pathlib import Path
import time

root = Tk()


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
 
for i in range(1,11):
    print(i)
    root.geometry ('1250x750')  
    video = imageio.get_reader('videos/across.mp4')
    delay = int(1000 / video.get_meta_data()['fps'])
    my_label = Label(root,height=480,width=848)
    my_label.place(x=10,y=0)
    my_label.after(delay, lambda: stream(my_label))
    root.after(3000 ,my_label.destroy)

    root.mainloop()
    root.destroy()
    