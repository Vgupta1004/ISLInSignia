# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 14:42:14 2021

@author: Vyapti
"""

from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import cv2 
import numpy as np 
import time
import random
#import imutils

window2 = tk.Tk();
window2.title('Sign Language Generator')
window2.geometry('1250x700')
window2.configure(bg='#FFBC8B')
window2.iconbitmap('D:/Reliance school/Computer project/Danieledesantis-Audio-Video-Outline-Play.ico')
 
global total
global score
score = 0
total = 0
 
global title_lb
global title2_lb
title_lb = tk.Label(window2, text = "It's Game Time", font=('Gabriola',68,'bold'),bg='#FFBC8B')
title_lb.place(x = 15, y = 20)
title2_lb = tk.Label(window2, text = "Test your knowledge of Indian Sign Language", font=('Cambria',12,'italic'),bg='#FFBC8B')
title2_lb.place(x = 135, y = 135)

global letter_eng
global list_eng
list_eng= ["build", 'built','building', 'builds', 'easily','easy','grew','grow','growth','growing','grows','like','likes','liked','liking','object','objects','our','ours','us','power','powers','powerful','them','themselves','those','these', 'thing','things','how','hey','best','everyone','mobile','mobiles','what','when','where','which','who','why', "above", "absent", "across", "add", 'added','adding','adds',"address",'addresses', "advance", 'advanced','advances','advancing','advancement',"africa", "after", 'afterwards',"afternoon", "age",'aged','aging', 'ages',"air", "airport",'airports', "all", "ambulance",'ambulances', "among", 'amongst',"angry",'anger', "animal",'animals', "antartica", "apple",'apples', "april", "area", 'areas',"arm",'arms', "asia", "ask", 'asks','asked','asking',"august", "australia", "baby", 'babies',"back",'backwards', "bad", "badminton", "ball",'balls',"banana",'bananas', "bank", 'banking','banks',"bathroom",'bathrooms', "beat", 'beats', 'beating', "beautiful", 'beautifully', "behind", "bird", 'birds',"birthday", 'birthdays',"black", "blue", "boat", 'boating','boats',"book",'books', "born", 'birth', "boy",'boys', "brain", 'brains', "breeze", "bright", 'brighten', 'brightness', 'brightly', "brown", "buy", 'buys','buying','bought',"bye", 'goodbye',"call", 'calls','called','calling',"calm",'calming', "camera", 'cameras', "can", 'could', "cancel", 'cancelled', 'cancelling', "cap", 'caps', 'car', 'cars', "careless", 'carelessness', "carrot", 'carrots', "cash", 'money', "cat", 'cats', "chair", 'chairs', "change", 'changing', 'changed', 'changes', "chapter", 'chapters', "chicken", 'chickens', 'child', "children", "circle", 'circles', "clever", 'cleverness', 'cleverly', "clouds", 'cloud', "coffee", "cold", "college", 'colleges', "colour", 'colours', 'color', 'colors', 'colouring', 'coloured', "come",'comes', 'came', 'coming', "cone", 'cones', "continent", 'continents', "copy", 'copies', 'copied', 'copying', "cry", 'cries', 'cried', 'crying', "cube", 'cubes', 'cuboids', "cuboid", 'cylinders', "cylinder", "dance", 'dances', 'dancing', 'danced', "dark", "darkness", "date", "dates", "daughter","daughters", "day", "days", "deaf", "deafness", "december", "desk", "desks", "diabetes", "die", "dies", "died", "difficult", 'difficulty', "dinner", "dinners", "dirty", "doctor", "doctors", "document", "documents", "dog", "dogs", "dosa", "dosas", "doubt", "doubts", "doubtful", "earn", "earns", "earned", "earning", "earth", "east", "eat", "eats", "eating", "ate", "eaten", "echo", "echos", "echoed", "echoing", "eight", "elbow", "elbows", "email", "emails", "empty", "emptiness", "empties", "emptied", "emptying", "engineer", "engineers", "enjoy", "enjoying", "enjoys", "enjoyed", "europe", "evening", "evenings", "exam", "exams", "eye", "eyes", "face", "faces", "fail", "failing", "fails", "failed", "fall", "falling", "falls", "fell", "fallen", "false", "family", "families", "fat", "father", "father's","fathers", "fear", "fears", "feared", "fearful", "fearing", "february", "feel", "feeling", "feels", "felt", "film", "films", "fire", "fish", "fishes", "five", "floor", "floors", "four", "free", "frees", "freed", "friday", "friend", "friends", "fruit", "fruits", "game", "games", "gas", "gases", "gate", "gates", "girl", "girls", "glass", "glasses", "go", "going", "went", "gone", "goes", "goal", "goals", "goaling", 'goaled',"god", "gods", "golden", "good", "goodness", "grandfather", "grandfather's","grandfathers", "grandmother's","grandmother", "grandmothers", "grass", "green", "grey", "happy", "happiness",'happily', "he", "his", "hear", "hearing", "heard", "hears", "hello", "hi", "help", "helps", "helping", "helped", "hindi", "home", "homes", "hope", "hopes", "hopeful", "hoping", "hoped", "hot", "house", "houses", "husband", "husbands", "idli", "idlis", "in", "income", "incomes", "increase", "increasing", "increased", "increases", "india", "information", "insect", "insects", "interest", "interesting", "interested", "interests", "introduction", "intrductions", "jail", "jails", "january", "jeep", "jeeps", "july", "june", "lazy", "laziness", "lazily", "lemon", "lemons", "light", "lights", "lighting", "lighten", "lighted", "mango", "mangoes", "march", "me", "mix", "mixing", "mixed", "mixes", "monday", "month", "months", "monthly", "moon", "moons", "morning", "mornings", "mother","mother's", "mothers", "music", "musical", "musically", "my", "name", "names", "nice", "nicely", "night", "nights", "nine", "no", "not", "november", "october", "office", "offices", "one", "orange", "oranges", "pendulum", "pendulums", "phone", "phones", "pink", "please", "proud", "pride", "purple", "railway", "railways", "rain", "rains", "raining", "rained", "rainy", "rainbow", "rainbows", "rectangle", "rectangles", "red", "reflection", "reflections", "roti", "rotis", "sad", "sadness", "sadly", "sambhar", "saturday", "school", "schools", "september", "seven", "she", "her", "shop", "shops", "shopping", "shopped", "silver", "sister", "sisters", "six", "snow", "snowy", "snowing", "snowed", "snows", "son", "sons", "sorry", "sphere", "spheres", "square", "squares", "star", "stars", "starry", "strong", "strength", "study", "studies", "studying", "studied" , "summer", "summers", "sun", "sunday", "telephone", "telephones", "telescope", "telescopes", "thank", "thanks", "three", "thursday", "triangle", "triangles", "tuesday", "two", "wada", "wadas", "weather", "wednesday", "welcome", "welcomes", "welcoming", "welcomed", "white", "whitish", "wife", "wives", "wind", "winds", "windy", "winter", "winters", "work", "world", "x-ray", "x-rays", "year", 'years', "yellow", "yes", "you", "your", "yours", "yourself", "yourselves", "zero", "zoo", "zoos", 'atmosphere', 'eclipse', "eclipses", 'environment', 'equator', 'expert', "experts", 'hardworking', 'lie', "lies", "lying", "lied", 'map', "maps", 'north', 'patience', 'patient','radio', "radios", 'record', "records", 'right', 'sound', "sounds", 'south', 'television', "televisions", 'tv', "tvs", 'trouble', "troubles", "troubled", "troubling", 'trust', "trusted", "trusting", "trusts", 'universe', 'west', 'wrong', 'confident', "confidence", 'intelligent', "intellegence", 'knowledge', 'busy', 'brave', "bravery", 'tea', 'milk', 'heart', "hearts", 'talk', 'speak','speaking','speaks','spoke',"talking", "talks", "talked", 'stand', "standing", "stands", "stood", 'smell', "smelling", "smells", "smelt", 'sleep', "sleeping", "sleeps", "slept", 'sit', "sits", "sat", "sitting", 'see','seen', "seeing", "saw", "sees", 'run', "running", "runs", "ran", 'pain', "paining", "pains", "pained", 'hair', "hairs", 'nose', "noses", 'concentrate', "concentrated", "concentrating", "concentrates", 'old', 'young', 'battery', "batteries", 'electronics', "electronic", 'sofa', "sofas", 'clock', "clocks", 'window', "windows", 'umbrella', "umbrellas",'towel', "towels", 'plate', "plates", 'spoon', "spoons", 'flower', "flowers", 'tree', "trees", 'common', 'wet', "wetness", 'wear', "wears", "wearing", "wore", "worn", 'wash', "washes", "washed", "washing", 'wait', "waiting", "waited", "waits", 'visit', "visits", "visiting", "visited", 'swim', "swims", "swimming", "swam", 'stop', "stops", "stopped", "stopping", 'start', "starts", "starting", "started", 'whistle', "whistling", "whistles", "whistled", 'tabla', "tablas", 'stage', "stages", 'guitar', "guitars", 'sing', "sings", "singing", "sang", 'sculpture', "sculptures", 'magic', "magical", "magically", 'flute', "flutes", 'entertainment', 'drum', "drums", 'doll', "dolls", 'cinema', "cinemas", 'balloon', "balloons", 'art', "first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "zeroth", "open", "opened", "opens", "opening",'reddish','orangish','greenish','greenery','bluish','blackish','yellowish','pinkish', 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', '1','2','3','4','5','6','7','8','9','0']
#letterNum = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', '1','2','3','4','5','6','7','8','9','0']
print(len(list_eng))
global level_words
level_words = []
global Q 
Q = ""
global score1_lb
global total1_lb
score1_lb = tk.Label(window2, text = "Score:", font=('Cambria',35),bg='#FFBC8B')
total1_lb = tk.Label(window2, text = "Total Questions:", font=('Cambria',35),bg='#FFBC8B')
score1_lb.place(x = 900, y = 125)
total1_lb.place(x = 900, y = 175)
global score2_lb
global total2_lb
score2_lb = tk.Label(window2, text = score, font=('Cambria',35),bg='#FFBC8B')
total2_lb = tk.Label(window2, text = total, font=('Cambria',35),bg='#FFBC8B')
score2_lb.place(x = 1250, y = 125)
total2_lb.place(x = 1250, y = 175)

def chooseL():
    makeList(5)

def makeList(levelNo):
    level = levelNo
    for i in list_eng:
        if level==1:
            if len(i)==1:
                level_words.append(i)
        elif level==2:
            if len(i)>1 and len(i)<=3:
                level_words.append(i)
        elif level==3:
            if len(i)>3 and len(i)<=5:
                level_words.append(i)
        elif level==4:
            if len(i)>5 and len(i)<=7:
                level_words.append(i)
        elif level==5:
            if len(i)>7:
                level_words.append(i)

                
def selectQ(level_words):
    global Q
    vid = random.randint(0, (len(level_words)-1))
    Q = level_words[vid]
              
global video
video = tk.Label(window2,bg='#FFBC8B')
video.place(x = 650, y = 160)    
    
    
def call_game(I):
    global video
    video = tk.Label(window2,bg='#FFBC8B')
    video.place(x = 610, y = 200) 
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
      
      cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
      img = Image.fromarray(cv2image)
      imgtk = ImageTk.PhotoImage(image=img)
      
      # if ret == True: 
       
      #   # Display the resulting frame
      #   cv2.moveWindow('Frame',750,160)
      #   cv2.imshow('Frame', frame) 
       
      #   # Press Q on keyboard to  exit 
      #   if cv2.waitKey(25) & 0xFF == ord('q'): 
      #      break
       
      # # Break the loop 
      # else:  
      #   break
       
      video.config(image=imgtk)

      window2.update()
      time.sleep(0.02)
      
    
    # When everything done, release  
    # the video capture object 
    cap.release() 

def playVid():
    global Q
    selectQ(level_words)
    call_game(Q)

def displayQ():
    global playVid_btn
    playVid_btn = tk.Button(window2, text = "Play the video", command = playVid, font=('Cambria',40),bg='#F29062')
    playVid_btn.place(x = 100, y = 250)
    
def accept_ans():
    global score
    global total
    global answer_ent
    global answer_btn
    global answer_lb
    global Q
    global answer
    global score2_lb
    global total2_lb
    global answerRight_lb
    
    total+=1
    answer = answer_ent.get().lower()
    ansCorrect_lb = tk.Label(window2, text = "Correct Answer!",font=('Cambria',25),bg='#FFBC8B')
    ansWrong_lb = tk.Label(window2, text = 'Incorrect Answer\nCorrect answer is :', font=('Cambria',14),bg='#FFBC8B')
    answerRight_lb = tk.Label(window2, text = Q, font=('Cambria',14),bg='#FFBC8B')
    if answer==Q:
        ansCorrect_lb.place(x = 975, y = 400, width = 300)
        score+=1
    else:   
        ansWrong_lb.place(x = 975, y = 400, width = 300)
        answerRight_lb.place(x = 1205, y=422)
    score2_lb = tk.Label(window2, text = score, font=('Cambria',35),bg='#FFBC8B')
    total2_lb = tk.Label(window2, text = total, font=('Cambria',35),bg='#FFBC8B')
    score2_lb.place(x = 1250, y = 125)
    total2_lb.place(x = 1250, y = 175)
    
    
def enter_ans():
    global answer_btn
    global Q
    global answer_ent
    answer_lb = tk.Label(window2, text = "Enter your Answer",font=('Cambria',14),bg='#FFBC8B')
    answer_lb.place(x = 975, y = 300)
    answer_ent = tk.Entry(window2, width = 30,font=('Cambria',14))
    answer_ent.place(x=975, y=360)
    answer_btn = tk.Button(window2, text = "Enter", font=('Cambria',14), command=accept_ans,bg='#F29062')
    answer_btn.place(x = 1250, y = 354)


def next_func():
    global video
    global answer_ent
    answer_ent.delete('0','end')
    cv2.destroyAllWindows()
    video.destroy()
    clear_lb = tk.Label(window2, font=('Cambria',30),bg='#FFBC8B')
    clear_lb.place(x = 975, y = 400, width = 300)

    
    
def display_next():
    global next_btn
    next_btn = tk.Button(window2, text = "Next Question", font=('Cambria',16), command=next_func,bg='#F29062')
    next_btn.place(x = 975, y = 500)

def playAgain_func():
    global Q
    call_game(Q)
    
def playAgain():
    global playAgain_btn
    playAgain_btn = tk.Button(window2, text = "Play Again", command = playAgain_func, font=('Cambria',40),bg='#F29062')
    playAgain_btn.place(x = 100, y = 450)
    
def quit_func():
    window2.destroy()
    
def display_quit():
    global quit_btn
    quit_btn = tk.Button(window2, text = "Quit", command = quit_func, font=('Cambria',16),bg='#F29062')
    quit_btn.place(x = 1150, y = 500)


chooseL()               
displayQ()
display_next()
playAgain()
display_quit()
enter_ans()



window2.mainloop()