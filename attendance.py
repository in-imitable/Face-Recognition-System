from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []

class Attendance:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Attendance System Panel")

        # ================= Variables ===================
        
        self.var_attend_id = StringVar()
        self.var_rollno = StringVar()
        self.var_name = StringVar()
        self.var_depart = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_attendance = StringVar()

        # First Image 2
        img1 = Image.open(r"img\group3.jpg")
        img1 = img1.resize((683, 200), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lb = Label(self.root, image=self.photoimg1)
        f_lb.place(x=0, y=0, width=683, height=200)
        
        # Second Image 2
        img2 = Image.open(r"img\students3 copy.jpg")
        img2 = img2.resize((683, 200), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lb = Label(self.root, image=self.photoimg2)
        f_lb.place(x=683, y=0, width=683, height=200)

        # Background Image 3
        img4 = Image.open(r"img\cyber.jpg")
        img4 = img4.resize((1366, 568), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=200, width=1366, height=568)

        # Title
        title_lb = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("open sans", 35, "bold"), bg="darkblue", fg="white")
        title_lb.place(x=0, y=0, width=1366, height=45)

        # Main Frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=5, y=50, width=1350, height=445)

        #Left Label Frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("open sans", 12, "bold"))
        left_frame.place(x=10, y=3, width=655, height=430)

        img_left = Image.open(r"img\man-gee9e16cc6_1920_0.jpg")
        img_left = img_left.resize((655, 100), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lb = Label(left_frame, image=self.photoimg_left)
        f_lb.place(x=3, y=0, width=646, height=100)

        left_inside_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=2, y=105, width=646, height=297)

        # Label and entry

        # Attendance ID
        attendanceId_label = Label(left_inside_frame, text="Attendance ID:", font=("open sans", 10, "bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        attendanceId_entry = ttk.Entry(left_inside_frame, width=22, textvariable=self.var_attend_id, font=("open sans", 10))
        attendanceId_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        # Roll no
        rollno_label = Label(left_inside_frame, text="Roll No:", font=("open sans", 10, "bold"), bg="white")
        rollno_label.grid(row=0, column=2, padx=10, pady=10, sticky=W)

        rollno_entry = ttk.Entry(left_inside_frame, width=22, textvariable=self.var_rollno, font=("open sans", 10))
        rollno_entry.grid(row=0, column=3, padx=10, pady=10, sticky=W)

        # Student Name
        studentName_label = Label(left_inside_frame, text="Student Name:", font=("open sans", 10, "bold"), bg="white")
        studentName_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(left_inside_frame, width=22, textvariable=self.var_name, font=("open sans", 10))
        studentName_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Department
        department_label = Label(left_inside_frame, text="Department:", font=("open sans", 10, "bold"), bg="white")
        department_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        department_entry = ttk.Entry(left_inside_frame, width=22, textvariable=self.var_depart, font=("open sans", 10))
        department_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Time
        time_label = Label(left_inside_frame, text="Time:", font=("open sans", 10, "bold"), bg="white")
        time_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        time_entry = ttk.Entry(left_inside_frame, width=22, textvariable=self.var_time, font=("open sans", 10))
        time_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Date
        date_label = Label(left_inside_frame, text="Date:", font=("open sans", 10, "bold"), bg="white")
        date_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        date_entry = ttk.Entry(left_inside_frame, width=22, textvariable=self.var_date, font=("open sans", 10))
        date_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Attendance
        attend_label = Label(left_inside_frame, text="Attendance Status:", font=("open sans", 10, "bold"), bg="white")
        attend_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        self.attend_combo = ttk.Combobox(left_inside_frame, font=("open sans", 10), width=20, textvariable=self.var_attendance, state="readonly")
        self.attend_combo["values"] = ("Status", "Present", "Absent")
        self.attend_combo.current(0)
        self.attend_combo.grid(row=3, column=1, padx=10, pady=5, sticky=W)


        # Button Frame
        btn_frame = Frame(left_inside_frame, bd=2, bg="white", relief=RIDGE)
        btn_frame.place(x=0, y=202, width=642, height=34)

        import_btn = Button(btn_frame, text="Import CSV", command=self.import_csv, width=19, font=("open sans", 10, "bold"), bg="green", fg="white")
        import_btn.grid(row=0, column=0)
        
        export_btn = Button(btn_frame, text="Export CSV", command=self.export_csv, width=19, font=("open sans", 10, "bold"), bg="blue", fg="white")
        export_btn.grid(row=0, column=1)
        
        update_btn = Button(btn_frame, text="Update", width=19, font=("open sans", 10, "bold"), bg="darkorange", fg="white")
        update_btn.grid(row=0, column=2)
        
        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=18, font=("open sans", 10, "bold"), bg="violet", fg="white")
        reset_btn.grid(row=0, column=3)



        # Right Label Frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("open sans", 12, "bold"))
        right_frame.place(x=675, y=3, width=655, height=430)

        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=0, y=3, width=650, height=400)

        # ======= Scroll Bar Table =======
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.attendanceTableReport = ttk.Treeview(table_frame, column=("id", "rollno", "name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendanceTableReport.xview)
        scroll_y.config(command=self.attendanceTableReport.yview)

        self.attendanceTableReport.heading("id", text="Attendance ID")
        self.attendanceTableReport.heading("rollno", text="Roll No")
        self.attendanceTableReport.heading("name", text="Name")
        self.attendanceTableReport.heading("department", text="Department")
        self.attendanceTableReport.heading("time", text="Time")
        self.attendanceTableReport.heading("date", text="Date")
        self.attendanceTableReport.heading("attendance", text="Attendance")

        self.attendanceTableReport["show"] = "headings"

        self.attendanceTableReport.column("id", width=80)
        self.attendanceTableReport.column("rollno", width=80)
        self.attendanceTableReport.column("name", width=80)
        self.attendanceTableReport.column("department", width=80)
        self.attendanceTableReport.column("time", width=80)
        self.attendanceTableReport.column("date", width=80)
        self.attendanceTableReport.column("attendance", width=80)

        self.attendanceTableReport.pack(fill=BOTH, expand=1)

        self.attendanceTableReport.bind("<ButtonRelease>", self.get_cursor)
        # self.fetch_data()

    # ============= Fetch Data =================

    def fetchData(self, rows):
        self.attendanceTableReport.delete(*self.attendanceTableReport.get_children())
        for i in rows:
            self.attendanceTableReport.insert("", END, value=i)

    # Import CSV Function
    def import_csv(self):
        global mydata
        mydata.clear()
        file_name = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
        with open(file_name) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # Export CSV Function
    def export_csv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data", "No Data Found to Export!!!", parent=self.root)
                return False
            
            file_name = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
            with open(file_name, mode="w", newline="") as myfile:
                export_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    export_write.writerow(i)

                messagebox.showinfo("Data Export", "Your data exported to "+os.path.basename(file_name)+" successfully.")

        except Exception as es:
            messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)

    # ============ Update Function ==============
    """def update_data(self):
        try:
            update_info = messagebox.askyesno("Update", "Do you want to update this attendance details?", parent=self.root)
            if update_info > 0:
                self.var_attend_id.get()
                self.var_rollno.get()
                self.var_name.get()
                self.var_depart.get()
                self.var_time.get()
                self.var_date.get()
                self.var_attendance.get()
                
            else:
                if not update_info:
                    return
            
            messagebox.showinfo("Success", "Attendance details updated successfully", parent=self.root)
    
        except Exception as es:
                messagebox.showerror("Error", f"Dut to : {str(es)}", parent=self.root)"""

    # Cursor Function
    def get_cursor(self, event=""):
        cursor_row = self.attendanceTableReport.focus()
        content = self.attendanceTableReport.item(cursor_row) 
        rows = content['values']
        self.var_attend_id.set(rows[0])
        self.var_rollno.set(rows[1])
        self.var_name.set(rows[2])
        self.var_depart.set(rows[3])
        self.var_time.set(rows[4])
        self.var_date.set(rows[5])
        self.var_attendance.set(rows[6])

    # Reset Function
    def reset_data(self):
        self.var_attend_id.set("")
        self.var_rollno.set("")
        self.var_name.set("")
        self.var_depart.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance.set("")

if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root) 
    root.mainloop()