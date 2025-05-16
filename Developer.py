from tkinter import *
from tkinter import ttk
from PIL import Image ,ImageTk
import sqlite3
from tkinter import messagebox
import cv2

class developer_ji:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x790+0+0")
        self.root.title("face Recognization System")

        title_lbl=Label(self.root,text="Developer",font=("times new roman",35,"bold"),bg="green",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

         # Left Label frame
        Left_frame=LabelFrame(self.root,bd=2,relief=RIDGE,font=("times new roman",12,"bold"),fg="red")
        Left_frame.place(x=10,y=50,width=840,height=730)

        img_left=Image.open(r"C:\Users\Arpit\Desktop\my project\my images\salar.jpg")
        img_left=img_left.resize((750,730),)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f2lbl=Label(Left_frame,image=self.photoimg_left)
        f2lbl.place(x=10,y=60,width=840,height=730)


        # Right Label frame
        Right_frame=LabelFrame(self.root,bd=2,font=("times new roman",12,"bold"),fg="red")
        Right_frame.place(x=850,y=50,width=840,height=730)

        img_right=Image.open(r"C:\Users\Arpit\Desktop\my project\my images\Arp.jpg")
        img_right=img_right.resize((750,130),)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f1lbl=Label(Right_frame,image=self.photoimg_right)
        f1lbl.place(x=0,y=0,width=750,height=130)


        img_right1=Image.open(r"C:\Users\Arpit\Desktop\my project\my images\mu.jpg")
        img_right1=img_right1.resize((270,210),)
        self.photoimg_right1=ImageTk.PhotoImage(img_right1)

        f1lbl1=Label(Right_frame,image=self.photoimg_right1)
        f1lbl1.place(x=410,y=130,width=270,height=210)


        dep_label=Label(Right_frame,text="Name",font=("times new roman",20,"bold"),fg="black")
        dep_label.place(x=0,y=160)

        dep_label1=Label(Right_frame,text="Arpit",font=("times new roman",20,"bold"),fg="black")
        dep_label1.place(x=170,y=160)

if __name__=="_main_" : 
  root=Tk()
  obj=developer_ji(root)  
  root.mainloop()      

