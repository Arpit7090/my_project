from tkinter import *
from tkinter import ttk
from PIL import Image ,ImageTk
import sqlite3
from tkinter import messagebox
import cv2

class stu:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x790+0+0")
        self.root.title("face Recognization System")

    #=========================================variables==============================================================


        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_dep=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_stuid=StringVar()
        self.var_name=StringVar()
        self.var_division=StringVar()
        self.var_rollno=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        
        
        
        
        
        
        

        
        
        
        
        
        
        



        #first image
        img=Image.open(r"C:\Users\Arpit\Desktop\my project\my images\1.jpg")
        img=img.resize((500,130),)
        self.photoimg=ImageTk.PhotoImage(img)

        f1lbl=Label(self.root,image=self.photoimg)
        f1lbl.place(x=0,y=0)


        #SECOND image
        img1=Image.open(r"C:\Users\Arpit\Desktop\my project\my images\2.jpg")
        img1=img1.resize((500,130),)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f2lbl=Label(self.root,image=self.photoimg1)
        f2lbl.place(x=500,y=0)


        #Third image
        img2=Image.open(r"C:\Users\Arpit\Desktop\my project\my images\4.jpg")
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


        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="green",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=20,y=55,width=1500,height=600)

        # Left Label frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Detail",font=("times new roman",12,"bold"),fg="red")
        Left_frame.place(x=10,y=10,width=830,height=580)

        img_left=Image.open(r"C:\Users\Arpit\Desktop\my project\my images\5.jpg")
        img_left=img_left.resize((740,130),)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f2lbl=Label(Left_frame,image=self.photoimg_left)
        f2lbl.place(x=10,y=0,width=740,height=130)

        # Current course frame
        current_course_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"),fg="red")
        current_course_frame.place(x=15,y=165,width=740,height=110)

        #Department

        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),fg="black")
        dep_label.grid(row=0,column=0)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12),width=17)
        dep_combo.grid(row=0,column=1,pady=10,padx=2)

        #course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),fg="black")
        course_label.grid(row=0,column=2,padx=15,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12),width=17)
        course_combo.grid(row=0,column=3,pady=10,padx=2,sticky=W)

        # year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),fg="black")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12),width=17)
        year_combo.grid(row=1,column=1,pady=10,padx=2,sticky=W)


        # Semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),fg="black")
        semester_label.grid(row=1,column=2,padx=15,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12),width=17)
        semester_combo.grid(row=1,column=3,pady=10,padx=6,sticky=W)

        # class student information
        class_student_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Detail",font=("times new roman",12,"bold"),fg="red")
        class_student_frame.place(x=15,y=275,width=820,height=300)

        #Student id

        studentId_label=Label(class_student_frame,text="Student Id",font=("times new roman",12,"bold"),fg="black")
        studentId_label.grid(row=0,column=0,padx=5,sticky=W)

        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_stuid,width=20,font=("times new roman",12,"bold"))
        studentId_entry.grid(row=0,column=1)

        #student name
        studentname_label=Label(class_student_frame,text="Student Name",font=("times new roman",12,"bold"),fg="black")
        studentname_label.grid(row=1,column=0,padx=5,pady=10,sticky=W)

        studentname_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=20,font=("times new roman",12,"bold"))
        studentname_entry.grid(row=1,column=1,padx=5,pady=10,)

        #class Division
        class_div_label=Label(class_student_frame,text="Class Division",font=("times new roman",12,"bold"),fg="black")
        class_div_label.grid(row=2,column=0,padx=5,pady=10,sticky=W)

        class_div_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_division,font=("times new roman",12,"bold"))
        class_div_entry.grid(row=2,column=1,padx=5,pady=10,)

        
        #email
        email_label=Label(class_student_frame,text="Email",font=("times new roman",12,"bold"),fg="black")
        email_label.grid(row=0,column=4,padx=5,pady=10,sticky=W)

        email_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_email,font=("times new roman",12,"bold"))
        email_entry.grid(row=0,column=5,padx=5,pady=10,)

        '''#class division
        class_label=Label(class_student_frame,text="class division",font=("times new roman",12,"bold"),fg="black")
        class_label.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        class_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",12,"bold"))
        class_entry.grid(row=0,column=4,padx=5,pady=10,)'''

         #Dob
        dob_label=Label(class_student_frame,text="Dob",font=("times new roman",12,"bold"),fg="black")
        dob_label.grid(row=1,column=4,padx=5,pady=10,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_dob,font=("times new roman",12,"bold"))
        dob_entry.grid(row=1,column=5,padx=5,pady=10,)


        #Gender
        gender_label=Label(class_student_frame,text="Gender",font=("times new roman",12,"bold"),fg="black")
        gender_label.grid(row=2,column=4,padx=5,pady=10,sticky=W)

        gender_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_gender,font=("times new roman",12,"bold"))
        gender_entry.grid(row=2,column=5,padx=5,pady=10,)



        #Roll no
        rollno_label=Label(class_student_frame,text="Roll No",font=("times new roman",12,"bold"),fg="black")
        rollno_label.grid(row=0,column=6,padx=3,pady=10,sticky=W)

        rollno_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_rollno,font=("times new roman",12,"bold"))
        rollno_entry.grid(row=0,column=7,padx=3,pady=10,)

        #address
        address_label=Label(class_student_frame,text="Address",font=("times new roman",12,"bold"),fg="black")
        address_label.grid(row=1,column=6,padx=3,pady=10,sticky=W)

        address_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_address,font=("times new roman",12,"bold"))
        address_entry.grid(row=1,column=7,padx=3,pady=10,)

        #Phone number
        phone_label=Label(class_student_frame,text="Phone number",font=("times new roman",12,"bold"),fg="black")
        phone_label.grid(row=2,column=6,padx=3,pady=10,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_phone,font=("times new roman",12,"bold"))
        phone_entry.grid(row=2,column=7,padx=3,pady=10,)

        #radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)

        
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5,column=1)



        #bbuttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=160,width=723,height=35)         

        save_btn=Button(btn_frame,text="Save",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white",command=self.add_data)
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white",command=self.update_data)
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white",command=self.delete_data)
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white",command=self.reset_data)
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=210,width=723,height=35)     

        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",width=17,font=("times new roman",13,"bold"),bg="green",fg="white",command=self.generate_dataset)  
        take_photo_btn.grid(row=0,column=0)

        update_take_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=17,font=("times new roman",13,"bold"),bg="green",fg="white")  
        update_take_photo_btn.grid(row=0,column=1)


  
  

                        
                        
                        
                        





















        






        # Right Label frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Detail",font=("times new roman",12,"bold"),fg="red")
        Right_frame.place(x=850,y=10,width=630,height=580)

        img_right=Image.open(r"C:\Users\Arpit\Desktop\my project\my images\rightframe.jpg")
        img_right=img_right.resize((670,130),)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f1lbl=Label(Right_frame,image=self.photoimg_right)
        f1lbl.place(x=0,y=0,width=625,height=130)

        #SEARCH SYSTEM
        Search_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,text="Search System",font=("times new roman",12,"bold"),fg="red")
        Search_frame.place(x=5,y=130,width=620,height=60)

        Search_label=Label(Search_frame,bd=2,relief=RIDGE,text="Search By",font=("times new roman",12,"bold"),bg="red",fg="white")
        Search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(Search_frame,font=("times new roman",12),width=15)
        search_combo["values"]=("Select","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,pady=10,padx=2,sticky=W)

        search_entry=ttk.Entry(Search_frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=3,pady=10,)


        search_btn=Button(Search_frame,text="Search",width=10,font=("times new roman",10,"bold"),bg="green",fg="white")  
        search_btn.grid(row=0,column=3,padx=4)

        showall_btn=Button(Search_frame,text="Show All",width=10,font=("times new roman",10,"bold"),bg="green",fg="white")  
        showall_btn.grid(row=0,column=4,padx=4)

        #==============================table frame=====================================
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,)
        table_frame.place(x=5,y=210,width=620,height=250)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        scroll_y.pack(side=RIGHT,fill=Y)
        
        


        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")

        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        
        self.student_table.heading("dob",text="Dob")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("roll",text="Roll_No")
        self.student_table.heading("photo",text="Photo")
    
    
    
        self.student_table["show"]="headings"
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100) 
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)  
        self.student_table.column("address",width=100) 
        self.student_table.column("photo",width=100) 
                    
        

        self.student_table.pack(fill=BOTH,expand=1)

        self.student_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()
        
        
        
        
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_stuid.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)

        else:
             try:
                db=sqlite3.connect('mystudentdatabase.db')
                cr=db.cursor()
                cr.execute("insert into studata values('"+self.var_dep.get()+"','"+self.var_course.get()+"','"+self.var_year.get()+"','"+self.var_semester.get()+"','"+self.var_stuid.get()+"','"+self.var_name.get()+"','"+self.var_division.get()+"','"+self.var_rollno.get()+"','"+self.var_gender.get()+"','"+self.var_dob.get()+"','"+self.var_email.get()+"','"+self.var_phone.get()+"','"+self.var_address.get()+"',' "+self.var_radio1.get()+" ')")
                db.commit()
                self.fetch_data()
                db.close()
            
                messagebox.showinfo("Success","Students details has been Successfully",parent=self.root)
             except Exception as es:
                 messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root) 

                     
    #======================================fetch data========================================

    def fetch_data(self):
        db=sqlite3.connect('mystudentdatabase.db')
        cr=db.cursor()
        cr.execute("select * from studata")
        data=cr.fetchall()
        if len(data) !=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
                db.commit()
        db.close()


    ### =================================================get cursor=====================================
    def get_cursor(self,event):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"] 

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_stuid.set(data[4]),
        self.var_name.set(data[5]),
        self.var_division.set(data[6]),
        self.var_rollno.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_radio1.set(data[13])

    # update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_stuid.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)  
                if Update>0:
                    db=sqlite3.connect('mystudentdatabase.db')
                    cr=db.cursor()
                    cr.execute("update studata set Department='"+self.var_dep.get()+"',Course='"+self.var_course.get()+"',Year='"+self.var_year.get()+"',Semester='"+self.var_semester.get()+"',Studentid='"+ self.var_stuid.get()+"',Name='"+self.var_name.get()+"',Division='"+self.var_division.get()+"',Rollno='"+self.var_rollno.get()+"' ,Gender='"+self.var_gender.get()+"',Dob='"+self.var_dob.get()+"',Email='"+self.var_email.get()+"',Phone='"+self.var_phone.get()+"', Address='"+self.var_address.get()+"',Radio='"+self.var_radio1.get()+"'where Studentid='"+self.var_stuid.get()+"'")
                    

                else:
                     if not Update:
                         return

                messagebox.showinfo("Success","Student details successfully update complete",parent=self.root)
                db.commit()
                self.fetch_data()
                db.close()
        
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

#=================delete functon
    def delete_data(self):
        if self.var_stuid.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
              delete=messagebox.askyesno("Student delete page","Do you want to delete this student",parent=self.root) 
              if delete>0:
                    db=sqlite3.connect('mystudentdatabase.db')
                    cr=db.cursor()
                    r=cr.execute("delete from studata where Studentid='"+self.var_stuid.get()+"' ")
              else:
                    if not delete:
                        return
              db.commit()   
              self.fetch_data()
              db.close()
              messagebox.showinfo("Delete","Successfully delete",parent=self.root)     

            except Exception as es:
                 messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    # reset
    def reset_data(self):
        self.var_dep.set(""),
        self.var_course.set(""),
        self.var_year.set(""),
        self.var_semester.set(""),
        self.var_stuid.set(""),
        self.var_name.set(""),
        self.var_division.set(""),
        self.var_rollno.set(""),
        self.var_gender.set(""),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_radio1.set("")

#=================================generate data set or take photo samples==========================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_stuid.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
               db=sqlite3.connect('mystudentdatabase.db')
               cr=db.cursor()
               cr.execute("select * from studata")
               myresult=cr.fetchall()
               id=0
               for x in myresult:
                   id+=1
               cr.execute("update studata set Department='"+self.var_dep.get()+"',Course='"+self.var_course.get()+"',Year='"+self.var_year.get()+"',Semester='"+self.var_semester.get()+"',Studentid='"+ self.var_stuid.get()+"',Name='"+self.var_name.get()+"',Division='"+self.var_division.get()+"',Rollno='"+self.var_rollno.get()+"' ,Gender='"+self.var_gender.get()+"',Dob='"+self.var_dob.get()+"',Email='"+self.var_email.get()+"',Phone='"+self.var_phone.get()+"', Address='"+self.var_address.get()+"',Radio='"+self.var_radio1.get()+"'where Studentid='"+self.var_stuid.get()+"'")    
               db.commit() 
               self.fetch_data()
               self.reset_data()
               db.close()

               #==========================Load predefined data on face frontals from opencv ========================================
               face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

               def face_cropped(img):
                   gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                   faces=face_classifier.detectMultiScale(gray,1.3,5)
                   #scaling factor=1.3
                   #Minimum Neighbour=5

                   for (x,y,w,h) in faces:
                       face_cropped=img[y:y+h,x:x+w]
                       return face_cropped

               cap=cv2.VideoCapture(0)
               img_id=0
               while True:
                   ret,my_frame=cap.read()
                   if face_cropped(my_frame) is not None:
                       img_id+=1

                       face=cv2.resize(face_cropped(my_frame),(450,450)) 
                       face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                       file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                       cv2.imwrite(file_name_path,face)
                       cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                       cv2.imshow("Croped face",face)
                   if cv2.waitKey(1)==13 or int(img_id)==50:
                       break

               cap.release()
               cv2.destroyAllWindows()
               messagebox.showinfo("Result","Generating data set  completed ")

            except Exception as es:
                 messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)



if __name__=="_main_" : 

                   

  root=Tk()
  obj=stu(root)  
  root.mainloop()      


