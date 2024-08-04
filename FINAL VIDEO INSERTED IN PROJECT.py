

from tkinter import *
from PIL import ImageTk, Image


import cv2 
import numpy as np 
 

root = Tk()
ent=input("Enter : ")
list= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', "above", "absent", "across", "add", 'added',"address", "advance", "africa", "after", "afternoon", "age", "air", "airport", "all", "ambulance", "among", "angry", "animal", "antartica", "apple", "april", "area", "arm", "asia", "ask", "august", "australia", "baby", "back", "bad", "badminton", "ball", "banana", "bank", "bathroom", "beat", "beautiful", "behind", "bird", "birthday", "black", "blue", "boat", "book", "born", "boy", "brain", "breeze", "bright", "brown", "buy", "bye", "call", "calm", "camera", "can", "cancel", "cap", "careless", "carrot", "cash", "cat", "chair", "change", "chapter", "chicken", "children", "circle", "clever", "clouds", "coffee", "cold", "college", "colour", "come", "cone", "continent", "copy", "cry", "cube", "cuboid", "cylinder", "dance", "dark", "date", "daughter", "day", "deaf", "december", "desk", "diabetes", "die","difficult", "dinner", "dirty", "doctor", "document", "dog", "dosa", "doubt", "earn", "earth", "east", "eat", "echo", "eight", "elbow", "email", "empty", "engineer", "enjoy", "europe", "evening", "exam", "eye", "face", "fail", "fall", "false", "family", "fat", "father", "fear", "february", "feel", "film", "fire", "fish", "five", "floor", "four", "free", "friday", "friend", "fruits", "games", "gas", "gate", "girl", "glass", "go", "goal", "god", "golden", "good", "grandfather", "grandmother", "grass", "green", "grey", "happy", "he", "hear", "hello", "help", "hindi", "home", "hope", "hot", "house", "husband", "idli", "in", "income", "increase", "india", "information", "insect", "interest", "introduction", "jail", "january", "jeep", "july", "june", "lazy", "lemon", "light", "mango", "march", "me", "mix", "monday", "month", "moon", "morning", "mother", "music", "my", "name", "nice", "night", "nine", "no", "november", "october", "office", "one", "orange", "pendulum", "phone", "pink", "please", "proud", "purple", "railway", "rain", "rainbow", "rectangle", "red", "reflection", "roti", "sad", "sambhar", "saturday", "school", "september", "seven", "she", "shop", "silver", "sister", "six", "snow", "son", "sorry", "sphere", "square", "star", "strong", "study" , "summer", "sun", "sunday", "telephone", "telescope", "thank", "three", "thursday", "triangle", "tuesday", "two", "wada", "weather", "wednesday", "welcome", "white", "wife", "wind", "winter", "work", "world", "x-ray", "year", "yellow", "yes", "you", "your", "yours", "yourself", "zero", "zoo"]
ent=ent.lower()
list1=[]
verbs=['the','an','a','is','are','was','were','will','am','be','being','been','has','have','had','having','do','does','did',"can","could", "may", "might", "must", "ought", "shall","should", 'would','to','and','or']


def call(I):
     
    # Create a VideoCapture object and read from input file 
    cap = cv2.VideoCapture('videos/'+I+'.mp4') 
       
    # Check if camera opened successfully 
    if (cap.isOpened()== False):  
      print("Error opening video  file") 
       
    # Read until video is completed 
    while(cap.isOpened()): 
          
      # Capture frame-by-frame 
      ret, frame = cap.read() 
      if ret == True: 
       
        # Display the resulting frame
        cv2.moveWindow('Frame',530,140)
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
   
 
              
def myClick():
    global c
    c=0
    for i in list1:
    #i=list1[c]
        c+=1
        call(i)
    if c==(len(list1)):
      # Closes all the frames 
      cv2.destroyAllWindows()

 

root.geometry ('1250x700') 

 

print('The Main Words are:') 
words = ent.split()
for i in words:
    if i in verbs:
        continue
    else:
        if i in list:
            list1.append(i)
            print(i)
        else:
            for j in i:
                list1.append(j)
                print(j)
            print(' ')
  
btn= Button(root,text='click me',command=myClick)
btn.pack()

 


root.mainloop()