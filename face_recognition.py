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
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Detection System Panel")

        # Title
        title_lb = Label(self.root, text="FACE RECOGNITION", font=("open sans", 35, "bold"), bg="darkblue", fg="white")
        title_lb.place(x=0, y=0, width=1366, height=45)

        # Images
        img_left = Image.open(r"img\abstract_0.jpg")
        img_left = img_left.resize((600, 700), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lb = Label(self.root, image=self.photoimg_left)
        f_lb.place(x=0, y=45, width=600, height=700)
        
        img_right = Image.open(r"img\face-detection_0.jpg")
        img_right = img_right.resize((766, 700), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lb = Label(self.root, image=self.photoimg_right)
        f_lb.place(x=600, y=45, width=766, height=700)

        # Button
        b_1 = Button(self.root, text="Face Recognition", command=self.face_recog, cursor="hand2", font=("open sans", 20, "bold"), bg="darkgreen", fg="white")
        b_1.place(x=830, y=600, width=300, height=55)


    # =============== Attendance ========================
    
    def mark_attendance(self, i, r, n, d):
        with open("data.csv", "r+", newline="\n") as f:
            my_data_list = f.readlines()
            name_list = []

            for line in my_data_list:
                entry = line.split((","))
                name_list.append(entry[0])

            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S") 
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
                

    # =============== Face Recognition Function ========================

    def face_recog(self):
        def draw_baoundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", port=3307, username="root", password="admin", database="face_recognition")
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where Student_Id="+str(id))
                n = my_cursor.fetchone()
                n = "".join(n)
                
                my_cursor.execute("select Rollno from student where Student_Id="+str(id))
                r = my_cursor.fetchone()
                r = "".join(r)
                
                my_cursor.execute("select Department from student where Student_Id="+str(id))
                d = my_cursor.fetchone()
                d = "".join(d)
                
                my_cursor.execute("select Student_Id from student where Student_Id="+str(id))
                i = my_cursor.fetchone()
                i = "".join(i)

                if confidence > 77:
                    cv2.putText(img, f"SID: {i}", (x,y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)
                    cv2.putText(img, f"Name: {n}", (x,y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)
                    cv2.putText(img, f"Rollno: {r}", (x,y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)
                    cv2.putText(img, f"Department: {d}", (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)
                    self.mark_attendance(i, r, n, d)
                    
                else:
                    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)

                coord = [x,y,w,h]

            return coord
        
        def recogize(img, clf, faceCascade):
            coord = draw_baoundary(img, faceCascade, 1.1, 10, (255,25,255), "Face", clf)
            return img
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_capture = cv2.VideoCapture(0)
        
        while True:
            ret, img = video_capture.read()
            img = recogize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1)==13:
                break

        video_capture.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root) 
    root.mainloop()