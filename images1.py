from tkinter import *
from PIL import ImageTk,Image
window1=Tk()
window1.title('learn to code at Codemy.com')

window1.iconbitmap('C:\\Users\\shara\\Downloads\\Danieledesantis-Audio-Video-Outline-Play.ico')

my_img1= ImageTk.PhotoImage(Image.open("images\\boy.png"))
my_img2= ImageTk.PhotoImage(Image.open("images\\mic.png"))
my_img3= ImageTk.PhotoImage(Image.open("images\\flowers.png"))

image_list=[my_img1,my_img2]

my_label=Label(image =my_img1)
my_label.grid(row=0,column=0,columnspan=3)

def destroy():
   window1.destroy()

def back(image_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label= Label(window1,image = image_list[image_number - 1])
    button_forward = Button(window1 , text='>>',command=lambda: forward(image_number+1))
    button_back = Button(window1, text='<<', command=lambda: back(image_number-1))
    if image_number==1:
        button_back=Button(window1,text='<<',state=DISABLED)
    button_forward.grid( row = 1 , column = 2)
    button_back.grid( row = 1 , column = 0)
    my_label.grid(row = 0 , column = 0 ,columnspan=3 )
    
def forward(image_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label= Label(window1,image = image_list[image_number - 1])
    button_forward = Button(window1 , text='>>',command=lambda: forward(image_number+1))
    button_back = Button(window1, text='<<', command=lambda: back(image_number-1))
    if image_number==2:
        button_forward = Button(window1, text='>>',state=DISABLED)
    
    
    button_forward.grid( row = 1 , column = 2)
    button_back.grid( row = 1 , column = 0)
    my_label.grid(row = 0 , column = 0 ,columnspan=3 )

    
    
button_back=Button(window1 ,text='<<',command=back,state=DISABLED)
button_exit=Button(window1,text='EXIT PROGRAM',command=destroy)
button_forward=Button(window1,text='>>',command= lambda: forward(2))

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)





window1.mainloop()
