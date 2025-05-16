from tkinter import *
from tkinter import ttk
from PIL import Image ,ImageTk
import sqlite3
from tkinter import messagebox
import cv2

class aboutp:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x790+0+0")
        self.root.title("face Recognization System")

        title_lbl=Label(self.root,text="ABOUT STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="green",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        # Left Label frame
        Left_frame=LabelFrame(self.root,bd=2,relief=RIDGE,font=("times new roman",12,"bold"),fg="red")
        Left_frame.place(x=10,y=50,width=1550,height=790)

        img_left=Image.open(r"C:\Users\Arpit\Desktop\my project\my images\aboutp.jpg")
        img_left=img_left.resize((1550,790),)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f2lbl=Label(Left_frame,image=self.photoimg_left)
        f2lbl.place(x=10,y=60,width=1550,height=790)

    



if __name__=="_main_" : 
   root=Tk()
   obj=aboutp(root) 
   root.mainloop()      

