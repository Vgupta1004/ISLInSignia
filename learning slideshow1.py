import imageio
from tkinter import *
from PIL import ImageTk, Image
from pathlib import Path
import time

 

root = Tk()
ent=input("Enter : ")
list= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', "above", "absent", "across", "add", "address", "advance", "africa", "after", "afternoon", "age", "air", "airport", "all", "ambulance", "among", "angry", "animal", "antartica", "apple", "april", "area", "arm", "asia", "ask", "august", "australia", "baby", "back", "bad", "badminton", "ball", "banana", "bank", "bathroom", "beat", "beautiful", "behind", "bird", "birthday", "black", "blue", "boat", "book", "born", "boy", "brain", "breeze", "bright", "brown", "buy", "bye", "call", "calm", "camera", "can", "cancel", "cap", "careless", "carrot", "cash", "cat", "chair", "change", "chapter", "chicken", "children", "circle", "clever", "clouds", "coffee", "cold", "college", "colour", "come", "cone", "continent", "copy", "cry", "cube", "cuboid", "cylinder", "dance", "dark", "date", "daughter", "day", "deaf", "december", "desk", "diabetes", "die","difficult", "dinner", "dirty", "doctor", "document", "dog", "dosa", "doubt", "earn", "earth", "east", "eat", "echo", "eight", "elbow", "email", "empty", "engineer", "enjoy", "europe", "evening", "exam", "eye", "face", "fail", "fall", "false", "family", "fat", "father", "fear", "february", "feel", "film", "fire", "fish", "five", "floor", "four", "free", "friday", "friend", "fruits", "games", "gas", "gate", "girl", "glass", "go", "goal", "god", "golden", "good", "grandfather", "grandmother", "grass", "green", "grey", "happy", "he", "hear", "hello", "help", "hindi", "home", "hope", "hot", "house", "husband", "idli", "in", "income", "increase", "india", "information", "insect", "interest", "introduction", "jail", "january", "jeep", "july", "june", "lazy", "lemon", "light", "mango", "march", "me", "mix", "monday", "month", "moon", "morning", "mother", "music", "my", "name", "nice", "night", "nine", "no", "november", "october", "office", "one", "orange", "pendulum", "phone", "pink", "please", "proud", "purple", "railway", "rain", "rainbow", "rectangle", "red", "reflection", "roti", "sad", "sambhar", "saturday", "school", "september", "seven", "she", "shop", "silver", "sister", "six", "snow", "son", "sorry", "sphere", "square", "star", "strong", "study" , "summer", "sun", "sunday", "telephone", "telescope", "thank", "three", "thursday", "triangle", "tuesday", "two", "wada", "weather", "wednesday", "welcome", "white", "wife", "wind", "winter", "work", "world", "x-ray", "year", "yellow", "yes", "you", "your", "yours", "yourself", "zero", "zoo"]
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
              vid='videos/'+ I +'.mp4'
              
              video = imageio.get_reader(vid)
              delay = int(2000 / video.get_meta_data()['fps'])
              my_label = Label(root,height=780,width=500)
              my_label.place(x=70,y=0)
              my_label.after(delay, lambda: stream(my_label))
              
              root.after(10000 ,my_label.destroy)
              
    
              
def show():
    for i in range(0,len(list1)):
        myClick()
        root.update_idletasks() 
        root.update()
        time.sleep(2)
        
def myClick():
    global c
    i=list1[c]
    c+=1
    call(i)
    if c==(len(list1)):
        btn['state']=DISABLED

 

root.geometry ('1250x2000') 

 

print('The Main Words are:') 
words = ent.split()
for i in words:
    if i in list:
        list1.append(i)
        print(i)
    else:
        for j in i:
            list1.append(j)
            print(j)
        print(' ')
    
btn= Button(root,text='click me',command=show)
btn.pack()

 

root.mainloop()