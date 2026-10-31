from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl=Label(self.root,text="HELP Desk",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45) 
                
        img_top = Image.open(r"C:\Users\Ramandeep Kaur\Desktop\Face Recognition sytem\college_images\pic23.jpg")
        img_top = img_top.resize((1530,720), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
                                       
        f_lb3 = Label(self.root, image=self.photoimg_top)
        f_lb3.place(x=0, y=55, width=1530, height=720) 
        
        dev_label=Label( f_lb3,text="Email:inderpreet142005@gmail.com",font=("times new roman",13,"bold"),bg="white") 
        dev_label.place(x=650,y=200) 
        
        
if __name__ == "__main__":
      root = Tk()
      obj = Help(root)
      root.mainloop()          