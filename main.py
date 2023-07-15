from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter
import os
from time import strftime
from datetime import datetime

from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help

class Face_Recognition_System:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Advance Face Recognition System")

        # Header Image 1
        img1 = Image.open(r"C:\Users\Atul\Downloads\Images\abstract-g9d8f4d565_1920.jpg")
        img1 = img1.resize((455, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lb = Label(self.root, image=self.photoimg1)
        f_lb.place(x=0, y=0, width=455, height=130)
        
        # Header Image 2
        img2 = Image.open(r"C:\Users\Atul\Downloads\Images\artificial-intelligence-g8da9c0309_1920.jpg")
        img2 = img2.resize((455, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lb = Label(self.root, image=self.photoimg2)
        f_lb.place(x=455, y=0, width=455, height=130)
        
        # Header Image 3
        img3 = Image.open(r"C:\Users\Atul\Downloads\Images\face-detection-ge0ac2f39a_1920.jpg")
        img3 = img3.resize((455, 130), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lb = Label(self.root, image=self.photoimg3)
        f_lb.place(x=910, y=0, width=455, height=130)
        
        # Background Image 3
        img4 = Image.open(r"C:\Users\Atul\Downloads\Images\cyber-g5b60cbf71_1920.jpg")
        img4 = img4.resize((1366, 638), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1366, height=638)

        # Title
        title_lb = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("open sans", 35, "bold"), bg="blue", fg="white")
        title_lb.place(x=0, y=0, width=1366, height=45)

        # =============== Time ==============
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl = Label(title_lb, font=("open sans", 12, "bold"),bg='blue', fg='white')
        lbl.place(x=5, y=5, width=100, height=30)
        time()


        #1 Student Button
        img5 = Image.open(r"C:\Users\Atul\Downloads\Images\pexels-buro-millennial-1438081.jpg")
        img5 = img5.resize((150, 150), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, command=self.student_details, cursor="hand2")
        b1.place(x=150, y=100, width=150, height=150)

        b_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=("open sans", 12, "bold"), bg="blue", fg="white")
        b_1.place(x=150, y=250, width=150, height=40)

        #2 Detect Face Button
        img6 = Image.open(r"C:\Users\Atul\Downloads\Images\pexels-thisisengineering-3861969.jpg")
        img6 = img6.resize((150, 150), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, command=self.face_data, cursor="hand2")
        b1.place(x=450, y=100, width=150, height=150)

        b_1 = Button(bg_img, text="Face Detection", command=self.face_data, cursor="hand2", font=("open sans", 12, "bold"), bg="blue", fg="white")
        b_1.place(x=450, y=250, width=150, height=40)

        #3 Attendance Button
        img7 = Image.open(r"C:\Users\Atul\Downloads\Images\pexels-burst-374720.jpg")
        img7 = img7.resize((150, 150), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, command=self.attendence_data, image=self.photoimg7, cursor="hand2")
        b1.place(x=750, y=100, width=150, height=150)

        b_1 = Button(bg_img, command=self.attendence_data, text="Attendance", cursor="hand2", font=("open sans", 12, "bold"), bg="blue", fg="white")
        b_1.place(x=750, y=250, width=150, height=40)

        #4 Help Button
        img8 = Image.open(r"C:\Users\Atul\Downloads\Images\possessed-photography-zbLW0FG8XU8-unsplash.jpg")
        img8 = img8.resize((150, 150), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, command=self.help_data, image=self.photoimg8, cursor="hand2")
        b1.place(x=1050, y=100, width=150, height=150)

        b_1 = Button(bg_img, command=self.help_data, text="Help Desk", cursor="hand2", font=("open sans", 12, "bold"), bg="blue", fg="white")
        b_1.place(x=1050, y=250, width=150, height=40)
        
        # Train Button
        img9 = Image.open(r"C:\Users\Atul\Downloads\Images\possessed-photography-YKW0JjP7rlU-unsplash.jpg")
        img9 = img9.resize((150, 150), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9, command=self.train_data, cursor="hand2")
        b1.place(x=150, y=350, width=150, height=150)

        b_1 = Button(bg_img, text="Train Data", command=self.train_data, cursor="hand2", font=("open sans", 12, "bold"), bg="blue", fg="white")
        b_1.place(x=150, y=500, width=150, height=40)

        # Photos Button
        img10 = Image.open(r"C:\Users\Atul\Downloads\Images\melissa-askew-tSlvoSZK77c-unsplash.jpg")
        img10 = img10.resize((150, 150), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10, command=self.open_img, cursor="hand2")
        b1.place(x=450, y=350, width=150, height=150)

        b_1 = Button(bg_img, text="Photos", cursor="hand2", command=self.open_img, font=("open sans", 12, "bold"), bg="blue", fg="white")
        b_1.place(x=450, y=500, width=150, height=40)

        # Developer Button
        img11 = Image.open(r"C:\Users\Atul\Downloads\Images\kevin-ku-w7ZyuGYNpRQ-unsplash.jpg")
        img11 = img11.resize((150, 150), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, command=self.developer_data, image=self.photoimg11, cursor="hand2")
        b1.place(x=750, y=350, width=150, height=150)

        b_1 = Button(bg_img, command=self.developer_data, text="Developer", cursor="hand2", font=("open sans", 12, "bold"), bg="blue", fg="white")
        b_1.place(x=750, y=500, width=150, height=40)
        
        # Exit Button
        img12 = Image.open(r"C:\Users\Atul\Downloads\Images\information-ga4c577d7f_1280.png")
        img12 = img12.resize((150, 150), Image.ANTIALIAS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        b1 = Button(bg_img, command=self.iExit, image=self.photoimg12, cursor="hand2")
        b1.place(x=1050, y=350, width=150, height=150)

        b_1 = Button(bg_img, command=self.iExit, text="Exit", cursor="hand2", font=("open sans", 12, "bold"), bg="blue", fg="white")
        b_1.place(x=1050, y=500, width=150, height=40)

    # =========== Other Function ================
    
    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition", "Are you sure to exit the program?", parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return
    
    # =========== Fuction Button ===============

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendence_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)




if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)  
    root.mainloop()