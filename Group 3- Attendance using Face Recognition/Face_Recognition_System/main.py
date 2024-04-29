import tkinter
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
from student import Student
from attendance import Attendance
from face_recognition import Face_Recognition
from train import Train


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        img=Image.open(r"C:\Users\Prachi\OneDrive\Desktop\Face_Recognition_System\image\main1.jpg")
        img=img.resize((500,130))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        img1 = Image.open(r"C:\Users\Prachi\OneDrive\Desktop\Face_Recognition_System\image\main3.jpg")
        img1 = img1.resize((530, 130))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=530, height=130)

        img2 = Image.open(r"C:\Users\Prachi\OneDrive\Desktop\Face_Recognition_System\image\main2.jpg")
        img2 = img2.resize((500, 130))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1030, y=0, width=500, height=130)

        img3 = Image.open(r"C:\Users\Prachi\OneDrive\Desktop\Face_Recognition_System\image\bg.jpg")
        img3 = img3.resize((1530, 710))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        #title
        title_lbl = Label(bg_img,text="FACIAL ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        #student detail
        img4 = Image.open(r"C:\Users\Prachi\OneDrive\Desktop\Face_Recognition_System\image\student4.jpg")
        img4 = img4.resize((220,220))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=250,y=100,width=220,height=220)

        b1_1=Button(bg_img, text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white", command=self.openpage)
        b1_1.place(x=250,y=300,width=220,height=40)


        #facial attendance
        img5 = Image.open(r"C:\Users\Prachi\OneDrive\Desktop\Face_Recognition_System\image\face1.jpg")
        img5 = img5.resize((220, 220))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2")
        b1.place(x=650, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Face Recognition", cursor="hand2", font=("times new roman", 15, "bold"), bg="blue",fg="white",command=self.openimg)#command=self.openimg
        b1_1.place(x=650, y=300, width=220, height=40)


        #attendace
        img6 = Image.open(r"C:\Users\Prachi\OneDrive\Desktop\Face_Recognition_System\image\attendance5.jpg")
        img6 = img6.resize((220, 220))
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2")
        b1.place(x=1050, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Attendance", cursor="hand2", font=("times new roman", 15, "bold"), bg="blue",fg="white",command=self.openatten)
        b1_1.place(x=1050, y=300, width=220, height=40)


        #Photos
        img7 = Image.open(r"C:\Users\Prachi\OneDrive\Desktop\Face_Recognition_System\image\photo.jpg")
        img7 = img7.resize((220,220))
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=250,y=380,width=220,height=220)

        b1_1=Button(bg_img, text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=250,y=580,width=220,height=40)


        #Train
        img8 = Image.open(r"C:\Users\Prachi\OneDrive\Desktop\Face_Recognition_System\image\data1.jpg")
        img8 = img8.resize((220, 220))
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2")
        b1.place(x=650, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Train Data", cursor="hand2", font=("times new roman", 15, "bold"), bg="blue", fg="white",command=self.opentrain)
        b1_1.place(x=650, y=580, width=220, height=40)


        #Exit
        img9 = Image.open(r"C:\Users\Prachi\OneDrive\Desktop\Face_Recognition_System\image\exit.jpg")
        img9 = img9.resize((220, 220))
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2")
        b1.place(x=1050, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Exit", cursor="hand2",command=self.iExit, font=("times new roman", 15, "bold"), bg="blue",fg="white")
        b1_1.place(x=1050, y=580, width=220, height=40)

    def open_img(self):
        os.startfile("data")
    #    pass

    #
    # def b1_1(self):
    #     self.new_window=Toplevel(self.root)
    #     self.app=Student(self.new_window)

    #==================== function buttons=================

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Face Recognition", "Are you sure exit this project", parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return

    def openpage(self):
        print("TEST")
        self.stu = Toplevel(self.root)
        self.stu2 = Student(self.stu)
       # self.root.iconify()

    def openatten(self):
        self.atten=Toplevel(self.root)
        self.atten2=Attendance(self.atten)
        #self.root.iconify()

    def openimg(self):
        self.face=Toplevel(self.root)
        self.face2=Face_Recognition(self.face)
        #self.root.iconify()

    def opentrain(self):
        self.data=Toplevel(self.root)
        self.data2=Train(self.data)
        #self.root.iconify()


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()

