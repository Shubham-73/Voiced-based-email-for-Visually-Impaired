import tkinter as tk
from tkinter import Message ,Text
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import tkinter.messagebox as tm
import sqlite3

from tkinter import filedialog
import tkinter.messagebox as tm
from tkinter import ttk
import Register as r
import time


from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import random
import os
import time



uname=""
password=""
name=""
email=""
epassword=""
mobile=""
n=0

# function to be called when button-2 of mouse is pressed 
def pressed2(event): 
	print('Button-2 pressed at x = % d, y = % d'%(event.x, event.y)) 

# function to be called when button-3 of mouse is pressed 
def pressed3(event):
	global n
	print('Button-3 pressed at x = % d, y = % d'%(event.x, event.y)) 
	print("usename",uname)
	print("password",password)
	print("name",name)
	print("email",email)
	print("epassword",epassword)
	print("mobile",mobile)
	conn= sqlite3.connect("Email")
	cmd="SELECT * FROM login WHERE username='"+str(uname)+"'"
	print(cmd)
	cursor=conn.execute(cmd)
	isRecordExist=0
	for row in cursor:
		isRecordExist=1
	if (isRecordExist==1):
		tts = gTTS(text="Username Already Exists", lang='en')
		ran=random.randint(0,999)
		ttsname=("name"+str(ran)+".mp3")
		tts.save(ttsname)
		playsound(ttsname)
		os.remove(ttsname)

		
	else:
		print("insert")
		cmd="INSERT INTO login Values('"+str(uname)+"','"+str(password)+"','"+str(name)+"','"+str(email)+"','"+str(epassword)+"','"+str(mobile)+"')"
		print(cmd)
		tts = gTTS(text="Inserted Successfully", lang='en')
		ran=random.randint(0,999)
		ttsname=("name"+str(ran)+".mp3")
		tts.save(ttsname)
		playsound(ttsname)
		os.remove(ttsname)
		n=1
		
	conn.execute(cmd)
	conn.commit()
	conn.close() 
	


def process():
	global uname,password,name,email,epassword,mobile
	bgcolor="#ECFDB0"
	fgcolor="black"
	window = tk.Tk()
	window.title("Voice based Email System")
	window.geometry('1280x720')
	window.configure(background=bgcolor)
	window.grid_rowconfigure(0, weight=1)
	window.grid_columnconfigure(0, weight=1)
	window.bind('<Button-2>', pressed2) 
	window.bind('<Button-3>', pressed3) 

		
	message1 = tk.Label(window, text="Voice based Email System" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=3,font=('times', 30, 'italic bold underline')) 
	message1.place(x=100, y=10)		
    
	
	lbl = tk.Label(window, text="User Name",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl.place(x=300, y=250)
	
	txt = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt.place(x=600, y=265)

	lbl1 = tk.Label(window, text="Password",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl1.place(x=300, y=300)
	
	txt1 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt1.place(x=600, y=315)

	lbl2 = tk.Label(window, text="Name",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl2.place(x=300, y=350)
	
	txt2 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt2.place(x=600, y=365)

	lbl3 = tk.Label(window, text="Email",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl3.place(x=300, y=400)
	
	txt3 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt3.place(x=600, y=415)


	lbl4 = tk.Label(window, text="Password",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl4.place(x=300, y=450)
	
	txt4 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt4.place(x=600, y=465)
	
	lbl5 = tk.Label(window, text="Mobile",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl5.place(x=300, y=500)

	txt5 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt5.place(x=600, y=515)


	sym,sym1,sym2,sym3,sym4,sym5=r.process()
		
	txt.insert('end',sym)
	txt1.insert('end',sym1)
	txt2.insert('end',sym2)
	txt3.insert('end',sym3)
	txt4.insert('end',sym4)
	txt5.insert('end',sym5)


	uname=txt.get()
	password=txt1.get()
	name=txt2.get()
	email=txt3.get()
	epassword=txt4.get()
	mobile=txt5.get()
	
	
	window.update()
	
	while True:
		time.sleep( 1 )
		uname=txt.get()
		password=txt1.get()
		name=txt2.get()
		email=txt3.get()
		epassword=txt4.get()
		mobile=txt5.get()

		print(uname)
		print(password)
		print(name)
		print(email)
		print(epassword)
		print(mobile)
		print(n)

		if n==1:
			window.destroy()
			break
		window.update()

	window.mainloop()
	
