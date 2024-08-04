# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 20:38:06 2020

@author: shara
"""

from bs4 import BeautifulSoup as soup
from tkinter import *
import urllib.parse
from PIL import Image, ImageTk
import io

website = "http://www.porcys.com/review/"
openWebsite = soup(urllib.request.urlopen(website), 'html.parser')

reviews = openWebsite.find(name="section", attrs={'class': 'slider-content review'}).ul

results = []
for a in reviews(href=True):
    temp = "http://www.porcys.com"+a['href']
    results.append(temp)

mainWindow = Tk()
mainWindow.title("Latest Porcys reviews")

for i in range(0, 8):
    review = results[i]
    openReview = soup(urllib.request.urlopen(review), 'html.parser')
    rating = openReview.find(name="span", attrs={'class': 'rating'})
    album = openReview.find(name="div", attrs={'class': 'wrapper'}).i
    artist = openReview.find(name="div", attrs={'class': 'wrapper'}).h2
    coverWIP = openReview.find(name="img", attrs={'class': 'cover'})
    for tag in openReview.find_all('i'):
        tag.replaceWith(' ')
    print(artist.text)
    print(album.text)
    print(rating.text)
    cover = "http://www.porcys.com"+coverWIP['src']
    print(cover)
    artistAndAlbum = Label(font=("Helvetica",10), text=artist.text+'- '+album.text)
    artistAndAlbum.grid(row=i, column=100, sticky=W)
    ratingGUI = Label(font=("Helvetica",10), text=rating.text)
    ratingGUI.grid(row=i+1,columnspan=100)
    raw_data = urllib.request.urlopen(cover).read()
    im = Image.open(io.BytesIO(raw_data))
    image = ImageTk.PhotoImage(im)
    label1 = Label(mainWindow, image=image)
    label1.grid(row=i, sticky=W)
    
mainWindow.mainloop()