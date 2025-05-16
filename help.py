from tkinter import *
from tkinter import ttk
from PIL import Image ,ImageTk
import sqlite3
from tkinter import messagebox
import cv2

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x790+0+0")
        self.root.title("face Recognization System")

        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="green",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        img_left=Image.open(r"C:\Users\Arpit\Desktop\my project\my images\helpvali.jpg")
        img_left=img_left.resize((1550,790),)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f2lbl=Label(self.root,image=self.photoimg_left)
        f2lbl.place(x=10,y=60,width=1540,height=790)
        dep_label1=Label(f2lbl,text="arpittrivedi715@gmail.com",font=("times new roman",20,"bold"),fg="black")
        dep_label1.place(x=650,y=420)


if __name__=="_main_" :         
  root=Tk()
  obj=Help(root) 
  root.mainloop()      
