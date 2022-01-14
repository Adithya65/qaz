import tkinter as tk
import mysql.connector 
from random import *
from tkinter import *
import datetime
date_t=datetime.datetime.now()
def signup_submit():
    pass
     

def login(w,a):
    print("success")
    
def signup():
    top1 = tk.Tk()
    top1.geometry("1000x1000") 
    top1.configure(bg= "brown" )
     
     
    canvas2 = Canvas( top1, width = 400,
                    height = 400)
    bg = PhotoImage(file = "trian_PNG16634 (1).png")
    
    canvas2.pack(fill = "both", expand = True)
    
    # Display image
    ##canvas2.create_image(300 , 300 , image = bg, anchor = "nw")
    
    # Add Text
    canvas2.create_text( 500 , 10 , text = "Signup")
    
    canvas2.create_text( 100 , 50 , text = "Name")
    name=tk.Entry(top1, width= 40)
    ent1_canvas2 = canvas2.create_window( 140, 40, 
                                       anchor = "nw",
                                       window =name)
    canvas2.create_text( 100 , 90 , text = "Contact no")
    cno=tk.Entry(top1, width= 40)
    ent2_canvas2 = canvas2.create_window( 140, 80, 
                                       anchor = "nw",
                                       window =cno)
    canvas2.create_text( 100 , 130 , text = "mail id")
    mid=tk.Entry(top1, width= 40)
    ent3_canvas2 = canvas2.create_window( 140, 120, 
                                       anchor = "nw",
                                       window =mid)
    canvas2.create_text( 100 , 170 , text = "password")
    
    psd1=tk.Entry(top1, width= 40)
    ent4_canvas2 = canvas2.create_window( 140, 160, 
                                       anchor = "nw",
                                       window =psd1)   
    sub1=tk.Button(top1,text="Signup",command=signup_submit)
    button4_canvas2 = canvas2.create_window( 180, 200, 
                                       anchor = "nw",
                                       window = sub1)
    
     
    top1.mainloop()       
top = tk.Tk()
top.geometry("1000x1000") 
top.configure(bg='blue')
bg = PhotoImage(file = "trian_PNG16634 (1).png")
canvas1 = Canvas( top, width = 400,
                 height = 400)
  
canvas1.pack(fill = "both", expand = True)
  
# Display image
canvas1.create_image(300 , 300 , image = bg, 
                     anchor = "nw")
  
# Add Text
canvas1.create_text( 500 , 10 , text = "Welcome")

canvas1.create_text( 500 , 50 , text = "Enter your details")
userid= tk.Entry(top, width= 40)
w=userid.get()
psw= tk.Entry(top, width= 40)
a=psw.get()
B = tk.Button(top, text ="login", command=lambda:login(w,a))
canvas1.create_text( 60 , 110 , text = "User Id")
canvas1.create_text( 60 , 150 , text = "password")
k=tk.Button(top,text="Signup",command=signup)
button1_canvas = canvas1.create_window( 100, 100, 
                                       anchor = "nw",
                                       window = userid)
button4_canvas = canvas1.create_window( 150, 180, 
                                       anchor = "nw",
                                       window = k)
  
button2_canvas = canvas1.create_window( 100, 140,
                                       anchor = "nw",
                                       window =psw )
  
button3_canvas = canvas1.create_window( 100, 180, anchor = "nw",
                                       window = B)
 
"""  B = tk.Button(top, text ="Right Arm", command = rightarm)
n=tk.Button(top,text="pushup",command=pushup)
z=tk.Button(top,text="vid",command=playvid)
m.pack()"""

 
top.mainloop()
 