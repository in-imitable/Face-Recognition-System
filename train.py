from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Train Data System Panel")

        # Title
        title_lb = Label(self.root, text="TRAIN DATA SET SYSTEM", font=("open sans", 35, "bold"), bg="blue", fg="white")
        title_lb.place(x=0, y=0, width=1366, height=45)

        # Top Images
        img_top = Image.open(r"img\man-gee9e16cc6_1920_0.jpg")
        img_top = img_top.resize((1366, 300), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lb = Label(self.root, image=self.photoimg_top)
        f_lb.place(x=0, y=45, width=1366, height=300)

        # Button
        b_1 = Button(self.root, text="Train Data", command=self.train_classifier, cursor="hand2", font=("open sans", 20, "bold"), bg="darkblue", fg="white")
        b_1.place(x=0, y=345, width=1366, height=55)

        # Bottom Images
        img_bottom = Image.open(r"img\face-detection-ge0ac2f39a_1920.jpg")
        img_bottom = img_bottom.resize((1366, 300), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lb = Label(self.root, image=self.photoimg_bottom)
        f_lb.place(x=0, y=400, width=1366, height=300)


    # Train data function

    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')    # Gray Scale Image
            imgNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imgNp)
            ids.append(id)

            cv2.imshow("Training", imgNp)
            cv2.waitKey(1)==13

        ids = np.array(ids)

        # Train the classifier and save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Dataset Completed!!!")


if __name__ == "__main__":
    root=Tk()
    obj=Train(root) 
    root.mainloop()
