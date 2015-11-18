#Program: Apple Tester
#By: Brad Turcott and Rich Cahill
#Date: 11/17/2015
import Tkinter
import tkMessageBox
import socket
from Tkinter import *
from PIL import Image, ImageTk

#initialize socket connection
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connected = False;

#Creates the window and labels it
top = Tkinter.Tk()
top.wm_title("Apple Tester")

#Sets the apple background image
bkg_img = Image.open('/home/bturcott/Pictures/apple_small.png')
tkimage = ImageTk.PhotoImage(bkg_img)
Tkinter.Label(top,image = tkimage).grid(row=0, column=3, rowspan=3, sticky=W+E+N+S, padx=5, pady=5)

#Label for IP Address
label1 = Label(top, text = "Enter Atlas IP Address:")
label1.grid(row=0, column=0, sticky=E+S)

#Textbox for IP Entry
entry1 = Entry(top, bd = 4)
entry1.grid(row=0, column=1, sticky=S)

#Label for IP Address
label2 = Label(top, text = "Enter String to Send:")
label2.grid(row=1, column=0, sticky=E+N)

#Textbox for IP Entry
entry2 = Entry(top, bd = 4)
entry2.grid(row=1, column=1, sticky=N)

def atlasConnect():
	host = entry1.get()
	client_socket.connect((host, 5000))
	connected = True
	tkMessageBox.showinfo("Atlas Connection Status", "You are connected.")

def sendString():
	totalsent = 0
	msg = entry2.get()
	if connected == True:
		MSGLEN = len(msg)
		while totalsent < MSGLEN:
			sent = client_socket.send(msg[totalsent:])
			if sent == 0:
				raise RuntimeError("socket connection broken")
			totalsent = totalsent + sent 
	tkMessageBox.showinfo("Atlas Connection Status", "You are not connected, please connect to Atlas.")

#Button for sending data
button1 = Tkinter.Button(top,text = "Send", command=sendString)
button1.grid(row=2,column=1, sticky=N+E)

#Button for connecting to the Atlas
button1 = Tkinter.Button(top,text = "Connect", command=atlasConnect)
button1.grid(row=2,column=1, sticky=N+W)

#labelframe.pack(fill="both", expand="yes")

#winlabel.pack()
#button1.pack()
top.mainloop()
