from tkinter import *
from tkinter import filedialog
import tkinter
import model_train
import os
from PIL import ImageTk
from PIL import Image,ImageOps
top = tkinter.Tk()

def clicked():
    fil_path = filedialog.askopenfilename()
    val=model_train.func(fil_path)
    if val==0 :
        panel2 = Label(top, text='CALM', font=('Arial Bold', 20), background='#393e46',foreground='#ecf0f1')
        panel2.pack(side=BOTTOM)
        img1 = Image.open("assets/wave.png")
        img1 = img1.resize((150, 150), Image.ANTIALIAS)
        img1 = ImageTk.PhotoImage(img1)
        panel1 = Label(top, image=img1, borderwidth=0,background='#393e46')
        panel1.image=img1
        panel1.pack(side=BOTTOM)

    if val==1 :
        panel2 = Label(top, text='Happy', font=('Arial Bold', 20), background='#393e46',foreground='#ecf0f1')
        panel2.pack(side=BOTTOM)
        img1 = Image.open("assets/flower.png")
        img1 = img1.resize((150, 150), Image.ANTIALIAS)
        img1 = ImageTk.PhotoImage(img1)
        panel1 = Label(top, image=img1, borderwidth=0,background='#393e46')
        panel1.image=img1
        panel1.pack(side=BOTTOM)

    if val==2 :
        panel2 = Label(top, text='FEAR', font=('Arial Bold', 20), background='#393e46',foreground='#ecf0f1')
        panel2.pack(side=BOTTOM)
        img1 = Image.open("assets/fear.png")
        img1 = img1.resize((150, 150), Image.ANTIALIAS)
        img1 = ImageTk.PhotoImage(img1)
        panel1 = Label(top, image=img1, borderwidth=0,background='#393e46')
        panel1.image=img1
        panel1.pack(side=BOTTOM)

    if val==3 :
        panel2 = Label(top, text='DISGUST', font=('Arial Bold', 20), background='#393e46',foreground='#ecf0f1')
        panel2.pack(side=BOTTOM)
        img1 = Image.open("assets/emoji.png")
        img1 = img1.resize((150, 150), Image.ANTIALIAS)
        img1 = ImageTk.PhotoImage(img1)
        panel1 = Label(top, image=img1, borderwidth=0,background='#393e46')
        panel1.image=img1
        panel1.pack(side=BOTTOM)

top.configure(background="#393e46")
top.geometry('320x520')
top.configure(padx=20,pady=10)
img=Image.open("assets/logo.png")
img = img.resize((200, 200), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
panel = Label(top, image = img,borderwidth=0)

panel.pack(side=TOP)

if not os.path.exists('mymodel'):
    model_train.main()
lbl=Label(top,text="Developed by Sakar Singhal",background='#393e46',foreground='#ecf0f1')
lbl.config(font=('',8))
lbl.pack(side=BOTTOM)
btn=Button(top,text="Choose your file",command=clicked,borderwidth=0,background='#00adb5',highlightthickness=0,foreground='#ecf0f1',width=100,height=2)
btn.pack(side=BOTTOM,pady=30)

top.mainloop()