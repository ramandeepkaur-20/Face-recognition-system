from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45) 
                
        img_top = Image.open(r"college_images\pic20.png")
        img_top = img_top.resize((1530,720), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
                                       
        f_lb3 = Label(self.root, image=self.photoimg_top)
        f_lb3.place(x=0, y=55, width=1530, height=720) 
                
        
        # Frame
        
        main_frame=Frame(f_lb3,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)  
        
        img_top1 = Image.open(r"college_images\pic21.jfif")
        img_top1 = img_top1.resize((200,200), Image.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)
                                               
        f_lb3 = Label(main_frame, image=self.photoimg_top1)
        f_lb3.place(x=300, y=0, width=200, height=200) 
                        
        # Developer info
                      
        dev_label=Label(main_frame,text="hello my name is Inder",font=("times new roman",13,"bold"),bg="white") 
        dev_label.place(x=0,y=5) 
        
        dev_label=Label(main_frame,text="I am full stack developer",font=("times new roman",13,"bold"),bg="white") 
        dev_label.place(x=0,y=40)                        
        
        img2 = Image.open(r"C:\Users\Ramandeep Kaur\Desktop\Face Recognition sytem\college_images\pic22.jpg")
        img2 = img2.resize((500,400), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
                       
        f_lb3 = Label(main_frame, image=self.photoimg2)
        f_lb3.place(x=0, y=210, width=500, height=400) 
            
        
        
        
        
        
        
        
if __name__ == "__main__":
      root = Tk()
      obj = Developer(root)
      root.mainloop()                