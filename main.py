from tkinter import *
import tkinter
from tkinter import ttk
import tkinter.messagebox
from PIL import Image ,ImageTk
from train import Train
from student import stu

from AboutP import aboutp
from Developer import developer_ji
from face_recognization import Face_Recognition

from help import Help
from time import sleep
import cv2
import numpy as np
from playsound import playsound
import  os

class Face_Recognization_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x790+0+0")
        self.root.title("face Recognization System")
    def reserve(self): 
        
        
        #first image
        img=Image.open(r"C:\Users\Arpit\Desktop\my project\my images\first.png")
        img=img.resize((500,130),)
        self.photoimg=ImageTk.PhotoImage(img)

        f1lbl=Label(self.root,image=self.photoimg)
        f1lbl.place(x=0,y=0)


         #SECOND image
        img1=Image.open(r"C:\Users\Arpit\Desktop\my project\my images\second.png")
        img1=img1.resize((500,130),)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f2lbl=Label(self.root,image=self.photoimg1)
        f2lbl.place(x=500,y=0)


         #Third image
        img2=Image.open(r"C:\Users\Arpit\Desktop\my project\my images\3.jpg")
        img2=img2.resize((530,130),)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f2lbl=Label(self.root,image=self.photoimg2)
        f2lbl.place(x=1000,y=0)


        #bgimage image
        img3=Image.open(r"C:\Users\Arpit\Desktop\my project\my images\bg_image.jpg")
        img3=img3.resize((1530,710),)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=-5,y=130,width=1550,height=710)


        title_lbl=Label(bg_img,text="FACE RECOGNIZATION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

      #STUDENT BUTTON
        img4=Image.open(r"C:\Users\Arpit\Desktop\my project\my images\student.jpeg")
        img4=img4.resize((230,220),)
        self.photoimg4=ImageTk.PhotoImage(img4)  

        b1=Button(bg_img,image=self.photoimg4,cursor="hand2",command=self.student_details)
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="red",command=self.student_details)
        b1_1.place(x=200,y=300,width=220,height=40)
 
 
      #DETECT FACE BUTTON
        img5=Image.open(r"C:\Users\Arpit\Desktop\my project\my images\face.jpg")
        img5=img5.resize((230,220),)
        self.photoimg5=ImageTk.PhotoImage(img5)  

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="red",command=self.face_data)
        b1_1.place(x=500,y=300,width=220,height=40)
 
 

      #About Project BUTTON
        img6=Image.open(r"C:\Users\Arpit\Desktop\my project\my images\attendance.jpg")
        img6=img6.resize((230,220),)
        self.photoimg6=ImageTk.PhotoImage(img6)  

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.About_Project)
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="About Project",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="red",command=self.About_Project)
        b1_1.place(x=800,y=300,width=220,height=40)


        #HELP FACE BUTTON
        img7=Image.open(r"C:\Users\Arpit\Desktop\my project\my images\help.jpg")
        img7=img7.resize((230,220),)
        self.photoimg7=ImageTk.PhotoImage(img7)  

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="red",command=self.help_data)
        b1_1.place(x=1100,y=300,width=220,height=40)
 

      #Train face BUTTON
        img8=Image.open(r"C:\Users\Arpit\Desktop\my project\my images\train.jpg")
        img8=img8.resize((230,220),)
        self.photoimg8=ImageTk.PhotoImage(img8)  

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="red",command=self.train_data)
        b1_1.place(x=200,y=580,width=220,height=40)
     

      #Photos face BUTTON
        img9=Image.open(r"C:\Users\Arpit\Desktop\my project\my images\Photos.jpg")
        img9=img9.resize((230,220),)
        self.photoimg9=ImageTk.PhotoImage(img9)  

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="red",command=self.open_img)
        b1_1.place(x=500,y=580,width=220,height=40)



       #Developer face BUTTON
        img10=Image.open(r"C:\Users\Arpit\Desktop\my project\my images\developer.jpg")
        img10=img10.resize((230,220),)
        self.photoimg10=ImageTk.PhotoImage(img10)  

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.About_Developer)
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="red",command=self.About_Developer)
        b1_1.place(x=800,y=580,width=220,height=40)



        #Exit face BUTTON
        img11=Image.open(r"C:\Users\Arpit\Desktop\my project\my images\exit.png")
        img11=img11.resize((230,220),)
        self.photoimg11=ImageTk.PhotoImage(img11)  

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="red",command=self.iExit)
        b1_1.place(x=1100,y=580,width=220,height=40)

    def open_img(self):
        os.startfile("data")  


    def iExit(self):
       self.iExit=tkinter.messagebox.askyesno("Face Recognization","Are you sure exit this project",parent=self.root)
       if self.iExit >0 :
          self.root.destroy()
       else:
          return         
        



  
 #=========================================== functions buttons=============================================   
    def student_details(self):
    
      self.new_window=Toplevel(self.root) 
      self.app=stu(self.new_window) 



    def train_data(self):
    
      self.new_window=Toplevel(self.root) 
      self.app=Train(self.new_window)  


    def face_data(self):
    
      self.new_window=Toplevel(self.root) 
      self.app=Face_Recognition(self.new_window)  


    def About_Project(self):
    
      self.new_window=Toplevel(self.root) 
      self.app=aboutp(self.new_window)  


    def About_Developer(self):
    
      self.new_window=Toplevel(self.root) 
      self.app=developer_ji(self.new_window)  
    

    def help_data(self):
       self.new_window=Toplevel(self.root) 
       self.app=Help(self.new_window)  
    
    
    
  

       

    

    
    

root=Tk()

obj=Face_Recognization_System(root) 
obj.reserve()

root.mainloop()      
