import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as scrtext
import logging
import threading
import subprocess
import time
import json
import asyncio
import os

def massrun(name):
	print('thread {}', name)

def Startmasscan():
	print('masscan started .....')
	ranges = txt.get("0.0", tk.END).splitlines()
	massp = massporttext.get()
	massrt = massratetext.get()
	for line in ranges:
		print(line)
		p1 = subprocess.Popen(['masscan', "-p" ,  massp , "--rate" , massrt , "--range" , line , "-oG" , line + ".json"], stdout=subprocess.PIPE)
		(output , err) = p1.communicate()
		p1.wait()
		print('{}\n{}'.format(output,err))
		servers = []
		if os.path.getsize(line + '.json') <= 0:
			continue
		with open(line + '.json', 'r') as f:
			texta = f.read()
			print(texta)
		servers.append(texta)
	print(servers)
	print('masscan finished .....')

def cleanGui():
	txt.delete('0.0', END)
	massporttext.set('')
	massratetext.set('')
	print('Cleanning')

def cleanranges():
	txt.delete('0.0', END)
	print('Ranges Cleaned')

mass = tk.Tk()
mass.title('masscan-GUI By Ghost5egy')
mass.minsize(400,600)
mass.eval('tk::PlaceWindow . center')
bottomframe = Frame(mass)
bottomframe.pack( side = BOTTOM , fill="x")
txt = scrtext.ScrolledText(mass, width=40,height=20,undo=True)
txt['font'] = ('consolas', '12')
txt.pack(expand=True, fill='both')
txt.insert(tk.INSERT,'192.168.1.0/24\n192.168.0.0/24\n10.0.0.1/8\n10.12.27.0/16')
massporttext = tk.StringVar()
massporttext.set('3389')
massport = ttk.Entry(bottomframe, width = 15, justify='center' , textvariable = massporttext)
massport.pack(expand=True, fill="x")
massratetext = tk.StringVar()
massratetext.set('10000')
massrate = ttk.Entry(bottomframe, width = 15, justify='center' ,textvariable = massratetext)
massrate.pack(expand=True, fill="x")
clearbtn = tk.Button(bottomframe, text ="Clear All", command = cleanGui)
clearbtn.pack(expand=True, fill="x")
clrngsbtn = tk.Button(bottomframe, text ="Clear Ranges", command = cleanranges)
clrngsbtn.pack(expand=True, fill="x")
scanbtn = tk.Button(bottomframe, text ="Scan", command = Startmasscan)
scanbtn.pack(expand=True, fill="x")
lbldata = tk.Label(bottomframe, text ="The Results will be saved in results.txt\nGhost5egy")
lbldata.pack(expand=True, fill="x")
mass.mainloop()
