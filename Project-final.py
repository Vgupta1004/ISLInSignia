# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 18:52:11 2021

@author: Vyapti
"""

#importing all modules required throughout program
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
import speech_recognition as sr
import cv2 
import numpy as np 
import time
#_______________________________________________________
#defining the main window
window1=tk.Tk()
window1.title('Sign Language Generator')
window1.geometry('1250x700')
window1.iconbitmap('D:/Reliance school/Computer project/Danieledesantis-Audio-Video-Outline-Play.ico')#_______________________________________________________

user_name=''  #for accepting the name of the user in the homepage
text=''
c1=0
#_______________________________________________________
#function for taking name input in homepage
def EnterName():
    global user_name
    user_name = name_ent.get()
    global nameError_lb
    global wlcm_lb
    nameError_lb=tk.Label(frame3,text='*Please enter atleast one character for name',bg='#FFBC8B',fg='red',font=('Cambria',10))

    if len(user_name)<1:
        nameError_lb.place(x=200,y=5)
    else:               
        wlcm_lb=tk.Label(frame3,text='Welcome '+user_name+"!!!",font=('Cambria',20),bg='#FFBC8B')
        wlcm_lb.place(x=210,y=80)
        
        nameError_lb.place_forget()
        
        name_ent['state']=tk.DISABLED
#_______________________________________________________        
#function for quitting the program
def windestroy():
     tk.messagebox.showinfo("Quit","You have chosen to exit the program\nThank you for visiting")
     window1.destroy()        
#_______________________________________________________
#video display
def call(I):
     
    # Create a VideoCapture object and read from input file 
    cap = cv2.VideoCapture('videos/'+I+'.mp4') 
       
    # Check if camera opened successfully 
    if (cap.isOpened()== False):  
      tk.messagebox.showinfo("Video error!","Error opening video  file") 
       
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
#_______________________________________________________
#function to play the video
def play():
    global c
    global list1
    global text_mainwords
    global btn_play
    c=0
    for i in list1:
    
        c+=1
        call(i)
    if c==(len(list1)):
      # Closes all the frames 
      time.sleep(1)
      cv2.destroyAllWindows()
      text_mainwords.destroy()
      eng_audio_btn['state']=tk.NORMAL
      eng_audio_ent['state']=tk.NORMAL
      eng_audio_ent.delete('0','end')
      btn_play['state']=tk.DISABLED
      global c1
      c1 = 0
#_______________________________________________________
#function to bifurcate input sentence into main words
def Submit():
    global lbl_mainwords
    global frame4
    global text_mainwords
    global btn_play
    global list1
    global sentences
    
    text = eng_audio_ent.get().lower()
    if len(text)>0:
        eng_audio_btn['state']=tk.DISABLED
        eng_audio_ent['state']=tk.DISABLED
        list1=[]
        words = text.split()
        lbl_mainwords=tk.Label(frame4)
        text_mainwords = tk.Text(frame4,width=200,height=200,bg='#FFBC8B',font=('Cambria',14),borderwidth=0)
        text_mainwords.pack(padx=20,pady=50)
        if text in sentences:
            list1=[text]
            for i in words:
                text_mainwords.insert('insert','-->'+i+'\n')
        else:
            for i in words:
                if i in verbs:
                    continue
                else:
                    if i in list:
                        list1.append(i)
                        text_mainwords.insert('insert','-->'+i+'\n')
                        
                    else:
                        for j in i:
                            list1.append(j)
                            text_mainwords.insert('end','-->'+j+'\n')
                        
                    
        
        frame5=tk.Frame(English_tab,bg='#FFBC8B')
        frame5.place(x=750,y=350,width=300,height=300)
        btn_play= tk.Button(frame5,text='Play the video',command=play,font=('Cambria',28),bg='#F29062')
        btn_play.place(x=20,y=20)
    
#_______________________________________________________
#function for receiving audio in Sign lanuguage generator
def receive_audio():
    global c1
    global eng_audio_ent
    if c1==0:
        c1=1
    else:
        eng_audio_ent.delete('0','end')
    sample_rate = 48000
    chunk_size = 2048
    r = sr.Recognizer()
    
            
    with sr.Microphone(sample_rate = sample_rate,  chunk_size = chunk_size) as source:
        
        r.adjust_for_ambient_noise(source,duration=0.5)
        
        audio = r.listen(source) 
              
        try:          
            global speak_text
            global text                                                     
            speak_text = r.recognize_google(audio)   
            speak_text = speak_text[0].upper()+speak_text[1:len(speak_text)]
            eng_audio_ent.insert(0, speak_text)
            text = eng_audio_ent.get().lower()
                                 
            
            
        except sr.UnknownValueError: 
            tk.messagebox.showinfo('Input Error!!!',"Google Speech Recognition could not understand audio\nPlease enter again")
            #("Google Speech Recognition could not understand audio") 
      
        except sr.RequestError as e: 
           tk.messagebox.showinfo("Input Error!!!","Could not request results from Google Speech Recognition service; {0}".format(e))    
           #print("Could not request results from Google Speech Recognition service; {0}".format(e))
#_______________________________________________________

#designing Sign lanuguage generator page
def eng_converter():
    
    audio_nb.select(1) #opening Sign lanuguage generator tab
    #_______________________________________________________
    #window heading
    frame1=tk.Frame(English_tab,bg='#FFBC8B')
    frame1.place(x=0,y=10,width=1500,height=120)
    heading_lb1= tk.Label(frame1,fg='black',bg='#FFBC8B',text='IN',font=('Gabriola',65,))
    heading_lb1.place(x=480,y=5)
    heading_lb2= tk.Label(frame1,fg='black',bg='#FFBC8B',text='SIGN',font=('Gabriola',68,'bold'))
    heading_lb2.place(x=550,y=0)
    heading_lb3= tk.Label(frame1,fg='black',bg='#FFBC8B',text='IA',font=('Gabriola',65,))
    heading_lb3.place(x=700,y=5)
    #_______________________________________________________
    #displaying menu bar
    frame2=tk.Frame(English_tab,bg='#5B524A')
    frame2.place(x=0,y=150,width=1500,height=50)
    homepage_btn=tk.Button(frame2,text='Homepage',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=homepage)
    homepage_btn.pack(side='left')
    English_btn=tk.Button(frame2,text='Sign lanuguage generator',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=eng_converter)
    English_btn.pack(side='left')
    About_btn=tk.Button(frame2,text='About',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=about_page)
    About_btn.pack(side='left')
    Quit_btn=tk.Button(frame2,text='Quit',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=windestroy)
    Quit_btn.pack(side='left')
    #________________________________________________________
    #audio/text input form user either by typing in entry box or by using mic
    global eng_audio_ent
    global eng_audio_btn
    global english_pic1
    global english_pic2
    global english_pic3
    global frame3
    frame3=tk.Frame(English_tab,bg='#FFBC8B')
    frame3.place(x=650,y=220,width=570,height=125)
    input_audio_lb=tk.Label(frame3,text='Press on the mic button to enter audio\n(Please wait for 2 seconds before speaking into your mic)',bg='#FFBC8B',font=('Cambria',14,'bold'))
    input_audio_lb.place(x=10,y=10)
    
    eng_audio_ent=tk.Entry(frame3,font=16,borderwidth=1,relief='solid')
    eng_audio_ent.place(x=10,y=60,width=400,height=37)
    
    english_pic1=Image.open('images/mic1.png')
    english_pic2 = english_pic1.resize((35,35),Image.ANTIALIAS)
    english_pic3=ImageTk.PhotoImage(english_pic2)
    
    eng_audio_btn= tk.Button(frame3, image = english_pic3 ,command=receive_audio, borderwidth = 0)
    eng_audio_btn.place(x=410,y=60)
    
    eng_submit = tk.Button(frame3, text = 'Submit',bg='#F29062',font=('Cambria',14),command = Submit)
    eng_submit.place(x=460,y=60)
    #_______________________________________________________
    #start displaying main words
    global list
    global verbs
    global text
    global frame4
    global sentences
    frame4=tk.Frame(English_tab,bg='#FFBC8B')
    frame4.place(x=60,y=220,width=550,height=400)
    list= ['1','2','3','4','5','6','7','8','9','0','how','what','when','where','which','who','why','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', "above", "absent", "across", "add", 'added','adding','adds',"address",'addresses', "advance", 'advanced','advances','advancing','advancement',"africa", "after", 'afterwards',"afternoon", "age",'aged','aging', 'ages',"air", "airport",'airports', "all", "ambulance",'ambulances', "among", 'amongst',"angry",'anger', "animal",'animals', "antartica", "apple",'apples', "april", "area", 'areas',"arm",'arms', "asia", "ask", 'asks','asked','asking',"august", "australia", "baby", 'babies',"back",'backwards', "bad", "badminton", "ball",'balls',"banana",'bananas', "bank", 'banking','banks',"bathroom",'bathrooms', "beat", 'beats', 'beating', "beautiful", 'beautifully', "behind", "bird", 'birds',"birthday", 'birthdays',"black", "blue", "boat", 'boating','boats',"book",'books' "born", 'birth', "boy",'boys', "brain", 'brains', "breeze", "bright", 'brighten', 'brightness', 'brightly', "brown", "buy", 'buys','buying','bought',"bye", 'goodbye',"call", 'calls','called','calling',"calm",'calming', "camera", 'cameras', "can", 'could', "cancel", 'cancelled', 'cancelling', "cap", 'caps', 'car', 'cars', "careless", 'carelessness', "carrot", 'carrots', "cash", 'money', "cat", 'cats', "chair", 'chairs', "change", 'changing', 'changed', 'changes', "chapter", 'chapters', "chicken", 'chickens', 'child', "children", "circle", 'circles', "clever", 'cleverness', 'cleverly', "clouds", 'cloud', "coffee", "cold", "college", 'colleges', "colour", 'colours', 'color', 'colors', 'colouring', 'coloured', "come", 'came', 'coming', "cone", 'cones', "continent", 'continents', "copy", 'copies', 'copied', 'copying', "cry", 'cries', 'cried', 'crying', "cube", 'cubes', 'cuboids', "cuboid", 'cylinders', "cylinder", "dance", 'dances', 'dancing', 'danced', "dark", "darkness", "date", "dates", "daughter","daughters", "day", "days", "deaf", "deafness", "december", "desk", "desks", "diabetes", "die", "dies", "died", "difficult", 'difficulty', "dinner", "dinners", "dirty", "doctor", "doctors", "document", "documents", "dog", "dogs", "dosa", "dosas", "doubt", "doubts", "doubtful", "earn", "earns", "earned", "earning", "earth", "east", "eat", "eats", "eating", "ate", "eaten", "echo", "echos", "echoed", "echoing", "eight", "elbow", "elbows", "email", "emails", "empty", "emptiness", "empties", "emptied", "emptying", "engineer", "engineers", "enjoy", "enjoying", "enjoys", "enjoyed", "europe", "evening", "evenings", "exam", "exams", "eye", "eyes", "face", "faces", "fail", "failing", "fails", "failed", "fall", "falling", "falls", "fell", "fallen", "false", "family", "families", "fat", "father", "fathers", "fear", "fears", "feared", "fearful", "fearing", "february", "feel", "feeling", "feels", "felt", "film", "films", "fire", "fish", "fishes", "five", "floor", "floors", "four", "free", "frees", "freed", "friday", "friend", "friends", "fruit", "fruits", "game", "games", "gas", "gases", "gate", "gates", "girl", "girls", "glass", "glasses", "go", "going", "went", "gone", "goes", "goal", "goals", "goaling", "god", "gods", "golden", "good", "goodness", "grandfather", "grandfathers", "grandmother", "grandmothers", "grass", "green", "grey", "happy", "happiness", "he", "his", "hear", "hearing", "heard", "hears", "hello", "hi", "help", "helps", "helping", "helped", "hindi", "home", "homes", "hope", "hopes", "hopeful", "hoping", "hoped", "hot", "house", "houses", "husband", "husbands", "idli", "idlis", "in", "income", "incomes", "increase", "increasing", "increased", "increases", "india", "information", "insect", "insects", "interest", "interesting", "interested", "interests", "introduction", "intrductions", "jail", "jails", "january", "jeep", "jeeps", "july", "june", "lazy", "laziness", "lazily", "lemon", "lemons", "light", "lights", "lighting", "lighten", "lighted", "mango", "mangoes", "march", "me", "mix", "mixing", "mixed", "mixes", "monday", "month", "months", "monthly", "moon", "moons", "morning", "mornings", "mother", "mothers", "music", "musical", "musically", "my", "name", "names", "nice", "nicely", "night", "nights", "nine", "no", "not", "november", "october", "office", "offices", "one", "orange", "oranges", "pendulum", "pendulums", "phone", "phones", "pink", "please", "proud", "pride", "purple", "railway", "railways", "rain", "rains", "raining", "rained", "rainy", "rainbow", "rainbows", "rectangle", "rectangles", "red", "reflection", "reflections", "roti", "rotis", "sad", "sadness", "sadly", "sambhar", "saturday", "school", "schools", "september", "seven", "she", "her", "shop", "shops", "shopping", "shopped", "silver", "sister", "sisters", "six", "snow", "snowy", "snowing", "snowed", "snows", "son", "sons", "sorry", "sphere", "spheres", "square", "squares", "star", "stars", "starry", "strong", "strength", "study", "studies", "studying", "studied" , "summer", "summers", "sun", "sunday", "telephone", "telephones", "telescope", "telescopes", "thank", "thanks", "three", "thursday", "triangle", "triangles", "tuesday", "two", "wada", "wadas", "weather", "wednesday", "welcome", "welcomes", "welcoming", "welcomed", "white", "whitish", "wife", "wives", "wind", "winds", "windy", "winter", "winters", "work", "world", "x-ray", "x-rays", "year", 'years', "yellow", "yes", "you", "your", "yours", "yourself", "yourselves", "zero", "zoo", "zoos", 'atmosphere', 'eclipse', "eclipses", 'environment', 'equator', 'expert', "experts", 'hardworking', 'lie', "lies", "lying", "lied", 'map', "maps", 'north', 'patience', 'radio', "radios", 'record', "records", 'right', 'sound', "sounds", 'south', 'television', "televisions", 'tv', "tvs", 'trouble', "troubles", "troubled", "troubling", 'trust', "trusted", "trusting", "trusts", 'universe', 'west', 'wrong', 'confident', "confidence", 'intelligent', "intellegence", 'knowledge', 'busy', 'brave', "bravery", 'tea', 'milk', 'heart', "hearts", 'talk', "talking", "talks", "talked", 'stand', "standing", "stands", "stood", 'smell', "smelling", "smells", "smelt", 'sleep', "sleeping", "sleeps", "slept", 'sit', "sits", "sat", "sitting", 'see', "seeing", "saw", "sees", 'run', "running", "runs", "ran", 'pain', "paining", "pains", "pained", 'hair', "hairs", 'nose', "noses", 'concentrate', "concentrated", "concentrating", "concentrates", 'old', 'young', 'battery', "batteries", 'electronics', "electronic", 'sofa', "sofas", 'clock', "clocks", 'window', "windows", 'umbrella', "umbrellas",'towel', "towels", 'plate', "plates", 'spoon', "spoons", 'flower', "flowers", 'tree', "trees", 'common', 'wet', "wetness", 'wear', "wears", "wearing", "wore", "worn", 'wash', "washes", "washed", "washing", 'wait', "waiting", "waited", "waits", 'visit', "visits", "visiting", "visited", 'swim', "swims", "swimming", "swam", 'stop', "stops", "stopped", "stopping", 'start', "starts", "starting", "started", 'whistle', "whistling", "whistles", "whistled", 'tabla', "tablas", 'stage', "stages", 'guitar', "guitars", 'sing', "sings", "singing", "sang", 'sculpture', "sculptures", 'magic', "magical", "magically", 'flute', "flutes", 'entertainment', 'drum', "drums", 'doll', "dolls", 'cinema', "cinemas", 'balloon', "balloons", 'art', "first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "zeroth", "open", "opened", "opens", "opening", "comes", "mother's", "father's","grandfather's", "grandmother's"]
    sentences = ['how are you','what is your name', 'i am fine', 'you are wrong', 'where is the police station', 'where is the hospital', 'where is the bathroom', 'where is the restroom', 'where is the washroom', 'where do you stay', "where do you live", 'when will we go', 'what is your moblie number', "what is your phone number", 'what is your job', 'what is your age', "how old are you", 'what date is it today', 'what is the problem', 'what are you doing', 'wait i am thinking', 'that is good', 'take care', 'stand up', 'sit down', 'shall i help you', 'can i help you', 'please call me later', 'please call an ambulance', "please call the ambulance", 'open the door', "open the doors", 'no smoking please', 'nice to meet you', 'let us go for lunch', 'keep quite', 'i have headache', 'i do not understand anything', 'i am tired', 'i am thinking', 'i am sorry', 'happy journey', 'good question', 'do not worry', 'be careful', 'are you sick', 'are you hungry', 'are you busy', 'all the best']
    verbs=['the','an','is','are','was','were','will','am','be','being','been','has','have','had','having','do','does','did', "may", "might", "must", "ought", "shall","should", 'would','to','and','or','on','of']
    lbl_display=tk.Label(frame4,text='The Main Words/Characters Are:',bg='#FFBC8B',font=('Cambria',20,'bold'))
    lbl_display.place(x=10,y=10)


#_______________________________________________________
#designing about page
def about_page():
    audio_nb.select(2) #opening about page tab
    #_______________________________________________________
    #window heading
    frame1=tk.Frame(About_tab,bg='#FFBC8B')
    frame1.place(x=0,y=10,width=1500,height=120)
    heading_lb1= tk.Label(frame1,fg='black',bg='#FFBC8B',text='IN',font=('Gabriola',65,))
    heading_lb1.place(x=480,y=5)
    heading_lb2= tk.Label(frame1,fg='black',bg='#FFBC8B',text='SIGN',font=('Gabriola',68,'bold'))
    heading_lb2.place(x=550,y=0)
    heading_lb3= tk.Label(frame1,fg='black',bg='#FFBC8B',text='IA',font=('Gabriola',65,))
    heading_lb3.place(x=700,y=5)
    #_______________________________________________________
    #displaying menu bar
    frame2=tk.Frame(About_tab,bg='#5B524A')
    frame2.place(x=0,y=150,width=1500,height=50)
    homepage_btn=tk.Button(frame2,text='Homepage',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=homepage)
    homepage_btn.pack(side='left')
    English_btn=tk.Button(frame2,text='Sign lanuguage generator',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=eng_converter)
    English_btn.pack(side='left')
    About_btn=tk.Button(frame2,text='About',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=about_page)
    About_btn.pack(side='left')
    Quit_btn=tk.Button(frame2,text='Quit',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=windestroy)
    Quit_btn.pack(side='left')
    #________________________________________________________
    info1='A sign language generator\nCan help make communication clear\nBecause sign language is the mother tongue\nFor those who have the inability to speak or hear'
    info2='             All humans being social animals wish to express their thoughts to each other.\n                                                   However, this task may become a bit challenging for the people who are hard of hearing or aphonic.\n                                                  Thus, this audio to sign language converter can convert audio to required visuals. These include the\ncombination of hand movements, arms or body and facial expressions.'
    info3='This program has been developed using Python programming language.\n                      In this program, the input may be given by speaking or typing. If audio input is given,\n                                       then the audio is converted to text using Google speech API. The main words from the text are \n     identified and the videos can be played by the user on the click of a button.'
    frame3=tk.Frame(About_tab,bg='#FFBC8B',width=1100,height=100)
    frame3.place(x=50,y=230)
    lbl_info1=tk.Label(frame3,bg='#FFBC8B',text=info1,font=('Cambria',14,'bold','italic'))
    lbl_info1.place(x=300,y=0)
    frame4=tk.Frame(About_tab,bg='#FFBC8B',width=500,height=100)
    frame4.place(x=0,y=350)
    lbl_info2=tk.Label(frame4,bg='#FFBC8B',text=info2,font=('Cambria',12))
    lbl_info2.pack()
    frame5=tk.Frame(About_tab,bg='#FFBC8B',width=1100,height=100)
    frame5.place(x=48,y=435)
    lbl_info3=tk.Label(frame5,bg='#FFBC8B',text=info3,font=('Cambria',12))
    lbl_info3.pack()
    #________________________________________________________
    
    global about_pic1
    global about_pic2
    
    frame4=tk.Frame(About_tab,bg='#FFBC8B',width=500,height=500)
    frame4.place(x=930,y=300)
    about_pic1=Image.open('images/about.jpg')
    about_pic2=ImageTk.PhotoImage(about_pic1)
    lbl= tk.Label(frame4, image = about_pic2)
    lbl.place(x=0,y=0)
#___________________________________________________________________
#function for designing the homepage
def homepage():
    audio_nb.select(0)
    #_______________________________________________________
    #window heading
    frame1=tk.Frame(Homepage_tab,bg='#FFBC8B')
    frame1.place(x=0,y=10,width=1500,height=120)
    heading_lb1= tk.Label(frame1,fg='black',bg='#FFBC8B',text='IN',font=('Gabriola',65,))
    heading_lb1.place(x=480,y=5)
    heading_lb2= tk.Label(frame1,fg='black',bg='#FFBC8B',text='SIGN',font=('Gabriola',68,'bold'))
    heading_lb2.place(x=550,y=0)
    heading_lb3= tk.Label(frame1,fg='black',bg='#FFBC8B',text='IA',font=('Gabriola',65,))
    heading_lb3.place(x=700,y=5)
    #_______________________________________________________
    #displaying menu bar
    frame2=tk.Frame(Homepage_tab,bg='#5B524A')
    frame2.place(x=0,y=150,width=1500,height=50)
    homepage_btn=tk.Button(frame2,text='Homepage',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=homepage)
    homepage_btn.pack(side='left')
    English_btn=tk.Button(frame2,text='Sign lanuguage generator',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=eng_converter)
    English_btn.pack(side='left')
    About_btn=tk.Button(frame2,text='About',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=about_page)
    About_btn.pack(side='left')
    Quit_btn=tk.Button(frame2,text='Quit',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=windestroy)
    Quit_btn.pack(side='left')
    #_______________________________________________________
    #name accepting
    global name_ent
    global frame3
    global name_btn
    frame3=tk.Frame(Homepage_tab,bg='#FFBC8B')
    frame3.place(x=10,y=280,width=600,height=150)
    name_lb=tk.Label(frame3,bg='#FFBC8B',text="Enter Your Name:",font=('Cambria',14))
    name_lb.place(x=15,y=30)
    name_ent=tk.Entry(frame3,width=30,font=('Cambria',14))
    name_ent.place(x=175,y=28)
    name_btn=tk.Button(frame3,text='Enter',bg='#F29062',font=('Cambria',14),command=EnterName)
    
    #checking if the user is visiting the home page for the first time
    if globals()['c_homepage']==0:
        globals()['c_homepage']=1
        
    elif globals()['c_homepage']==1 and user_name=='':
        pass   
    else:
        name_btn['state']=tk.DISABLED
        wlcm_lb=tk.Label(frame3,text='Welcome '+user_name+"!!!",font=('Cambria',20),bg='#FFBC8B')
        wlcm_lb.place(x=210,y=80)
        name_ent.insert(0,user_name)
        name_ent['state']=tk.DISABLED
        
    name_btn.place(x=525,y=22) 
    #_________________________________________________________
    
    #side animation
    global homepage_pic1
    global homepage_pic2
    global homepage_pic3
    frame4=tk.Frame(Homepage_tab,highlightcolor='black',highlightbackground='black',highlightthickness=1)
    frame4.place(x=800,y=250,height=350,width=350)
    homepage_pic1 = Image.open('images/boy.png')
    homepage_pic2 = homepage_pic1.resize ((300,375), Image.ANTIALIAS)
    homepage_pic3 = ImageTk.PhotoImage(homepage_pic2)
    pic_lb = tk.Label(frame4, image = homepage_pic3)
    pic_lb.pack()
    #_____________________________________________________
    
    #designing homepage ends here
#_______________________________________________________


#_______________________________________________________
#creating tk notebook with tabs to switch between pages
audio_nb=ttk.Notebook(window1)
audio_nb.pack(fill='both',expand=1)

Homepage_tab = tk.Frame(audio_nb,width=1250,height=750,bg='#FFBC8B')
English_tab = tk.Frame(audio_nb,width=1250,height=750,bg='#FFBC8B')
About_tab = tk.Frame(audio_nb,width=1250,height=750,bg='#FFBC8B')


audio_nb.add (Homepage_tab , text="Homepage")
audio_nb.add (English_tab , text="Sign lanuguage generator")
audio_nb.add (About_tab , text="About")

audio_nb.hide(1)
audio_nb.hide(2)
#_______________________________________________________

c_homepage=0 #this c is used for keeping track whether the person is visiting the home page for the first time 
#this is because if the user is visitng the homepage for the second time after already inputing his name then that info should only be dsplayed

homepage() #the first page which should always open is home page


    

window1.mainloop()