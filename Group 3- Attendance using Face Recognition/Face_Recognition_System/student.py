
import re
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #======================== Variables ==========================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_name = StringVar()
        self.var_id = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_add = StringVar()
        self.var_teacher = StringVar()

        img = Image.open(r"C:\Users\Prachi\OneDrive\Desktop\Face_Recognition_System\image\student1.jpg")
        img = img.resize((500, 130))
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        img1 = Image.open(r"C:\Users\Prachi\OneDrive\Desktop\Face_Recognition_System\image\student3.jpg")
        img1 = img1.resize((530, 130))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=530, height=130)

        img2 = Image.open(r"C:\Users\Prachi\OneDrive\Desktop\Face_Recognition_System\image\student2.jpg")
        img2 = img2.resize((500, 130))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1030, y=0, width=500, height=130)

        img3 = Image.open(r"C:\Users\Prachi\OneDrive\Desktop\Face_Recognition_System\image\bg.jpg")
        img3 = img3.resize((1530, 710))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        # title
        title_lbl = Label(bg_img, text="STUDENT DETAIL", font=("times new roman", 35, "bold"), bg="white",fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10, y=48, width=1505, height=600)


        #left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12,"bold"))
        Left_frame.place(x=10,y=9,width=780,height=580)

        img4 = Image.open(r"C:\Users\Prachi\OneDrive\Desktop\Face_Recognition_System\image\student5.jpg")
        img4 = img4.resize((770, 130))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        f_lbl = Label(Left_frame, image=self.photoimg4)
        f_lbl.place(x=3, y=0, width=770, height=130)

        #current course
        current_course_frame=LabelFrame(Left_frame,bd=2, bg="white", relief=RIDGE ,text="Current Course", font=("times new roman",12,"bold"))
        current_course_frame.place(x=3,y=135,width=770,height=110)

        #Department
        dep_label=Label(current_course_frame,text="Department", font=("times new roman",12,"bold"), bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",11),state="readonly")
        dep_combo["values"]=("Select Department","Data Science","IT","COMPS","Civil","Mechanical","EXTC")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
        course_label=Label(current_course_frame, text="Course", font=("times new roman",12,"bold"), bg="white" )
        course_label.grid(row=0, column=2, padx=10)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course, font=("times new roman", 11), state="readonly")
        course_combo["values"] = ("Select Course", "FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        #Year
        year_label = Label(current_course_frame, text="Year", font=("times new roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10)

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year, font=("times new roman", 11), state="readonly")
        year_combo["values"] = ("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        #Semester
        sem_label = Label(current_course_frame, text="Semester", font=("times new roman", 12, "bold"), bg="white")
        sem_label.grid(row=1, column=2, padx=10)

        sem_combo = ttk.Combobox(current_course_frame,textvariable=self.var_sem, font=("times new roman", 11), state="readonly")
        sem_combo["values"] = ("Select Semester", "I", "II", "III", "IV", "V", "VI", "VII", "VIII")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # class student information
        class_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
        class_frame.place(x=3, y=245, width=770, height=310)

        #Student ID
        stdID_label = Label(class_frame, text="Student ID", font=("times new roman", 12, "bold"), bg="white")
        stdID_label.grid(row=0, column=2, padx=10, pady=4, sticky=W)

        stdID_entry=ttk.Entry(class_frame, width=20,textvariable=self.var_id, font=("times new roman",11))
        stdID_entry.grid(row=0,column=3,padx=10,sticky=W)

        # Student name
        std_name_label = Label(class_frame, text="Student Name", font=("times new roman", 12, "bold"), bg="white")
        std_name_label.grid(row=0, column=0, padx=10, pady=4, sticky=W)

        std_name_entry = ttk.Entry(class_frame, width=20,textvariable=self.var_name, font=("times new roman", 11))
        std_name_entry.grid(row=0, column=1, padx=10, sticky=W)

        # Student div
        std_div_label = Label(class_frame, text="Division", font=("times new roman", 12, "bold"), bg="white")
        std_div_label.grid(row=1, column=0, padx=10, pady=4, sticky=W)

        #std_div_entry = ttk.Entry(class_frame, width=20,textvariable=self.var_div, font=("times new roman", 11))
        #std_div_entry.grid(row=1, column=1, padx=10, sticky=W)

        div_combo = ttk.Combobox(class_frame, textvariable=self.var_div, font=("times new roman", 11),state="readonly",width=18)
        div_combo["values"] = ("Select Division","A", "B", "C","D","E")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        # Student roll no
        std_roll_label = Label(class_frame, text="Roll No", font=("times new roman", 12, "bold"), bg="white")
        std_roll_label.grid(row=1, column=2, padx=10, pady=4, sticky=W)

        std_roll_entry = ttk.Entry(class_frame, width=20,textvariable=self.var_roll, font=("times new roman", 11))
        std_roll_entry.grid(row=1, column=3, padx=10, sticky=W)

        #Gender
        gender_label = Label(class_frame, text="Gender", font=("times new roman", 12, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=4, sticky=W)

        #gender_entry = ttk.Entry(class_frame, width=20,textvariable=self.var_gender, font=("times new roman", 11))
        #gender_entry.grid(row=2, column=1, padx=10, sticky=W)

        gender_combo = ttk.Combobox(class_frame, textvariable=self.var_gender, font=("times new roman", 11),state="readonly",width=18)
        gender_combo["values"] = ("Select Gender","Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        #DOB
        dob_label = Label(class_frame, text="DOB", font=("times new roman", 12, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=4, sticky=W)

        dob_entry = ttk.Entry(class_frame, width=20,textvariable=self.var_dob, font=("times new roman", 11))
        dob_entry.grid(row=2, column=3, padx=10, sticky=W)

        # email ID
        email_label = Label(class_frame, text="Email ID", font=("times new roman", 12, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=4, sticky=W)

        email_entry = ttk.Entry(class_frame, width=20,textvariable=self.var_email, font=("times new roman", 11))
        email_entry.grid(row=3, column=1, padx=10, sticky=W)

        # Phone no
        phone_label = Label(class_frame, text="Phone No", font=("times new roman", 12, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=4, sticky=W)

        phone_entry = ttk.Entry(class_frame, width=20,textvariable=self.var_phone, font=("times new roman", 11))
        phone_entry.grid(row=3, column=3, padx=10, sticky=W)

        # Address
        add_label = Label(class_frame, text="Address", font=("times new roman", 12, "bold"), bg="white")
        add_label.grid(row=4, column=0, padx=10, pady=4, sticky=W)

        add_entry = ttk.Entry(class_frame, width=20,textvariable=self.var_add, font=("times new roman", 11))
        add_entry.grid(row=4, column=1, padx=10, sticky=W)

        # Teacher
        teacher_label = Label(class_frame, text="Teacher Name", font=("times new roman", 12, "bold"), bg="white")
        teacher_label.grid(row=4, column=2, padx=10, pady=4, sticky=W)

        teacher_entry = ttk.Entry(class_frame, width=20,textvariable=self.var_teacher, font=("times new roman", 11))
        teacher_entry.grid(row=4, column=3, padx=10, sticky=W)

        #radio button
        self.var_radio1=StringVar(value="No")
        radiobtn1=ttk.Radiobutton(class_frame,variable=self.var_radio1, text="Take Photo Sample", value="Yes", )
        radiobtn1.grid(row=5,column=1)

        radiobtn2 = ttk.Radiobutton(class_frame,variable=self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=5, column=2)

        #button frame
        btn_frame=Frame(class_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=210,width=765,height=60)

        save_btn=Button(btn_frame,width=20, text="Save",command=self.add_data,font=("times new roman",11,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame, width=20, text="Update",command=self.update_data, font=("times new roman", 11, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, width=20, text="Delete",command=self.delete_data, font=("times new roman", 11, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, width=20, text="Reset",command=self.reset_data, font=("times new roman", 11, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        btn_frame1=Frame(class_frame, bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=240,width=765,height=30)

        photo_btn = Button(btn_frame1, width=20,command=self.generate_dataset, text="Take Photo Sample", font=("times new roman", 11, "bold"), bg="blue",fg="white")
        photo_btn.grid(row=0, column=0)

        update_photo_btn = Button(btn_frame1, width=20, text="Update Photo Sample", font=("times new roman", 11, "bold"), bg="blue",fg="white")
        update_photo_btn.grid(row=0, column=1)

        # Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",font=("times new roman", 12, "bold"))
        Right_frame.place(x=800, y=9, width=700, height=580)

        img5 = Image.open(r"C:\Users\Prachi\OneDrive\Desktop\Face_Recognition_System\image\student5.jpg")
        img5 = img5.resize((690, 130))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        f_lbl = Label(Right_frame, image=self.photoimg5)
        f_lbl.place(x=3, y=0, width=690, height=130)

        '''
        #search
        Search_frame=LabelFrame(Right_frame, bd=2,bg="white", relief=RIDGE, text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=3,y=135,width=690,height=65)

        Search_label = Label(Search_frame, text="Search By:", font=("times new roman", 12, "bold"), bg="red",fg="white")
        Search_label.grid(row=0, column=0, padx=10, pady=4, sticky=W)

        Search_combo = ttk.Combobox(Search_frame, font=("times new roman", 11), state="readonly")
        Search_combo["values"] = ("Select", "Roll No", "Phone No")
        Search_combo.current(0)
        Search_combo.grid(row=0, column=1, padx=2, pady=4, sticky=W)

        Search_entry = ttk.Entry(Search_frame, width=20, font=("times new roman", 11))
        Search_entry.grid(row=0, column=2, padx=5,pady=5, sticky=W)

        Search_btn = Button(Search_frame, width=13, text="Search", font=("times new roman", 11, "bold"), bg="blue",fg="white")
        Search_btn.grid(row=0, column=3,padx=2)

        show_btn = Button(Search_frame, width=12, text="Show All", font=("times new roman", 11, "bold"), bg="blue",fg="white")
        show_btn.grid(row=0, column=4,padx=2)
        '''
        #================table frame=================
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=3, y=150, width=690, height=390)

        #table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        #table_frame.place(x=5, y=5, width=685, height=550)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame, column=("id", "name", "roll", "dep", "course","div", "sem", "year","gender","dob","email","phone","add","teacher","photo"), xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("id", text="Moodle Id")
        self.student_table.heading("roll", text="Roll")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("add", text="Address")
        self.student_table.heading("email", text="Email Id")
        self.student_table.heading("phone", text="Phone No")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("teacher", text="Teacher Name")
        self.student_table.heading("photo", text="Photo")

        self.student_table["show"] = "headings"

        self.student_table.column("id", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("dep", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("add", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    #============================ Function Declaration =============================
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="@group1816",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                               self.var_id.get(),
                                                                                                                               self.var_name.get(),
                                                                                                                               self.var_roll.get(),
                                                                                                                               self.var_dep.get(),
                                                                                                                               self.var_course.get(),
                                                                                                                               self.var_div.get(),
                                                                                                                               self.var_sem.get(),
                                                                                                                               self.var_year.get(),
                                                                                                                               self.var_gender.get(),
                                                                                                                               self.var_dob.get(),
                                                                                                                               self.var_email.get(),
                                                                                                                               self.var_phone.get(),
                                                                                                                               self.var_add.get(),
                                                                                                                               self.var_teacher.get(),
                                                                                                                               self.var_radio1.get()

                                                                                                          ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)


    #===============fetch data===============
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="@group1816",database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #=============get cursor==================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_id.set(data[0]),
        self.var_name.set(data[1]),
        self.var_roll.set(data[2]),
        self.var_dep.set(data[3]),
        self.var_course.set(data[4]),
        self.var_div.set(data[5]),
        self.var_sem.set(data[6]),
        self.var_year.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_add.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    #update function
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details?",parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="@group1816",database="face_recognition")
                    my_cursor = conn.cursor()
                    
                    my_cursor.execute("UPDATE student SET  Name=%s, Roll=%s, Dep=%s, Course=%s, `Div`=%s, Sem=%s, Year=%s, Gender=%s,DOB=%s, Email=%s, Phone=%s, Addr=%s, Teacher=%s,Photo=%s where ID=%s;",(

                                                                                                                                                                self.var_name.get(),
                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                self.var_sem.get(),
                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                self.var_add.get(),
                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                self.var_id.get()
                                                                                                                                                                ))
                    
                    #mysqlquery = "UPDATE student SET Name=%s, Roll=%s, Dep=%s, Course=%s, `Div`=%s, Sem=%s, Year=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Addr=%s, Teacher=%s, Photo=%s WHERE ID=%s;"
                    #mysqldata = (self.var_name.get(), self.var_roll.get(), self.var_dep.get(), self.var_course.get(), self.var_div.get(), self.var_sem.get(), self.var_year.get(), self.var_gender.get(), self.var_dob.get(), self.var_email.get(), self.var_phone.get(), self.var_add.get(), self.var_teacher.get(), self.var_radio1.get(), self.var_id.get())
                    #print(mysqlquery.format(mysqldata))
                    #my_cursor.execute(mysqlquery, mysqldata)
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Student details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #delete function
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student details?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="@group1816",database="face_recognition")
                    my_cursor = conn.cursor()
                    sql = "delete from student where ID=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully deleted student detail", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #Reset
    def reset_data(self):
        self.var_id.set("")
        self.var_name.set("")
        self.var_roll.set("")
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_div.set("Select Division")
        self.var_sem.set("Select Semester")
        self.var_year.set("Select Year")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_add.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    # =========================== Generate data set or Take photo Samples ====================
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="@group1816",database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                #id = len(myresult)
                #print(myresult[0])
               # print("\n\n", type(self.var_radio1.get()), self.var_radio1)
                id = 0
                for x in myresult:
                    id += 1
                #print(self.var_email.get())
                #mysqlquery = "UPDATE student SET Name=%s, Roll=%s, Dep=%s, Course=%s, `Div`=%s, Sem=%s, Year=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Addr=%s, Teacher=%s, Photo=%s WHERE ID=%s;"
                #mysqldata = (self.var_name.get(), self.var_roll.get(), self.var_dep.get(), self.var_course.get(), self.var_div.get(), self.var_sem.get(), self.var_year.get(), self.var_gender.get(), self.var_dob.get(), self.var_email.get(), self.var_phone.get(), self.var_add.get(), self.var_teacher.get(), self.var_radio1.get(), self.var_id.get())
                #print(mysqlquery.format(mysqldata))
                #my_cursor.execute(mysqlquery, mysqldata)
                my_cursor.execute("UPDATE student SET  Name=%s, Roll=%s, Dep=%s, Course=%s, `Div`=%s, Sem=%s, Year=%s, Gender=%s,DOB=%s, Email=%s, Phone=%s, Addr=%s, Teacher=%s,Photo=%s where ID=%s;",(

                                                                                                                                                                self.var_name.get(),
                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                self.var_sem.get(),
                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                self.var_add.get(),
                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                self.var_id.get()==id+1
                                                                                                                                                                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ================ Load predifiend data on face frontals from opencv ==================

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                # scaling factor=1.3
                # Minimun Neighbor=5

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x + w]
                        return face_cropped

                cap = cv2.VideoCapture(0)  # open web camera
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+= 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)  # convert color img to gray
                        file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id),(50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindow()
                messagebox.showinfo("Result", "Generating data sets completed!!!")

            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()