    
import tkinter as tk 
import tkinter.messagebox
import mysql.connector
import time
#logging in to your account
def login():
    global name1_ent
    global pswd1_ent
    global login_window
    sql_obj1=mysql.connector.connect(host='bwqwqvenmbwqhzwutgu6-mysql.services.clever-cloud.com',user='u7bizpwgzah61bgv',password='UKX0nnX3eNDTj86DEOTT',database='bwqwqvenmbwqhzwutgu6')
    cursor=sql_obj1.cursor()
    username=name1_ent.get()
    password=pswd1_ent.get()
    cursor.execute('select username from user')
    rs1=cursor.fetchall()
    
    cursor.execute('select pswd from user')
    rs2=cursor.fetchall()
    
    if (username,) in rs1:
        if (password,)==rs2[rs1.index((username,))]:
            tkinter.messagebox.showinfo("Succesful Login!","You have been logged in successfully!")
            time.sleep(1)
            login_window.destroy()
        else:
            tkinter.messagebox.showinfo("Error!","You have entered the wrong password.\nPlease enter the password again!")
            pswd1_ent.delete('0','end')
    else:
        tkinter.messagebox.showinfo("Error!","The user does not exist.\nPlease enter again!")
        name1_ent.delete('0','end')
        pswd1_ent.delete('0','end')

    sql_obj1.close()
    
    
    
#making the account using sign up page   
def sign():
    global name2_ent
    global pswd2_ent
    global signup_window
    sql_obj2=mysql.connector.connect(host='bwqwqvenmbwqhzwutgu6-mysql.services.clever-cloud.com',user='u7bizpwgzah61bgv',password='UKX0nnX3eNDTj86DEOTT',database='bwqwqvenmbwqhzwutgu6')
    cursor=sql_obj2.cursor()
    username=name2_ent.get()
    password=pswd2_ent.get()
    cursor.execute('select username from user')
    rs1=cursor.fetchall()
    print(rs1)
    cursor.execute('select pswd from user')
    rs2=cursor.fetchall()
    print(rs2)
    cursor.execute('select count(*) from user')
    rs3=cursor.fetchall()
    print(rs3)
    c=rs3[0][0] 
    print (c)#this helps to identify which user number are we catering to
    if (username,) in rs1:
              tkinter.messagebox.showinfo("Error!",f"Sorry!The username {username} is not available\nPlease Enter Again!",parent=signup_window)
              name2_ent.delete('0','end')
              pswd2_ent.delete('0','end')
    elif len(username)<1 or len(username)>20:
              tkinter.messagebox.showinfo("Error!","The username should be atleast 1 and atmost 20 characters long.\nPlease Enter Again!")
              name2_ent.delete('0','end')
              pswd2_ent.delete('0','end')
    elif len(password)<8 or len(password)>20:
              tkinter.messagebox.showinfo("Error!","The password should be atleast 8 and atmost 20 characters long.\nPlease Enter Again!")
              name2_ent.delete('0','end')
              pswd2_ent.delete('0','end')
    else:
        cursor.execute(f"insert into user(user_id,username,pswd) values({c+1},'{username}','{password}')")
        sql_obj2.commit()
        sql_obj2.close()
        tkinter.messagebox.showinfo("Successful Signup!","Account successfully created!\nTaking you back to login page")
        signup_window.destroy()
    
#create the signup page    
def signup(): 
    global signup_window
    signup_window=tk.Tk()
    signup_window.title('Insignia Sign-Up')
    signup_window.geometry('1250x700')
    signup_window.iconbitmap('D:/Reliance school/Computer project/extra/Danieledesantis-Audio-Video-Outline-Play.ico')
    
    #window heading
    frame1=tk.Frame(signup_window,bg='#FFBC8B')
    frame1.place(x=0,y=0,width=1500,height=150)
    heading_lb1= tk.Label(frame1,fg='black',bg='#FFBC8B',text='IN',font=('Gabriola',65,))
    heading_lb1.place(x=480,y=5)
    heading_lb2= tk.Label(frame1,fg='black',bg='#FFBC8B',text='SIGN',font=('Gabriola',68,'bold'))
    heading_lb2.place(x=550,y=0)
    heading_lb3= tk.Label(frame1,fg='black',bg='#FFBC8B',text='IA',font=('Gabriola',65,))
    heading_lb3.place(x=700,y=5)

    #menu bar
    frame2=tk.Frame(signup_window,bg='#5B524A')
    frame2.place(x=0,y=150,width=1500,height=60)
    login_lb=tk.Label(frame2,bg='#5B524A',fg='#F29062',text='Sign-Up Page',font=('Cambria',25))
    login_lb.place(x=530,y=10)
    
    frame3=tk.Frame(signup_window,bg='#FFBC8B')
    frame3.place(x=0,y=210,width=1500,height=1200)
    
    name_lb=tk.Label(frame3,bg='#FFBC8B',text='Enter Username:',font=('Cambria',20))
    name_lb.place(x=200,y=30)
    pswd_lb=tk.Label(frame3,bg='#FFBC8B',text='Enter Password: (Must be atleast 8 characters long)',font=('Cambria',20))
    pswd_lb.place(x=200,y=150)
    
    global name2_ent
    global pswd2_ent
    name2_ent=tk.Entry(frame3,width=30,font=('Cambria',20))
    name2_ent.place(x=200,y=90)
    pswd2_ent=tk.Entry(frame3,width=30,font=('Cambria',20))
    pswd2_ent.place(x=200,y=200)
    
    login1_btn=tk.Button(frame3,bg='#F29062',text='Sign Up',font=('Cambria',20),command=sign)
    login1_btn.place(x=600,y=300)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

login_window=tk.Tk()
login_window.title('Insignia')
login_window.geometry('1250x700')
login_window.iconbitmap('D:/Reliance school/Computer project/extra/Danieledesantis-Audio-Video-Outline-Play.ico')

#window heading
frame1=tk.Frame(login_window,bg='#FFBC8B')
frame1.place(x=0,y=0,width=1500,height=150)
heading_lb1= tk.Label(frame1,fg='black',bg='#FFBC8B',text='IN',font=('Gabriola',65,))
heading_lb1.place(x=480,y=5)
heading_lb2= tk.Label(frame1,fg='black',bg='#FFBC8B',text='SIGN',font=('Gabriola',68,'bold'))
heading_lb2.place(x=550,y=0)
heading_lb3= tk.Label(frame1,fg='black',bg='#FFBC8B',text='IA',font=('Gabriola',65,))
heading_lb3.place(x=700,y=5)

#menu bar
frame2=tk.Frame(login_window,bg='#5B524A')
frame2.place(x=0,y=150,width=1500,height=60)
login_lb=tk.Label(frame2,bg='#5B524A',fg='#F29062',text='Login Page',font=('Cambria',25))
login_lb.place(x=530,y=10)

#login part
frame3=tk.Frame(login_window,bg='#FFBC8B')
frame3.place(x=0,y=210,width=1500,height=1200)
wc_lb=tk.Label(frame3,bg='#FFBC8B',text='Welcome to Insignia!',font=('Cambria italic',35))
wc_lb.place(x=430,y=20)
name1_lb=tk.Label(frame3,bg='#FFBC8B',text='Enter Username:',font=('Cambria',20))
name1_lb.place(x=200,y=120)
pswd1_lb=tk.Label(frame3,bg='#FFBC8B',text='Enter Password:',font=('Cambria',20))
pswd1_lb.place(x=200,y=180)
name1_ent=tk.Entry(frame3,width=30,font=('Cambria',20))
name1_ent.place(x=430,y=120)
pswd1_ent=tk.Entry(frame3,width=30,font=('Cambria',20))
pswd1_ent.place(x=430,y=180)

login_btn=tk.Button(frame3,bg='#F29062',text='Login',font=('Cambria',20),command=login)
login_btn.place(x=600,y=240)

signup_lb=tk.Label(frame3,bg='#FFBC8B',text='No Account?',font=('Cambria',14))
signup_lb.place(x=490,y=325)
sign_btn=tk.Button(frame3,bg='#FFBC8B',fg='#0048BA',relief='flat',text='Create One Now!',font=('Cambria',14),command=signup)
sign_btn.place(x=600,y=320)


login_window.mainloop()