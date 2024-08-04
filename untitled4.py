#to run  Miscellaneous for dictionary
def Miscellaneous():
        window8=tk.Tk()
        window8.title('Miscellaneous')
        window8.geometry('1250x700')
        window8.iconbitmap('D:/Reliance school/Computer project/Danieledesantis-Audio-Video-Outline-Play.ico')
        global frame_Miscellaneous
        frame_Miscellaneous=tk.Frame(window8,bg="#FFBC8B")
        frame_Miscellaneous.place(x=0,y=0,width=1550,height=700)
        
        global list_Miscellaneous
        list_Miscellaneous=['chapter', 'college', 'exam', 'desk', 'book', 'absent', 'knowledge']
        global x1
        global y1
        x1 = 50
        y1 = 75     
        global count
        global row
        count = 0
        row = 1
                
            
        for i in list_Miscellaneous:
                    count+=1
                    display_Miscellaneous(i)
                    if count%3==0:
                        row+=1
                        y1+=150
                        if row==3:
                            x1 = 200
                        else:
                            x1 = 50
                    else:
                        x1+=220
        global label_Miscellaneous1
        label_Miscellaneous1=tk.Label(frame_Miscellaneous,text= 'Choose the word whose sign',bg="#FFBC8B",font=('Lucida Calligraphy',20))
        label_Miscellaneous1.place(x=750,y=40)
        global label_Miscellaneous2
        label_Miscellaneous2=tk.Label(frame_Miscellaneous,text= 'language you want to learn',bg="#FFBC8B",font=('Lucida Calligraphy',20))
        label_Miscellaneous2.place(x=750,y=90)
    

def call32(I):
   
    # Create a VideoCapture Miscellaneous and read from input file 
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
        cv2.moveWindow('Frame',900,200)
        cv2.imshow('Frame', frame) 
       
        # Press Q on keyboard to  exit 
        if cv2.waitKey(25) & 0xFF == ord('q'): 
            break
       
      # Break the loop 
      else:  
        break
       
    # When everything done, release  
    # the video capture Miscellaneous 
    cap.release() 


    
    
def which_button(button_press):
        call32(button_press)
        time.sleep(1)
        cv2.destroyAllWindows()
        
def display_Miscellaneous(i):
        global frame_Miscellaneous
        global element_Miscellaneous
        global x1
        global y1
        element_Miscellaneous = tk.Button(frame_Miscellaneous, text = i, command = lambda m=i:which_button(m), bg='#F29062',font=('Cambria',30))
        element_Miscellaneous.place(x = x1,y = y1,width=200)
        
        
        
        
        
        Miscellaneous_btn=tk.Button(frame3,text='Miscellaneous',bg='#F29062',font=('Cambria',20),command=Miscellaneous)
        Miscellaneous_btn.place(x=160,y=80)