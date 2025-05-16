from tkinter import *
from tkinter import ttk
from PIL import Image ,ImageTk
import sqlite3
from tkinter import messagebox
import cv2
import os
import numpy as np




class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x790+0+0")
        self.root.title("face Recognization System")


        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="green",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        img_top=Image.open(r"C:\Users\Arpit\Desktop\my project\my images\salar5.jpg")
        img_top=img_top.resize((1530,700),)
        
        self.photoimg_top=ImageTk.PhotoImage(img_top)


        f1_lbl=Label(self.root,image=self.photoimg_top)
        f1_lbl.place(x=0,y=40,width=1530,height=700)


        #button
        b1_1=Button(self.root,text="FACE RECOGNITION",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="red",command=self.face_recog)
        b1_1.place(x=0,y=700,width=1530,height=40)




        ###========================variables=========================
        self.var_stuid=StringVar()




    def  face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            coord=[]
            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                db=sqlite3.connect('mystudentdatabase.db')
                cr=db.cursor()
                cr.execute("Select Name from studata where Studentid='"+str(id)+"' ")
                n=cr.fetchone()
                nx="+".join(n)



                cr.execute("Select  Department from studata where Studentid='"+str(id)+"' ")
                d=cr.fetchone()
                dx="+".join(d)





                if confidence>77:
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
    
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)   
                    cv2.putText(img,f"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3) 
                    
                coord=[x,y,w,h]

            return coord  
          
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome TO face  Recognition",img)
            
            if cv2.waitKey(1)==13:
                break

        video_cap.release()
        cv2.destroyAllWindows()



if __name__=="_main_" : 


 root=Tk()
 obj=Face_Recognition(root)  
 root.mainloop()      

