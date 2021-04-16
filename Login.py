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
import LoginPage as LP

from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import random
import os
import time
import Start as s

    
uname=""
password=""
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
	conn= sqlite3.connect("Email")
	cmd="SELECT username,password FROM login WHERE username='"+str(uname)+"' and password='"+str(password)+"'"
	print(cmd)
	cursor=conn.execute(cmd)
	#print(cursor.fetchall())
	isRecordExist=0
	for row in cursor:
		isRecordExist=1
	if(isRecordExist==1):
		#tm.showinfo("Input", "Lgoin Succesfully")
		tts = gTTS(text="Logged in Succesfully", lang='en')
		ran=random.randint(0,999)
		ttsname=("name"+str(ran)+".mp3")
		tts.save(ttsname)
		playsound(ttsname)
		os.remove(ttsname)
		n=1
		
	else:
		tts = gTTS(text="Check Username and Password", lang='en')
		ran=random.randint(0,999)
		ttsname=("name"+str(ran)+".mp3")
		tts.save(ttsname)
		playsound(ttsname)
		os.remove(ttsname)
	
    	
    



def process():
	global uname,password,n	
	bgcolor="#ECFDB0"
	fgcolor="black"
	window = tk.Tk()
	window.title("Voice based Email System")
	window.geometry('1280x720')
	window.configure(background=bgcolor)
	#window.attributes('-fullscreen', True)

	window.grid_rowconfigure(0, weight=1)
	window.grid_columnconfigure(0, weight=1)
	window.bind('<Button-2>', pressed2) 
	window.bind('<Button-3>', pressed3) 

		
	message1 = tk.Label(window, text="Voice based Email System" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=3,font=('times', 30, 'italic bold underline')) 
	message1.place(x=100, y=10)

   
	
	lbl = tk.Label(window, text="User Name",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl.place(x=300, y=300)
	
	txt = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt.place(x=600, y=315)

	lbl1 = tk.Label(window, text="Password",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl1.place(x=300, y=400)
	
	txt1 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt1.place(x=600, y=415)


	sym,sym1=LP.process()

	txt.insert('end',sym)
	txt1.insert('end',sym1)

	uname=txt.get()
	password=txt1.get()

	window.update()
	
	while True:
		time.sleep( 1 )
		uname=txt.get()
		password=txt1.get()
		print(uname)
		print(password)
		print(n)
		if n==1:
			window.destroy()
			s.process(uname)
			break
		window.update()

	#window.after(30000, window.destroy)
	window.mainloop()
	



