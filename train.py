from tkinter import *
from tkinter import ttk
from PIL import Image ,ImageTk
import sqlite3
from tkinter import messagebox
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x790+0+0")
        self.root.title("face Recognization System")

        title_lbl=Label(self.root,text="Train Data Set",font=("times new roman",35,"bold"),bg="green",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        img_top=Image.open(r"C:\Users\Arpit\Desktop\my project\my images\salar3.jpg")
        img_top=img_top.resize((1530,330),)
        
        self.photoimg_top=ImageTk.PhotoImage(img_top)


        f1_lbl=Label(self.root,image=self.photoimg_top)
        f1_lbl.place(x=0,y=70,width=1530,height=325)


        #button
        b1_1=Button(self.root,text="Train Data",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="red",command=self.train_classifier)
        b1_1.place(x=0,y=400,width=1530,height=40)




        





        img_bottom=Image.open(r"C:\Users\Arpit\Desktop\my project\my images\salar4.jpg")
        img_bottom=img_bottom.resize((1530,325),)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)


        f2_lbl=Label(self.root,image=self.photoimg_bottom)
        f2_lbl.place(x=0,y=450,width=1530,height=375)


    def  train_classifier(self):
        data_dir=("data")
        path=[ os.path.join(data_dir,file)  for file in os.listdir(data_dir)] 

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')    #Gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids) 


        
        
        
        
        #=========================Train the classifier===================   
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")


        


if __name__=="_main_" : 

  root=Tk()
  obj=Train(root)  
  root.mainloop()      

