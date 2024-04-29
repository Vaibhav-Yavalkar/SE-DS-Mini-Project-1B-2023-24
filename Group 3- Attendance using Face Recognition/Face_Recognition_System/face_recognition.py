import re
from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
#from face3 import dispcam

from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np



class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbl = Label(self.root, text="FACE  RECOGNITION", font=("times new roman", 35, "bold"), bg="white",fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # 1st Image
        img_top = Image.open(r"C:\Users\Prachi\OneDrive\Desktop\Face_Recognition_System\image\face3.jpg")
        img_top = img_top.resize((650, 700))
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)

        # 2nd Image
        img_bottom = Image.open(r"C:\Users\Prachi\OneDrive\Desktop\Face_Recognition_System\image\face2.jpg")
        img_bottom = img_bottom.resize((950, 700))
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=55, width=950, height=700)

        # button
        b1_1 = Button(f_lbl,text="Face Recognition",command=self.face_recog, cursor="hand2", font=("times new roman", 18, "bold"), bg="red",fg="white") # command = dispcam,
        b1_1.place(x=365, y=620, width=200, height=40)
        
         #***********************attendance function*********************
    def mark_attendance(self, i, r, n, d):  # i,r,n,d are the data to be taken
        with open("attendance.csv", "r+", newline="\n") as f:
            # to save data in csv(excel) file
            myDataList = f.readlines()  # data is read in myDataList
            name_list = []  # empty list to store data
            # to store data from myDataList to name_list,loop is run
            for line in myDataList:
                entry = line.split((','))  # renuka,ds
                name_list.append(entry[0])
            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
        
        #========= Face Recognition =============

    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                #if confidence>77:
                conn = mysql.connector.connect(host="localhost", username="root", password="@group1816",database="face_recognition")
                my_cursor = conn.cursor()
                   
                my_cursor.execute("select Name from student where ID="+str(id))
                n=my_cursor.fetchone()
                n = "+".join(n) if n is not None else "Unknown"
            

                my_cursor.execute("select Roll from student where ID="+str(id))
                r=my_cursor.fetchone()
                r = "+".join(r) if r is not None else "Unknown"
                        

                my_cursor.execute("select Dep from student where ID="+str(id))
                d=my_cursor.fetchone()
                d = "+".join(d) if d is not None else "Unknown"
                       
                    # to get student_id on attendance sheet
                    
                my_cursor.execute("select ID from student where ID=" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(i) if i is not None else "Unknown"
                       
                    
                    
                #print(confidence)
                if confidence > 77:
                    '''if id==1:
                        i=22107018
                        r=42
                        n='Prachi'
                        d='Data Science' 
                    '''       
                    #cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                    cv2.putText(img,f"ID:{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Dep:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i, r, n, d)
                    #else:
                       # pass
                    '''
                    my_cursor.execute("SELECT Name, Roll, Dep FROM student WHERE ID = %s", (id,))
                    result = my_cursor.fetchone()
                    if result:
                        name, roll, dep = result

                        cv2.putText(img, f"ID: {id}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 3)
                        cv2.putText(img, f"Name: {name}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 3)
                        cv2.putText(img, f"Roll: {roll}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 3)
                        cv2.putText(img, f"Dep: {dep}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 3)
                        break
                    '''
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    
                    

    # to get student_id on attendance sheet
                    #my_cursor.execute("select Student_id from student where Student_id=" + str(id))
                    #i = my_cursor.fetchone()
                    #i = "+".join(i)

                coord = [x, y, w, h]

            return coord


        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img,faceCascade,1.1,10,(255, 25, 255),"Face",clf)
            return img


        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0, cv2.CAP_DSHOW)
        video_cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
        video_cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)

        while True:
            ret,img = video_cap.read(0)
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)

            if cv2.waitKey(1)== 13:
                break

        video_cap.release()
        cv2.destroyALLWindows()


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()