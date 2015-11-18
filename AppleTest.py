#Program: Apple Tester
#By: Brad Turcott and Rich Cahill
#Date: 11/17/2015
import Tkinter
import tkMessageBox
from Tkinter import *
from PIL import Image, ImageTk

#Creates the window and labels it
top = Tkinter.Tk()
top.wm_title("Apple Tester")
top.resizable(width=FALSE, height=FALSE)
top.geometry('{}x{}'.format(650,400))

#Sets the apple background image
bkg_img = Image.open('/home/bturcott/Pictures/Apple-logo.gif')
tkimage = ImageTk.PhotoImage(bkg_img)
Tkinter.Label(top,image = tkimage).place(x=0, y=0, relwidth=1, relheight=1)


label1 = Label(top, text = "Enter bits:")
label1.pack(side=LEFT)

entry1 = Entry(top, bd = 4)
entry1.pack(side=LEFT)

def sendBits():
	tkMessageBox.showinfo("Bit Report", "You've sent some bits")

button1 = Tkinter.Button(top,text = "Send Bits", command=sendBits)
button1.pack(side=LEFT)

#labelframe.pack(fill="both", expand="yes")

#winlabel.pack()
#button1.pack()
top.mainloop()
