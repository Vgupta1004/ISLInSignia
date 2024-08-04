#_______
#importing all modules required throughout program
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
import speech_recognition as sr
import cv2 
import numpy as np 
import time
from PyDictionary import PyDictionary
from timeit import *
#_______
#defining the main window
window1=tk.Tk()
window1.title('Sign Language Generator')
window1.geometry('1250x700')
window1.iconbitmap('D:/Reliance school/Computer project/Danieledesantis-Audio-Video-Outline-Play.ico')
#_______
#_______
#function for taking name input in homepage
def EnterName():
    global user_name
    user_name=name_ent.get()
    global nameError_lb
    global wlcm_lb
    nameError_lb=tk.Label(frame3,text='*Please enter atleast one character for name',bg='#FFBC8B',fg='red',font=('Cambria',10))

    if len(user_name)<1:
        nameError_lb.place(x=200,y=5)
    else:               
        wlcm_lb=tk.Label(frame3,text='Welcome '+user_name+"!!!",font=('Cambria',20),bg='#FFBC8B')
        wlcm_lb.place(x=210,y=80)
        wlcm_lb2=tk.Label(frame3,text='Please check out the sign langauge generator tab...',font=('Cambria',20),bg='#FFBC8B')
        wlcm_lb2.place(x=60,y=130)
        nameError_lb.place_forget()
        
        name_ent['state']=tk.DISABLED
#_________________        
#function for quitting the program
def windestroy():
     tk.messagebox.showinfo("Quit","You have chosen to exit the program\nThank you for visiting!")
     window1.destroy()        
#_________________
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
#_______________
#function to play the hin video
def play_hin():
    global c
    global list1
    global text_mainwords
    global btn_play
    c=0 #to check if all words have been displayed
    for i in list1:
    
        c+=1
        call(i)
    if c==(len(list1)):
      # Closes all the frames 
      time.sleep(1)
      cv2.destroyAllWindows()
      text_mainwords.destroy()
      hin_audio_btn['state']=tk.NORMAL
      hin_audio_ent['state']=tk.NORMAL
      hin_audio_ent.delete('0','end')
      btn_play['state']=tk.DISABLED
      global c1
      c1=0
#_________________
#function to play the eng video
def play_eng():
    
    global c
    global list1
    global text_mainwords
    global btn_play
    c=0 #to check if all words have been displayed
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
      c1=0
      
#_________________
#function to bifurcate input hindi sentence into main words
def Submit_hin():
    global frame4
    global text_mainwords
    global btn_play
    global list1
    global sentences
    global hin_audio_ent
    global punctuation
    
    text = hin_audio_ent.get()
    if len(text)>0:
        hin_audio_btn['state']=tk.DISABLED
        hin_audio_ent['state']=tk.DISABLED
        list1=[]
        for i in text:
            if i in punctuation:
                text=text.replace(i,' ')
        words = text.split()
        text_mainwords = tk.Text(frame4,width=200,height=200,bg='#FFBC8B',font=('Cambria',14),borderwidth=0)
        text_mainwords.pack(padx=20,pady=50)
        c = 0
        for i in words:

            if i in list_hin:
                list1.append(i)
                text_mainwords.insert('insert','-->'+i+'\n')
                c = c + 1
            if c==0:
                    for k in i:
                        if k == '्':
                            continue
                        list1.append(k)
                        text_mainwords.insert('insert','-->'+k+'\n')
            c = 0
                        
        frame5=tk.Frame(Hindi_tab,bg='#FFBC8B')
        frame5.place(x=750,y=350,width=300,height=300)
        btn_play= tk.Button(frame5,text='Play the video',command=play_hin,font=('Cambria',28),bg='#F29062')
        btn_play.place(x=20,y=20)
#_________________
#function to bifurcate input english sentence into main words
def Submit_eng():
    global start
    global stop
    start= default_timer()
    global frame4
    global text_mainwords
    global btn_play
    global list1
    global sentences
    global eng_audio_ent
    global punctuation
    
    text = eng_audio_ent.get().lower()
    if len(text)>0:
        eng_audio_btn['state']=tk.DISABLED
        eng_audio_ent['state']=tk.DISABLED
        list1=[]
        for i in text:
            if i in punctuation:
                text=text.replace(i,' ')
        words = text.split()
        text_mainwords = tk.Text(frame4,width=200,height=200,bg='#FFBC8B',font=('Cambria',14),borderwidth=0)
        text_mainwords.pack(padx=20,pady=50)
        c = 0
        if text in sentences:
                    list1=[text]
                    for i in words:
                        text_mainwords.insert('insert','-->'+i+'\n')
        else:
            for i in words:
                if i in verbs:
                    c = 0
                    continue
                
                else:
                    if i in list_eng:
                        list1.append(i)
                        text_mainwords.insert('insert','-->'+i+'\n')
                        c = c + 1
                    else:
                        s = (PyDictionary().synonym(i))
                        for j in list_eng:
                            if s!=None:
                                if j in s:
                                    list1.append(j)
                                    text_mainwords.insert('insert','-->'+i+'\n')
                                    c = c + 1
                                    break
                                
                    if c==0:
                        for k in i:
                            list1.append(k)
                            text_mainwords.insert('insert','-->'+k+'\n')
                c = 0
                        
                    
        
        frame5=tk.Frame(English_tab,bg='#FFBC8B')
        frame5.place(x=750,y=350,width=300,height=300)
        btn_play= tk.Button(frame5,text='Play the video',command=play_eng,font=('Cambria',28),bg='#F29062')
        btn_play.place(x=20,y=20)
        stop=default_timer()
        print(stop-start)
    
#_____________
#function for receiving audio in English Sign lanuguage generator
def receive_audio_eng():
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
            eng_audio_ent.insert(0,speak_text)
      
                                 
            
            
        except sr.UnknownValueError: 
            tk.messagebox.showinfo('Input Error!!!',"Google Speech Recognition could not understand audio\nPlease enter again")
            #("Google Speech Recognition could not understand audio") 
      
        except sr.RequestError as e: 
           tk.messagebox.showinfo("Input Error!!!","Could not request results from Google Speech Recognition service; {0}".format(e))    
           #print("Could not request results from Google Speech Recognition service; {0}".format(e))
#_________________
#function for receiving audio in English Sign lanuguage generator
def receive_audio_hin():
    global c1
    global hin_audio_ent
    
    if c1==0:
        c1=1
    else:
        hin_audio_ent.delete('0','end')
        
    sample_rate = 48000
    chunk_size = 2048
    r = sr.Recognizer()
    
            
    with sr.Microphone(sample_rate = sample_rate,  chunk_size = chunk_size) as source:
        
        r.adjust_for_ambient_noise(source,duration=0.5)
        
        audio = r.listen(source) 
              
        try:          
            global speak_text
            global text                                                     
            speak_text = r.recognize_google(audio,language='hi-IN')   
            hin_audio_ent.insert(0,speak_text)
      
                                 
            
            
        except sr.UnknownValueError: 
            tk.messagebox.showinfo('इनपुट त्रुटि !!! ' ,   " गूगल भाषण मान्यता ऑडियो नहीं समझ सका। कृपया फिर से दर्ज करें")
            #("Google Speech Recognition could not understand audio") 
      
        except sr.RequestError as e: 
           tk.messagebox.showinfo('इनपुट त्रुटि !!! ' ," गूगल भाषण मान्यता सेवा से परिणाम का अनुरोध नहीं किया जा सका". format(e))    
           #print("Could not request results from Google Speech Recognition service; {0}".format(e))

#__________________
#designing Sign lanuguage generator page
def english_gen():
    
    audio_nb.select(1) #opening Sign lanuguage generator tab
    #_______
    #window heading
    frame1=tk.Frame(English_tab,bg='#FFBC8B')
    frame1.place(x=0,y=10,width=1500,height=120)
    heading_lb1= tk.Label(frame1,fg='black',bg='#FFBC8B',text='IN',font=('Gabriola',65,))
    heading_lb1.place(x=480,y=5)
    heading_lb2= tk.Label(frame1,fg='black',bg='#FFBC8B',text='SIGN',font=('Gabriola',68,'bold'))
    heading_lb2.place(x=550,y=0)
    heading_lb3= tk.Label(frame1,fg='black',bg='#FFBC8B',text='IA',font=('Gabriola',65,))
    heading_lb3.place(x=700,y=5)
    #_________________
    #displaying menu bar
    frame2=tk.Frame(English_tab,bg='#5B524A')
    frame2.place(x=0,y=150,width=1500,height=50)
    homepage_btn=tk.Button(frame2,text='Homepage',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=homepage)
    homepage_btn.pack(side='left')
    English_btn=tk.Button(frame2,text='English Sign lanuguage generator',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=english_gen)
    English_btn.pack(side='left')
    Hindi_btn=tk.Button(frame2,text='Hindi Sign lanuguage generator',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=hindi_gen)
    Hindi_btn.pack(side='left')
    About_btn=tk.Button(frame2,text='About',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=about_page)
    About_btn.pack(side='left')
    Quit_btn=tk.Button(frame2,text='Quit',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=windestroy)
    Quit_btn.pack(side='left')
    #_________________
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
    
    eng_audio_btn= tk.Button(frame3, image = english_pic3 ,command=receive_audio_eng, borderwidth = 0)
    eng_audio_btn.place(x=410,y=60)
    
    eng_submit = tk.Button(frame3, text = 'Submit',bg='#F29062',font=('Cambria',14),command = Submit_eng)
    eng_submit.place(x=460,y=60)
    #_______________
    #start displaying main words
    global list_eng
    global verbs
    global text
    global frame4
    global sentences
    global punctuation
    frame4=tk.Frame(English_tab,bg='#FFBC8B')
    frame4.place(x=60,y=220,width=550,height=400)
    list_eng= ["build", 'built','building', 'builds', 'easily','easy','grew','grow','growth','growing','grows','like','likes','liked','liking','object','objects','our','ours','us','power','powers','powerful','them','themselves','those','these', 'thing','things','1','2','3','4','5','6','7','8','9','0','how','hey','best','everyone','mobile','mobiles','what','when','where','which','who','why','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', "above", "absent", "across", "add", 'added','adding','adds',"address",'addresses', "advance", 'advanced','advances','advancing','advancement',"africa", "after", 'afterwards',"afternoon", "age",'aged','aging', 'ages',"air", "airport",'airports', "all", "ambulance",'ambulances', "among", 'amongst',"angry",'anger', "animal",'animals', "antartica", "apple",'apples', "april", "area", 'areas',"arm",'arms', "asia", "ask", 'asks','asked','asking',"august", "australia", "baby", 'babies',"back",'backwards', "bad", "badminton", "ball",'balls',"banana",'bananas', "bank", 'banking','banks',"bathroom",'bathrooms', "beat", 'beats', 'beating', "beautiful", 'beautifully', "behind", "bird", 'birds',"birthday", 'birthdays',"black", "blue", "boat", 'boating','boats',"book",'books', "born", 'birth', "boy",'boys', "brain", 'brains', "breeze", "bright", 'brighten', 'brightness', 'brightly', "brown", "buy", 'buys','buying','bought',"bye", 'goodbye',"call", 'calls','called','calling',"calm",'calming', "camera", 'cameras', "can", 'could', "cancel", 'cancelled', 'cancelling', "cap", 'caps', 'car', 'cars', "careless", 'carelessness', "carrot", 'carrots', "cash", 'money', "cat", 'cats', "chair", 'chairs', "change", 'changing', 'changed', 'changes', "chapter", 'chapters', "chicken", 'chickens', 'child', "children", "circle", 'circles', "clever", 'cleverness', 'cleverly', "clouds", 'cloud', "coffee", "cold", "college", 'colleges', "colour", 'colours', 'color', 'colors', 'colouring', 'coloured', "come",'comes', 'came', 'coming', "cone", 'cones', "continent", 'continents', "copy", 'copies', 'copied', 'copying', "cry", 'cries', 'cried', 'crying', "cube", 'cubes', 'cuboids', "cuboid", 'cylinders', "cylinder", "dance", 'dances', 'dancing', 'danced', "dark", "darkness", "date", "dates", "daughter","daughters", "day", "days", "deaf", "deafness", "december", "desk", "desks", "diabetes", "die", "dies", "died", "difficult", 'difficulty', "dinner", "dinners", "dirty", "doctor", "doctors", "document", "documents", "dog", "dogs", "dosa", "dosas", "doubt", "doubts", "doubtful", "earn", "earns", "earned", "earning", "earth", "east", "eat", "eats", "eating", "ate", "eaten", "echo", "echos", "echoed", "echoing", "eight", "elbow", "elbows", "email", "emails", "empty", "emptiness", "empties", "emptied", "emptying", "engineer", "engineers", "enjoy", "enjoying", "enjoys", "enjoyed", "europe", "evening", "evenings", "exam", "exams", "eye", "eyes", "face", "faces", "fail", "failing", "fails", "failed", "fall", "falling", "falls", "fell", "fallen", "false", "family", "families", "fat", "father", "father's","fathers", "fear", "fears", "feared", "fearful", "fearing", "february", "feel", "feeling", "feels", "felt", "film", "films", "fire", "fish", "fishes", "five", "floor", "floors", "four", "free", "frees", "freed", "friday", "friend", "friends", "fruit", "fruits", "game", "games", "gas", "gases", "gate", "gates", "girl", "girls", "glass", "glasses", "go", "going", "went", "gone", "goes", "goal", "goals", "goaling", 'goaled',"god", "gods", "golden", "good", "goodness", "grandfather", "grandfather's","grandfathers", "grandmother's","grandmother", "grandmothers", "grass", "green", "grey", "happy", "happiness",'happily', "he", "his", "hear", "hearing", "heard", "hears", "hello", "hi", "help", "helps", "helping", "helped", "hindi", "home", "homes", "hope", "hopes", "hopeful", "hoping", "hoped", "hot", "house", "houses", "husband", "husbands", "idli", "idlis", "in", "income", "incomes", "increase", "increasing", "increased", "increases", "india", "information", "insect", "insects", "interest", "interesting", "interested", "interests", "introduction", "intrductions", "jail", "jails", "january", "jeep", "jeeps", "july", "june", "lazy", "laziness", "lazily", "lemon", "lemons", "light", "lights", "lighting", "lighten", "lighted", "mango", "mangoes", "march", "me", "mix", "mixing", "mixed", "mixes", "monday", "month", "months", "monthly", "moon", "moons", "morning", "mornings", "mother","mother's", "mothers", "music", "musical", "musically", "my", "name", "names", "nice", "nicely", "night", "nights", "nine", "no", "not", "november", "october", "office", "offices", "one", "orange", "oranges", "pendulum", "pendulums", "phone", "phones", "pink", "please", "proud", "pride", "purple", "railway", "railways", "rain", "rains", "raining", "rained", "rainy", "rainbow", "rainbows", "rectangle", "rectangles", "red", "reflection", "reflections", "roti", "rotis", "sad", "sadness", "sadly", "sambhar", "saturday", "school", "schools", "september", "seven", "she", "her", "shop", "shops", "shopping", "shopped", "silver", "sister", "sisters", "six", "snow", "snowy", "snowing", "snowed", "snows", "son", "sons", "sorry", "sphere", "spheres", "square", "squares", "star", "stars", "starry", "strong", "strength", "study", "studies", "studying", "studied" , "summer", "summers", "sun", "sunday", "telephone", "telephones", "telescope", "telescopes", "thank", "thanks", "three", "thursday", "triangle", "triangles", "tuesday", "two", "wada", "wadas", "weather", "wednesday", "welcome", "welcomes", "welcoming", "welcomed", "white", "whitish", "wife", "wives", "wind", "winds", "windy", "winter", "winters", "work", "world", "x-ray", "x-rays", "year", 'years', "yellow", "yes", "you", "your", "yours", "yourself", "yourselves", "zero", "zoo", "zoos", 'atmosphere', 'eclipse', "eclipses", 'environment', 'equator', 'expert', "experts", 'hardworking', 'lie', "lies", "lying", "lied", 'map', "maps", 'north', 'patience', 'patient','radio', "radios", 'record', "records", 'right', 'sound', "sounds", 'south', 'television', "televisions", 'tv', "tvs", 'trouble', "troubles", "troubled", "troubling", 'trust', "trusted", "trusting", "trusts", 'universe', 'west', 'wrong', 'confident', "confidence", 'intelligent', "intellegence", 'knowledge', 'busy', 'brave', "bravery", 'tea', 'milk', 'heart', "hearts", 'talk', 'speak','speaking','speaks','spoke',"talking", "talks", "talked", 'stand', "standing", "stands", "stood", 'smell', "smelling", "smells", "smelt", 'sleep', "sleeping", "sleeps", "slept", 'sit', "sits", "sat", "sitting", 'see','seen', "seeing", "saw", "sees", 'run', "running", "runs", "ran", 'pain', "paining", "pains", "pained", 'hair', "hairs", 'nose', "noses", 'concentrate', "concentrated", "concentrating", "concentrates", 'old', 'young', 'battery', "batteries", 'electronics', "electronic", 'sofa', "sofas", 'clock', "clocks", 'window', "windows", 'umbrella', "umbrellas",'towel', "towels", 'plate', "plates", 'spoon', "spoons", 'flower', "flowers", 'tree', "trees", 'common', 'wet', "wetness", 'wear', "wears", "wearing", "wore", "worn", 'wash', "washes", "washed", "washing", 'wait', "waiting", "waited", "waits", 'visit', "visits", "visiting", "visited", 'swim', "swims", "swimming", "swam", 'stop', "stops", "stopped", "stopping", 'start', "starts", "starting", "started", 'whistle', "whistling", "whistles", "whistled", 'tabla', "tablas", 'stage', "stages", 'guitar', "guitars", 'sing', "sings", "singing", "sang", 'sculpture', "sculptures", 'magic', "magical", "magically", 'flute', "flutes", 'entertainment', 'drum', "drums", 'doll', "dolls", 'cinema', "cinemas", 'balloon', "balloons", 'art', "first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "zeroth", "open", "opened", "opens", "opening",'reddish','orangish','greenish','greenery','bluish','blackish','yellowish','pinkish', 'hai', 'kitabon','shoony','padhti' , 'ek','do','padta','padhta','teen','kitabi','chaar','paanch','chhah','saat','aath','nau','chhutiyon','chhutiyan','doston','panktiyan','parivaron','maa','mata','mummy','baithana','mitron','bol','rekhayen','mumma','matashri','pita','pitaji','papa','pitashri','saheliyan','baap','apna','apni','apne','avkash','aap','aapka','aapko','sthanon','kaksha','kar','karna','kariye','kare','karo','kahana','ho','kitab','kuchh','kripya','kaun','kya','hain','hun','sabko','saheli','sthan','shyampatt','kitabe','khada','khade','ganit','chahie','chhutti','jagah','jaaiye','jao','tum','tumko','tumhara','dost','namaskar','vigyan','lekhan','likho','likhe','likhna','naam','nikle','pankti','padhaanaa','nikalna','pathan','parivar','padhaai','paath','pustak','prarthana','padhna','band','baitha','likha','line','rekha','rihai','riha','bahi','ram','mein','mera','mitra','padhte','pustake','baithiye','baithi','baithe','baith','mat','bhid','bolna']    
    sentences = ['how are you','what is your name', 'i am fine', 'you are wrong', 'where is the police station', 'where is the hospital', 'where is the bathroom', 'where is the restroom', 'where is the washroom', 'where do you stay', "where do you live", 'when will we go', 'what is your moblie number', "what is your phone number", 'what is your job', 'what is your age', "how old are you", 'what date is it today', 'what is the problem', 'what are you doing', 'wait i am thinking', 'that is good', 'take care', 'stand up', 'sit down', 'shall i help you', 'can i help you', 'please call me later', 'please call an ambulance', "please call the ambulance", 'open the door', "open the doors", 'no smoking please', 'nice to meet you', 'let us go for lunch', 'keep quite', 'i have headache', 'i do not understand anything', 'i am tired', 'i am thinking', 'i am sorry', 'happy journey', 'good question', 'do not worry', 'be careful', 'are you sick', 'are you hungry', 'are you busy', 'all the best']
    verbs=['the','an','is','are','was','were','will','am','be','being','been','has','have','had','having','do','does','did', "may", "might", "must", "ought", "shall","should", 'would','to','and','or','on','of']
    punctuation=['!','@','#','$','%','^','&','*','(',')','_','-','+','=','~','`','{','[','}',']', '\\','|', ':',';', '"' , "'", ',' , '<', '.', '>' , '?', '/']
    lbl_display=tk.Label(frame4,text='The Main Words/Characters Are:',bg='#FFBC8B',font=('Cambria',20,'bold'))
    lbl_display.place(x=10,y=10)
#designing english_gen ends here
#_________________
#designing hindi sign language generator
def hindi_gen():
    audio_nb.select(2)  #opening Hindi tab
    #_________________
    #window heading
    frame1=tk.Frame(Hindi_tab,bg='#FFBC8B')
    frame1.place(x=0,y=10,width=1500,height=120)
    heading_lb1= tk.Label(frame1,fg='black',bg='#FFBC8B',text='IN',font=('Gabriola',65,))
    heading_lb1.place(x=480,y=5)
    heading_lb2= tk.Label(frame1,fg='black',bg='#FFBC8B',text='SIGN',font=('Gabriola',68,'bold'))
    heading_lb2.place(x=550,y=0)
    heading_lb3= tk.Label(frame1,fg='black',bg='#FFBC8B',text='IA',font=('Gabriola',65,))
    heading_lb3.place(x=700,y=5)
    #_______
    #displaying menu bar
    frame2=tk.Frame(Hindi_tab,bg='#5B524A')
    frame2.place(x=0,y=150,width=1500,height=50)
    homepage_btn=tk.Button(frame2,text='Homepage',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=homepage)
    homepage_btn.pack(side='left')
    English_btn=tk.Button(frame2,text='English Sign lanuguage generator',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=english_gen)
    English_btn.pack(side='left')
    Hindi_btn=tk.Button(frame2,text='Hindi Sign lanuguage generator',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=hindi_gen)
    Hindi_btn.pack(side='left')
    About_btn=tk.Button(frame2,text='About',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=about_page)
    About_btn.pack(side='left')
    Quit_btn=tk.Button(frame2,text='Quit',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=windestroy)
    Quit_btn.pack(side='left')
    #________
    #audio/text input form user either by typing in entry box or by using mic
    global hin_audio_ent
    global hin_audio_btn
    global hindi_pic1
    global hindi_pic2
    global hindi_pic3
    global frame3
    frame3=tk.Frame(Hindi_tab,bg='#FFBC8B')
    frame3.place(x=650,y=220,width=570,height=125)
    input_audio_lb=tk.Label(frame3,text='ऑडियो दर्ज करने के लिए माइक बटन पर दबाएँ  \n कृपया अपने माइक में बोलने से पहले 2  सेकंड प्रतीक्षा करें'      ,   bg='#FFBC8B',font=('Cambria',14,'bold'))
    input_audio_lb.place(x=10,y=10)
    
    hin_audio_ent=tk.Entry(frame3,font=16,borderwidth=1,relief='solid')
    hin_audio_ent.place(x=10,y=60,width=400,height=37)
    
    hindi_pic1=Image.open('images/mic1.png')
    hindi_pic2 = hindi_pic1.resize((35,35),Image.ANTIALIAS)
    hindi_pic3=ImageTk.PhotoImage(hindi_pic2)
    
    hin_audio_btn= tk.Button(frame3, image = hindi_pic3 ,command=receive_audio_hin, borderwidth = 0)
    hin_audio_btn.place(x=410,y=60)
    
    hin_submit = tk.Button(frame3, text = 'दर्ज करे',  bg='#F29062',font=('Cambria',14),command = Submit_hin)
    hin_submit.place(x=460,y=60)
    #_____________________
    global list_hin
    global verbs
    global text
    global frame4
    global sentences
    global punctuation
    frame4=tk.Frame(Hindi_tab,bg='#FFBC8B')
    frame4.place(x=60,y=220,width=550,height=400)
    punctuation=['!','@','#','$','%','^','&','*','(',')','_','-','+','=','~','`','{','[','}',']', '\\','|', ':',';', '"' , "'", ',' , '<', '.', '>' , '?', '/']
    list_hin=['०', 'शून्य', '१', 'एक', '२', 'दो', '३', 'तीन', '४', 'चार', '५', 'पांच', '६', 'छह', '७', 'सात', '८', 'आठ', '९', 'नौ', 'मां', 'माता', 'मम्मी', 'मम्मा', 'माताश्री', 'पिता' , 'बाप', 'पिताजी', 'पापा'  ,'पिताश्री',    'अ'  ,  ' आ'  ,   ' इ'   ,  ' ई' , ' उ'  , ' ऊ' , ' ए' , "ऐ", ' ओ' , ' औ' , "अं", "अः", ' ा' , ' ि' , ' ी' , ' ु' , ' ू' , ' े' , ' ै' , ' ो' , ' ौ' , ' ं' , ' ः'   , ' ृ' , "क", "ख", "ग", "घ", "ङ", "च", "छ", "ज", "झ", "ञ", "ट", "ठ", "ड", "ढ", "ण", "त", "थ", "द", "ध", "न", "प", "फ", "ब", "भ", "म", "य", "र", "ल", "व", "ह", "श", "ष", "स", "क्ष", "त्र", "ज्ञ", "अपना", "अपनी", "अपने", "अवकाश", "आप", "आपका", "आपको", "कक्षा", "कर", "करना", "करिये", "करे", "करो", "कहना", "किताब", "किताबें", "कुछ", "कृप्या", "कौन", "क्या", "खड़ा", "खड़े", "गणित", "चाहिए", "छुट्टी", "जगह", "जाइये", "जाओ", "तुम", "तुमको", "तुम्हारा", "दोस्त", "नमस्कार", "नाम", "निकले", "निकालना", "पंक्ति", "पठन", "पढ़ाना", "पढ़ाई", "परिवार", "पाठ", "पुस्तक", "पुस्तकें", "प्रार्थना", "पढ़ना", "बंद", "बही", "बैठ", "बैठा", "बैठिये", "बैठी", "बैठे", "बोलना", "भीड़", "मत", "मित्र", "में", "मेरा", "मैं", "राम", "रिहा", "रिहाई", "रेखा", "लाइन", "लिखा", "लिखना", "लिखे", "लिखो", "लेखन", "विज्ञान", "श्यामपट्ट", "सबको", "सहेली", "स्थान", "हिंदी", "हूं", "है", "हो" , "स्थानों" , "सहेलियां", "लाइने", "रेखाएं", "बोल", "मित्रों", "बैठना", "परिवारों", "पंक्तियां","दोस्तों", "छुट्टियां","छुट्टियों", "किताबी", "पढ़ता","किताबों","हैं" , "पढ़ती" ,"मुझे","पढ़ना","पढ़ते"]
    lbl_display=tk.Label(frame4,text='मुख्य शब्द / वर्ण हैं:'   ,    bg='#FFBC8B',font=('Cambria',20,'bold'))
    lbl_display.place(x=10,y=10)
#designing hindi_gen ends here
#_____________________
#_____________________
#designing about page
def about_page():
    audio_nb.select(3) #opening about page tab
    #______________________
    #window heading
    frame1=tk.Frame(About_tab,bg='#FFBC8B')
    frame1.place(x=0,y=10,width=1500,height=120)
    heading_lb1= tk.Label(frame1,fg='black',bg='#FFBC8B',text='IN',font=('Gabriola',65,))
    heading_lb1.place(x=480,y=5)
    heading_lb2= tk.Label(frame1,fg='black',bg='#FFBC8B',text='SIGN',font=('Gabriola',68,'bold'))
    heading_lb2.place(x=550,y=0)
    heading_lb3= tk.Label(frame1,fg='black',bg='#FFBC8B',text='IA',font=('Gabriola',65,))
    heading_lb3.place(x=700,y=5)
    #_________________
    #displaying menu bar
    frame2=tk.Frame(About_tab,bg='#5B524A')
    frame2.place(x=0,y=150,width=1500,height=50)
    homepage_btn=tk.Button(frame2,text='Homepage',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=homepage)
    homepage_btn.pack(side='left')
    English_btn=tk.Button(frame2,text='English Sign lanuguage generator',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=english_gen)
    English_btn.pack(side='left')
    Hindi_btn=tk.Button(frame2,text='Hindi Sign lanuguage generator',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=hindi_gen)
    Hindi_btn.pack(side='left')
    About_btn=tk.Button(frame2,text='About',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=about_page)
    About_btn.pack(side='left')
    Quit_btn=tk.Button(frame2,text='Quit',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=windestroy)
    Quit_btn.pack(side='left')
    #_________________
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
    #_______________
    
    global about_pic1
    global about_pic2
    
    frame4=tk.Frame(About_tab,bg='#FFBC8B',width=500,height=500)
    frame4.place(x=930,y=300)
    about_pic1=Image.open('images/about.jpg')
    about_pic2=ImageTk.PhotoImage(about_pic1)
    lbl= tk.Label(frame4, image = about_pic2)
    lbl.place(x=0,y=0)
#designing about page ends here
#__________________
#_________________
#function for designing the homepage
def homepage():
    audio_nb.select(0)
    #__________________
    #window heading
    frame1=tk.Frame(Homepage_tab,bg='#FFBC8B')
    frame1.place(x=0,y=10,width=1500,height=120)
    heading_lb1= tk.Label(frame1,fg='black',bg='#FFBC8B',text='IN',font=('Gabriola',65,))
    heading_lb1.place(x=480,y=5)
    heading_lb2= tk.Label(frame1,fg='black',bg='#FFBC8B',text='SIGN',font=('Gabriola',68,'bold'))
    heading_lb2.place(x=550,y=0)
    heading_lb3= tk.Label(frame1,fg='black',bg='#FFBC8B',text='IA',font=('Gabriola',65,))
    heading_lb3.place(x=700,y=5)
    #_________________
    #displaying menu bar
    frame2=tk.Frame(Homepage_tab,bg='#5B524A')
    frame2.place(x=0,y=150,width=1500,height=50)
    homepage_btn=tk.Button(frame2,text='Homepage',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=homepage)
    homepage_btn.pack(side='left')
    English_btn=tk.Button(frame2,text='English Sign lanuguage generator',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=english_gen)
    English_btn.pack(side='left')
    Hindi_btn=tk.Button(frame2,text='Hindi Sign lanuguage generator',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=hindi_gen)
    Hindi_btn.pack(side='left')
    About_btn=tk.Button(frame2,text='About',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=about_page)
    About_btn.pack(side='left')
    Quit_btn=tk.Button(frame2,text='Quit',bg='#5B524A',fg='#F29062',padx=10,borderwidth=0,font=('Cambria',14),command=windestroy)
    Quit_btn.pack(side='left')
    #__________________
    #name accepting
    global name_ent
    global frame3
    global name_btn
    global c_homepage
    frame3=tk.Frame(Homepage_tab,bg='#FFBC8B')
    frame3.place(x=5,y=280,width=700,height=250)
    name_lb=tk.Label(frame3,bg='#FFBC8B',text="Enter Your Name:",font=('Cambria',14))
    name_lb.place(x=15,y=30)
    name_ent=tk.Entry(frame3,width=30,font=('Cambria',14))
    name_ent.place(x=175,y=28)
    name_btn=tk.Button(frame3,text='Enter',bg='#F29062',font=('Cambria',14),command=EnterName)
    
    #checking if the user is visiting the home page for the first time
    if c_homepage==0:
        c_homepage=1
        
    elif c_homepage==1 and user_name=='':
        pass   
    else:
        name_btn['state']=tk.DISABLED
        wlcm_lb=tk.Label(frame3,text='Welcome '+user_name+"!!!",font=('Cambria',20),bg='#FFBC8B')
        wlcm_lb.place(x=210,y=80)
        wlcm_lb2=tk.Label(frame3,text='Please check out the sign langauge generator tab...',font=('Cambria',20),bg='#FFBC8B')
        wlcm_lb2.place(x=60,y=130)
        name_ent.insert(0,user_name)
        name_ent['state']=tk.DISABLED
        
    name_btn.place(x=525,y=22) 
    #________________
    
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
    #________________
    
    #designing homepage ends here
#_______________


#_________________
#creating tk notebook with tabs to switch between pages
audio_nb=ttk.Notebook(window1)
audio_nb.pack(fill='both',expand=1)

Homepage_tab = tk.Frame(audio_nb,width=1250,height=750,bg='#FFBC8B')
English_tab = tk.Frame(audio_nb,width=1250,height=750,bg='#FFBC8B')
Hindi_tab = tk.Frame(audio_nb,width=1250,height=750,bg='#FFBC8B')
About_tab = tk.Frame(audio_nb,width=1250,height=750,bg='#FFBC8B')


audio_nb.add (Homepage_tab , text="Homepage")
audio_nb.add (English_tab , text="English Sign lanuguage generator")
audio_nb.add (Hindi_tab, text='Hindi Sign Language generator')
audio_nb.add (About_tab , text="About")

audio_nb.hide(1)
audio_nb.hide(2)
audio_nb.hide(3)
#__________________
user_name=''  #for accepting the name of the user in the homepage
text=''
c1=0
c_homepage=0 #this c is used for keeping track whether the person is visiting the home page for the first time 
#this is because if the user is visitng the homepage for the second time after already inputing his name then that info should only be displayed

homepage() #the first page which should always open is home page


    

window1.mainloop()