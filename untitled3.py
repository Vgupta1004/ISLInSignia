# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 00:16:12 2021

@author: shara
"""

import tkinter as tk
from tkinter import ttk
import cv2 
import numpy as np 
import time

 

window1 = tk.Tk();
window1.title('Sign Language Generator')
window1.geometry('1250x700')
#window1.iconbitmap('E:/Python Programs/CS project/Danieledesantis-Audio-Video-Outline-Play.ico')
 
global letter_eng
global list_eng
list_eng= ["build", 'built','building', 'builds', 'easily','easy','grew','grow','growth','growing','grows','like','likes','liked','liking','object','objects','our','ours','us','power','powers','powerful','them','themselves','those','these', 'thing','things','1','2','3','4','5','6','7','8','9','0','how','hey','best','everyone','mobile','mobiles','what','when','where','which','who','why', "above", "absent", "across", "add", 'added','adding','adds',"address",'addresses', "advance", 'advanced','advances','advancing','advancement',"africa", "after", 'afterwards',"afternoon", "age",'aged','aging', 'ages',"air", "airport",'airports', "all", "ambulance",'ambulances', "among", 'amongst',"angry",'anger', "animal",'animals', "antartica", "apple",'apples', "april", "area", 'areas',"arm",'arms', "asia", "ask", 'asks','asked','asking',"august", "australia", "baby", 'babies',"back",'backwards', "bad", "badminton", "ball",'balls',"banana",'bananas', "bank", 'banking','banks',"bathroom",'bathrooms', "beat", 'beats', 'beating', "beautiful", 'beautifully', "behind", "bird", 'birds',"birthday", 'birthdays',"black", "blue", "boat", 'boating','boats',"book",'books', "born", 'birth', "boy",'boys', "brain", 'brains', "breeze", "bright", 'brighten', 'brightness', 'brightly', "brown", "buy", 'buys','buying','bought',"bye", 'goodbye',"call", 'calls','called','calling',"calm",'calming', "camera", 'cameras', "can", 'could', "cancel", 'cancelled', 'cancelling', "cap", 'caps', 'car', 'cars', "careless", 'carelessness', "carrot", 'carrots', "cash", 'money', "cat", 'cats', "chair", 'chairs', "change", 'changing', 'changed', 'changes', "chapter", 'chapters', "chicken", 'chickens', 'child', "children", "circle", 'circles', "clever", 'cleverness', 'cleverly', "clouds", 'cloud', "coffee", "cold", "college", 'colleges', "colour", 'colours', 'color', 'colors', 'colouring', 'coloured', "come",'comes', 'came', 'coming', "cone", 'cones', "continent", 'continents', "copy", 'copies', 'copied', 'copying', "cry", 'cries', 'cried', 'crying', "cube", 'cubes', 'cuboids', "cuboid", 'cylinders', "cylinder", "dance", 'dances', 'dancing', 'danced', "dark", "darkness", "date", "dates", "daughter","daughters", "day", "days", "deaf", "deafness", "december", "desk", "desks", "diabetes", "die", "dies", "died", "difficult", 'difficulty', "dinner", "dinners", "dirty", "doctor", "doctors", "document", "documents", "dog", "dogs", "dosa", "dosas", "doubt", "doubts", "doubtful", "earn", "earns", "earned", "earning", "earth", "east", "eat", "eats", "eating", "ate", "eaten", "echo", "echos", "echoed", "echoing", "eight", "elbow", "elbows", "email", "emails", "empty", "emptiness", "empties", "emptied", "emptying", "engineer", "engineers", "enjoy", "enjoying", "enjoys", "enjoyed", "europe", "evening", "evenings", "exam", "exams", "eye", "eyes", "face", "faces", "fail", "failing", "fails", "failed", "fall", "falling", "falls", "fell", "fallen", "false", "family", "families", "fat", "father", "father's","fathers", "fear", "fears", "feared", "fearful", "fearing", "february", "feel", "feeling", "feels", "felt", "film", "films", "fire", "fish", "fishes", "five", "floor", "floors", "four", "free", "frees", "freed", "friday", "friend", "friends", "fruit", "fruits", "game", "games", "gas", "gases", "gate", "gates", "girl", "girls", "glass", "glasses", "go", "going", "went", "gone", "goes", "goal", "goals", "goaling", 'goaled',"god", "gods", "golden", "good", "goodness", "grandfather", "grandfather's","grandfathers", "grandmother's","grandmother", "grandmothers", "grass", "green", "grey", "happy", "happiness",'happily', "he", "his", "hear", "hearing", "heard", "hears", "hello", "hi", "help", "helps", "helping", "helped", "hindi", "home", "homes", "hope", "hopes", "hopeful", "hoping", "hoped", "hot", "house", "houses", "husband", "husbands", "idli", "idlis", "in", "income", "incomes", "increase", "increasing", "increased", "increases", "india", "information", "insect", "insects", "interest", "interesting", "interested", "interests", "introduction", "intrductions", "jail", "jails", "january", "jeep", "jeeps", "july", "june", "lazy", "laziness", "lazily", "lemon", "lemons", "light", "lights", "lighting", "lighten", "lighted", "mango", "mangoes", "march", "me", "mix", "mixing", "mixed", "mixes", "monday", "month", "months", "monthly", "moon", "moons", "morning", "mornings", "mother","mother's", "mothers", "music", "musical", "musically", "my", "name", "names", "nice", "nicely", "night", "nights", "nine", "no", "not", "november", "october", "office", "offices", "one", "orange", "oranges", "pendulum", "pendulums", "phone", "phones", "pink", "please", "proud", "pride", "purple", "railway", "railways", "rain", "rains", "raining", "rained", "rainy", "rainbow", "rainbows", "rectangle", "rectangles", "red", "reflection", "reflections", "roti", "rotis", "sad", "sadness", "sadly", "sambhar", "saturday", "school", "schools", "september", "seven", "she", "her", "shop", "shops", "shopping", "shopped", "silver", "sister", "sisters", "six", "snow", "snowy", "snowing", "snowed", "snows", "son", "sons", "sorry", "sphere", "spheres", "square", "squares", "star", "stars", "starry", "strong", "strength", "study", "studies", "studying", "studied" , "summer", "summers", "sun", "sunday", "telephone", "telephones", "telescope", "telescopes", "thank", "thanks", "three", "thursday", "triangle", "triangles", "tuesday", "two", "wada", "wadas", "weather", "wednesday", "welcome", "welcomes", "welcoming", "welcomed", "white", "whitish", "wife", "wives", "wind", "winds", "windy", "winter", "winters", "work", "world", "x-ray", "x-rays", "year", 'years', "yellow", "yes", "you", "your", "yours", "yourself", "yourselves", "zero", "zoo", "zoos", 'atmosphere', 'eclipse', "eclipses", 'environment', 'equator', 'expert', "experts", 'hardworking', 'lie', "lies", "lying", "lied", 'map', "maps", 'north', 'patience', 'patient','radio', "radios", 'record', "records", 'right', 'sound', "sounds", 'south', 'television', "televisions", 'tv', "tvs", 'trouble', "troubles", "troubled", "troubling", 'trust', "trusted", "trusting", "trusts", 'universe', 'west', 'wrong', 'confident', "confidence", 'intelligent', "intellegence", 'knowledge', 'busy', 'brave', "bravery", 'tea', 'milk', 'heart', "hearts", 'talk', 'speak','speaking','speaks','spoke',"talking", "talks", "talked", 'stand', "standing", "stands", "stood", 'smell', "smelling", "smells", "smelt", 'sleep', "sleeping", "sleeps", "slept", 'sit', "sits", "sat", "sitting", 'see','seen', "seeing", "saw", "sees", 'run', "running", "runs", "ran", 'pain', "paining", "pains", "pained", 'hair', "hairs", 'nose', "noses", 'concentrate', "concentrated", "concentrating", "concentrates", 'old', 'young', 'battery', "batteries", 'electronics', "electronic", 'sofa', "sofas", 'clock', "clocks", 'window', "windows", 'umbrella', "umbrellas",'towel', "towels", 'plate', "plates", 'spoon', "spoons", 'flower', "flowers", 'tree', "trees", 'common', 'wet', "wetness", 'wear', "wears", "wearing", "wore", "worn", 'wash', "washes", "washed", "washing", 'wait', "waiting", "waited", "waits", 'visit', "visits", "visiting", "visited", 'swim', "swims", "swimming", "swam", 'stop', "stops", "stopped", "stopping", 'start', "starts", "starting", "started", 'whistle', "whistling", "whistles", "whistled", 'tabla', "tablas", 'stage', "stages", 'guitar', "guitars", 'sing', "sings", "singing", "sang", 'sculpture', "sculptures", 'magic', "magical", "magically", 'flute', "flutes", 'entertainment', 'drum', "drums", 'doll', "dolls", 'cinema', "cinemas", 'balloon', "balloons", 'art', "first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "zeroth", "open", "opened", "opens", "opening",'reddish','orangish','greenish','greenery','bluish','blackish','yellowish','pinkish']
letter_eng = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print(len(list_eng))
 

def call(I):
    #global end
    #end = timeit.default_timer()
    #print("time :", end-start)
    # Create a VideoCapture object and read from input file 
    cap = cv2.VideoCapture('videos/'+I+'.mp4') 
       
    # Check if camera opened successfully 
    if (cap.isOpened()== False):  
      tk.messagebox.showinfo("Video error!","Error opening video  file") 
       
    # Read until video is completed 
    while(cap.isOpened()): 
          
      # Capture frame-by-frame 
      ret, frame = cap.read() 
      #frame = imutils.resize(frame, width=270)
      if ret == True: 
       
        # Display the resulting frame
        cv2.moveWindow('Frame',965,160)
        cv2.imshow('Frame', frame) 
       
        # Press Q on keyboard to  exit 
        if cv2.waitKey(25) & 0xFF == ord('q'): 
           break
       
      # Break the loop 
      else:  
        break
       
    # When everything done, release  
    # the video capture object 
    cap.release() 

global x
global y
x1 = 50
y1 = 15

def which_button(button_press):
    call(button_press)
    time.sleep(1)
    cv2.destroyAllWindows()
    
def display_btn(i):
    global element_btn
    element_btn = tk.Button(window1, text = i, command = lambda m=i:which_button(m), font=('Cambria',40),bg='#F29062')
    element_btn.place(x = x1,y = y1,width=100)

 

global c
global r
c = 0
r = 1

   
global i 
for i in letter_eng:
    c+=1
    display_btn(i)
    if c%6==0:
        r+=1
        y1+=130
        if r==5:
            x1 = 330
        else:
            x1 = 90
    else:
        x1+=120
        
window1.mainloop()