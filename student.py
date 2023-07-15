from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Student Management System Panel")

        # ================= Variables ===================
        
        self.var_name = StringVar()
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_sid = StringVar()
        self.var_div = StringVar()
        self.var_rollno = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_faculty = StringVar()
        # self.var_photo = StringVar()

        # ================= Layout =========================
        # Header Image 1
        img1 = Image.open(r".\img\students copy.jpg")
        img1 = img1.resize((455, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lb = Label(self.root, image=self.photoimg1)
        f_lb.place(x=0, y=0, width=455, height=130)
        
        # Header Image 2
        img2 = Image.open(r".\img\students3 copy.jpg")
        img2 = img2.resize((455, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lb = Label(self.root, image=self.photoimg2)
        f_lb.place(x=455, y=0, width=455, height=130)
        
        # Header Image 3
        img3 = Image.open(r".\img\study copy.jpg")
        img3 = img3.resize((455, 130), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lb = Label(self.root, image=self.photoimg3)
        f_lb.place(x=910, y=0, width=455, height=130)

        # Background Image 3
        img4 = Image.open(r".\img\cyber.jpg")
        img4 = img4.resize((1366, 638), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1366, height=638)

        # Title
        title_lb = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("open sans", 35, "bold"), bg="darkblue", fg="white")
        title_lb.place(x=0, y=0, width=1366, height=45)

        # Main Frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1340, height=510)

        #Left Label Frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Information", font=("open sans", 12, "bold"))
        left_frame.place(x=10, y=3, width=650, height=495)

        img_left = Image.open(r".\img\group2 copy.jpg")
        img_left = img_left.resize((640, 100), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lb = Label(left_frame, image=self.photoimg_left)
        f_lb.place(x=3, y=0, width=640, height=100)

        # Current Course
        curr_course_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information", font=("open sans", 12, "bold"))
        curr_course_frame.place(x=3, y=102, width=640, height=100)

        # Department
        dep_label = Label(curr_course_frame, text="Department:", font=("open sans", 10, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        dep_combo = ttk.Combobox(curr_course_frame, textvariable=self.var_dep, font=("open sans", 10), width=20, state="readonly")
        dep_combo["values"] = ("Select Department", "Computer Science", "Information Technology", "Mechanical", "Civil", "Electrical", "Others")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Course
        course_label = Label(curr_course_frame, text="Course:", font=("open sans", 10, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        course_combo = ttk.Combobox(curr_course_frame, textvariable=self.var_course, font=("open sans", 10), width=20, state="readonly")
        course_combo["values"] = ("Select Course", "Software Engineering", "Data Science", "Production Engineering", "Automobile", "Machine Learning", "Web Development", "Others")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Year
        year_label = Label(curr_course_frame, text="Year:", font=("open sans", 10, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        year_combo = ttk.Combobox(curr_course_frame, textvariable=self.var_year, font=("open sans", 10), width=20, state="readonly")
        year_combo["values"] = ("Select Year", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Semester
        sem_label = Label(curr_course_frame, text="Semester:", font=("open sans", 10, "bold"), bg="white")
        sem_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        sem_combo = ttk.Combobox(curr_course_frame, textvariable=self.var_sem, font=("open sans", 10), width=20, state="readonly")
        sem_combo["values"] = ("Select Semester", "I", "II", "III", "IV", "V", "VI", "VII", "VIII")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Class Information
        class_student_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Student Class Information", font=("open sans", 12, "bold"))
        class_student_frame.place(x=3, y=205, width=640, height=260)

        # Student ID
        studentId_label = Label(class_student_frame, text="Student ID:", font=("open sans", 10, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentId_entry = ttk.Entry(class_student_frame, textvariable=self.var_sid, width=20, font=("open sans", 10))
        studentId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student Name
        studentName_label = Label(class_student_frame, text="Student Name:", font=("open sans", 10, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_student_frame, textvariable=self.var_name, width=20, font=("open sans", 10))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)
        
        # Class Division
        classDiv_label = Label(class_student_frame, text="Division:", font=("open sans", 10, "bold"), bg="white")
        classDiv_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        classDiv_combo = ttk.Combobox(class_student_frame, textvariable=self.var_div, font=("open sans", 10), width=15, state="readonly")
        classDiv_combo["values"] = ("Select", "A", "B", "C", "D", "E", "F")
        classDiv_combo.current(0)
        classDiv_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Roll No
        rollno_label = Label(class_student_frame, text="Roll No:", font=("open sans", 10, "bold"), bg="white")
        rollno_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        rollno_entry = ttk.Entry(class_student_frame, textvariable=self.var_rollno, width=20, font=("open sans", 10))
        rollno_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender
        gender_label = Label(class_student_frame, text="Gender:", font=("open sans", 10, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=("open sans", 10), width=15, state="readonly")
        gender_combo["values"] = ("Select", "Male", "Female", "Others")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # DOB
        dob_label = Label(class_student_frame, text="Date of Birth:", font=("open sans", 10, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20, font=("open sans", 10))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        email_label = Label(class_student_frame, text="Email:", font=("open sans", 10, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20, font=("open sans", 10))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone no
        phone_label = Label(class_student_frame, text="Phone No:", font=("open sans", 10, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=20, font=("open sans", 10))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address
        address_label = Label(class_student_frame, text="Address:", font=("open sans", 10, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, width=20, font=("open sans", 10))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Faculty Name
        faculty_label = Label(class_student_frame, text="Faculty Name:", font=("open sans", 10, "bold"), bg="white")
        faculty_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        faculty_entry = ttk.Entry(class_student_frame, textvariable=self.var_faculty, width=20, font=("open sans", 10))
        faculty_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # Radio Buttons
        self.var_radio1 = StringVar()
        radio_btn1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radio_btn1.grid(row=5, column=0, padx=10, pady=2)
        
        self.var_radio2 = StringVar()
        radio_btn2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radio_btn2.grid(row=5, column=1, padx=10, pady=2)
      
        # Button Frame
        btn_frame = Frame(class_student_frame, bd=2, bg="white", relief=RIDGE)
        btn_frame.place(x=0, y=202, width=636, height=34)

        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=19, font=("open sans", 10, "bold"), bg="green", fg="white")
        save_btn.grid(row=0, column=0)
        
        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=19, font=("open sans", 10, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)
        
        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=19, font=("open sans", 10, "bold"), bg="red", fg="white")
        delete_btn.grid(row=0, column=2)
        
        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=18, font=("open sans", 10, "bold"), bg="violet", fg="white")
        reset_btn.grid(row=0, column=3)

        # Other Button Frame
        btn_frame1 = Frame(class_student_frame, bd=2, bg="white", relief=RIDGE)
        btn_frame1.place(x=324, y=170, width=312, height=34)

        take_photo_btn = Button(btn_frame1, command=self.generate_dataset, text="Take Photo Sample", width=19, font=("open sans", 10, "bold"), bg="teal", fg="white")
        take_photo_btn.grid(row=0, column=0)
        
        update_photo_btn = Button(btn_frame1, text="Update Photo", width=18, font=("open sans", 10, "bold"), bg="magenta", fg="white")
        update_photo_btn.grid(row=0, column=1)


        # Right Label Frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("open sans", 12, "bold"))
        right_frame.place(x=670, y=3, width=650, height=495)

        img_right = Image.open(r".\img\classroom copy.jpg")
        img_right = img_right.resize((640, 100), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lb = Label(right_frame, image=self.photoimg_right)
        f_lb.place(x=3, y=0, width=640, height=100)

        # ===================== Search System =====================

        # Search Frame
        search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("open sans", 12, "bold"))
        search_frame.place(x=3, y=102, width=640, height=65)

        search_label = Label(search_frame, text="Search By:", font=("open sans", 10, "bold"), bg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("open sans", 10), width=15, state="readonly")
        search_combo["values"] = ("Select", "Roll No", "Phone", "Email", "Enroll ID")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        search_entry = ttk.Entry(search_frame, width=20, font=("open sans", 10))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search", width=10, font=("open sans", 10, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=10)
        
        showAll_btn = Button(search_frame, text="Show All", width=10, font=("open sans", 10, "bold"), bg="darkblue", fg="white")
        showAll_btn.grid(row=0, column=4, padx=5)

        # Table Frame
        table_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=3, y=170, width=640, height=300)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("name", "dep", "course", "year", "sem", "id", "div", "rollno", "gender", "dob", "email", "phone", "faculty", "address", "photo"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("name", text="Name")
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("rollno", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("faculty", text="Faculty")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("photo", text="Photo Sample Status")
        self.student_table["show"] = "headings"

        self.student_table.column("name", width=80)
        self.student_table.column("dep", width=80)
        self.student_table.column("course", width=80)
        self.student_table.column("year", width=80)
        self.student_table.column("sem", width=80)
        self.student_table.column("id", width=80)
        self.student_table.column("div", width=80)
        self.student_table.column("rollno", width=80)
        self.student_table.column("gender", width=80)
        self.student_table.column("dob", width=80)
        self.student_table.column("email", width=80)
        self.student_table.column("phone", width=80)
        self.student_table.column("faculty", width=80)
        self.student_table.column("address", width=80)
        self.student_table.column("photo", width=80)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()


    # ======================= Function Declaration ============================

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_sid.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        
        else:
            try:
                conn = mysql.connector.connect(host="localhost", port=3307, username="root", password="admin", database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("Insert into student values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                    self.var_name.get(),
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_sid.get(),
                    self.var_div.get(),
                    self.var_rollno.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_faculty.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Success", " Student details has been added Successfully", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)


    # ============ Fetch Data ==============

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", port=3307, username="root", password="admin", database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # ============== Get Cursor ===============

    def get_cursor(self, event):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_name.set(data[0]),
        self.var_dep.set(data[1]),
        self.var_course.set(data[2]),
        self.var_year.set(data[3]),
        self.var_sem.set(data[4]),
        self.var_sid.set(data[5]),
        self.var_div.set(data[6]),
        self.var_rollno.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_faculty.set(data[13]),
        self.var_radio1.set(data[14])

    # ============= Update Function ============

    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_sid.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)

        else:
            try:
                update_info = messagebox.askyesno("Update", "Do you want to update this student details?", parent=self.root)
                if update_info > 0:
                    conn = mysql.connector.connect(host="localhost", port=3307, username="root", password="admin", database="face_recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Name=%s, Department=%s, Course=%s, Year=%s, Semester=%s, Division=%s, Rollno=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Address=%s, Faculty=%s, Photo_Sample=%s where Student_Id=%s", (
                        self.var_name.get(),
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_div.get(),
                        self.var_rollno.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_faculty.get(),
                        self.var_radio1.get(),
                        self.var_sid.get()
                    ))

                else:
                    if not update_info:
                        return
                
                messagebox.showinfo("Success", "Student details updated successfully", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error", f"Dut to : {str(es)}", parent=self.root)

    # =============== Delete Function ==============

    def delete_data(self):
        if self.var_sid.get() == "":
            messagebox.showerror("Error", "Student ID must be required for delete the data", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this student?", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", port=3307, username="root", password="admin", database="face_recognition")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_Id=%s"
                    val = (self.var_sid.get(),)
                    my_cursor.execute(sql, val)
                
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully deled student details", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Dut to : {str(es)}", parent=self.root)

    # ==================== Reset Function ======================

    def reset_data(self):
        self.var_name.set(""),
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_sem.set("Select Semester"),
        self.var_sid.set(""),
        self.var_div.set("Select"),
        self.var_rollno.set(""),
        self.var_gender.set("Select"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_faculty.set(""),
        self.var_radio1.set("")

    # ====================== Computer Vision =========================
    # ========== Generate Data sets or Take Photo Samples ============

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_sid.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(host="localhost", port=3307, username="root", password="admin", database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("Select * from student")
                my_result = my_cursor.fetchall()
                id = 0
                for x in my_result:
                    id += 1
                my_cursor.execute("update student set Name=%s, Department=%s, Course=%s, Year=%s, Semester=%s, Division=%s, Rollno=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Address=%s, Faculty=%s, Photo_Sample=%s where Student_Id=%s", (
                    self.var_name.get(),
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_div.get(),
                    self.var_rollno.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_faculty.get(),
                    self.var_radio1.get(),
                    self.var_sid.get()==id+1
                ))

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ============ Load Predefine Data on Face ================

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # scaling factor = 1.3
                    # minimum neighbor = 5

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped
                    
                capture = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = capture.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = f"data/user.{str(id)}.{str(img_id)}.jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                
                capture.release()
                cv2.destroyAllWindows()

                messagebox.showinfo("Result", "Data Sets Generated Successfully!!!", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Dut to : {str(es)}", parent=self.root)




if __name__ == "__main__":
    root=Tk()
    obj=Student(root) 
    root.mainloop()