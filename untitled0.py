# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 09:02:01 2022

@author: shara
"""

import tkinter
import mysql.connector
window=tkinter.Tk()
window.title("CUSTOMER DETAILS")
obj=mysql.connector.connect(host='localhost',user='root',password='blyton',database='cs1_term2')
cursor=obj.cursor()

def insert():
    #to add record
    cid=t1.get()
    cname=t2.get()
    gender=t3.get()
    country=t4.get()
    print(cid,cname,gender,country)

tkinter.Label(text="ENTER CUSTOMER ID",font=('Arial Bold',10)).grid(column=0,row=0)
tkinter.Label(text="ENTER CUSTOMER NAME",font=('Arial Bold',10)).grid(column=0,row=1)
tkinter.Label(text="ENTER GENDER",font=('Arial Bold',10)).grid(column=0,row=2)
tkinter.Label(text="ENTER COUNTRY",font=('Arial Bold',10)).grid(column=0,row=3)


t1=tkinter.Entry(window,width=20).grid(column=1,row=0)
t2=tkinter.Entry(window,width=20).grid(column=1,row=1)
t3=tkinter.Entry(window,width=20).grid(column=1,row=2)
t4=tkinter.Entry(window,width=20).grid(column=1,row=3)


b1=tkinter.Button(window,text="ADD RECORD",bg="orange",fg="red",command=insert).grid(column=0,row=4)
b1=tkinter.Button(window,text="CLEAR",bg="orange",fg="red").grid(column=0,row=5)



window.mainloop()
