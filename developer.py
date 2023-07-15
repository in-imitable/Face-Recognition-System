from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Developer Panel")

        # Title
        title_lb = Label(self.root, text="DEVELOPER INFO", font=("open sans", 35, "bold"), bg="darkblue", fg="white")
        title_lb.place(x=0, y=0, width=1366, height=45)

        # Top Images
        img_top = Image.open(r"img\tech1.jpg")
        img_top = img_top.resize((1366, 723), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lb = Label(self.root, image=self.photoimg_top)
        f_lb.place(x=0, y=45, width=1366, height=723)

        # Main Frame
        main_frame = Frame(f_lb, bd=2, bg="white")
        main_frame.place(x=800, y=0, width=500, height=600)

        # Main Frame Images
        dev_img = Image.open(r"img\Dev.jpg")
        dev_img = dev_img.resize((150, 150), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(dev_img)

        f_lb = Label(main_frame, image=self.photoimg)
        f_lb.place(x=350, y=0, width=150, height=150)

        # Developer Info
        dev_label = Label(main_frame, text="Hello, My name is Atul", font=("open sans", 12, "bold"), bg="white")
        dev_label.place(x=0, y=5)
        
        dev_label = Label(main_frame, text="I'm a Full Stack Developer", font=("open sans", 12, "bold"), bg="white")
        dev_label.place(x=0, y=30)

        # Frame Image 2
        img2 = Image.open(r"img\device.jpg")
        img2 = img2.resize((500, 450), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lb = Label(main_frame, image=self.photoimg2)
        f_lb.place(x=0, y=150, width=500, height=450)


if __name__ == "__main__":
    root=Tk()
    obj=Developer(root) 
    root.mainloop() 