from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Help Desk Panel")

        # Title
        title_lb = Label(self.root, text="HELP DESK", font=("open sans", 35, "bold"), bg="darkblue", fg="white")
        title_lb.place(x=0, y=0, width=1366, height=45)

        # Top Images
        img_top = Image.open(r"img\laptop.jpg")
        img_top = img_top.resize((1366, 723), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lb = Label(self.root, image=self.photoimg_top)
        f_lb.place(x=0, y=45, width=1366, height=723)

        # # Main Frame
        # main_frame = Frame(self.root, bd=2, bg="white")
        # main_frame.place(x=0, y=0, width=1366, height=45)

        dev_label = Label(f_lb, text="Email: atul69030@gmail.com", font=("open sans", 20, "bold"), bg="white")
        dev_label.place(x=450, y=250)

if __name__ == "__main__":
    root=Tk()
    obj=Help(root) 
    root.mainloop() 