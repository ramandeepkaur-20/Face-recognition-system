from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45) 
        
        ## First image
        img_top = Image.open(r"college_images\pic2.jpg")
        img_top = img_top.resize((650,700), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
                                       
        f_lb3 = Label(self.root, image=self.photoimg_top)
        f_lb3.place(x=0, y=55, width=650, height=700) 
        
        
        #Second image
        
        img_bottom = Image.open(r"college_images\pic19.png")
        img_bottom = img_bottom.resize((950,700), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
                                               
        f_lb3 = Label(self.root, image=self.photoimg_bottom)
        f_lb3.place(x=650, y=55, width=950, height=700) 
        
        
         # button
                
        b1_1=Button(f_lb3,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",18,"bold"),bg="darkgreen",fg="white")
        b1_1.place(x=365,y=630,width=200,height=40) 
        
        ### Attendence
    def mark_attendence(self,i,r,n,d):
        with open("Inder.csv","r+" ,newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((",")) 
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list)  and  (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
            
             
        
        
        
        
        
        
        #  face recongnition
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            
            coord=[]
            
            for(x,y,w,h) in features:
                cv2.rectangle(img, (x, y),(x+w, y+h),(0,0,255), 3)
                id,predict=clf.predict(gray_image[y:y+h, x:x+w])

                confidence=int((100*(1-predict/300)))
                
                
                conn=mysql.connector.connect(host="localhost",username="root",password="Inder@15",database="face_recognizer1")
                my_cursor=conn.cursor()
                my_cursor.execute("SELECT name FROM student WHERE student_id=%s",(id,))
                n = my_cursor.fetchone()
                n = n[0] if n else "Unknown"
                                
                my_cursor.execute("SELECT Roll FROM student WHERE student_id=%s", (id,))
                r = my_cursor.fetchone()
                r = r[0] if r else "Unknown"
                
                my_cursor.execute("SELECT Dep FROM student WHERE student_id=%s", (id,))
                d = my_cursor.fetchone()
                d = d[0] if d else "Unknown"
                
                my_cursor.execute("SELECT student_id FROM student WHERE student_id=%s", (id,))
                i = my_cursor.fetchone()
                i = i[0] if d else "Unknown"
                
                if confidence > 77:
                    cv2.putText(img," StudentID: %s" %i,(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,"Roll: %s" %r,(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,"name: %s" %n,(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,"Dep: %s" %d,(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendence(i,r,n,d)
                else:
                     cv2.rectangle(img,(x, y),(x+w, y+h),(0,0,255), 3)
                     cv2.putText(img,"Unknown Face",(x,y-10),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                     coord=[x,y,w,h]
            return coord
        def recognizer(img,clf,faceCascade):
            coord=draw_boundray(img, faceCascade, 1.1, 10, (255,255,255), clf)
            return img
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img=recognizer(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)
            
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()   


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()                  