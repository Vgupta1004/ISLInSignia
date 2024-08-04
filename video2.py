# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 13:36:20 2020

@author: shara
"""

import vlc
import pafy
import imageio
from tkinter import Tk, Label
from PIL import ImageTk, Image
from pathlib import Path
import os

os.add_dll_directory(r'E:\Python Programs\CS project\libvlc.dll')

url = "https://www.youtube.com/watch?v=A_wVyOCjHeM"
video = pafy.new(url)
best = video.getbest()
playurl = best.url

video = imageio.get_reader(playurl)
delay = int(1000 / video.get_meta_data()['fps'])
     
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

if __name__ == '__main__':
 
  root = Tk()
  my_label = Label(root)
  my_label.pack()
  my_label.after(delay, lambda: stream(my_label))
  root.mainloop()