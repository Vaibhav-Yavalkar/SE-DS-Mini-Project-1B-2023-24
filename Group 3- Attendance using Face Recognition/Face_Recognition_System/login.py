from tkinter import*
from main import Face_Recognition_System
from tkinter import messagebox

root=Tk()
root.geometry("1530x790")
root.configure(bg='cyan4')

label1=Label(root,text='Login Page',bg='cyan4',fg='cyan',font=('Arial',50,'bold'))
label1.place(x=520,y=20)

label2=Label(root,text='Username', font=('Arial',32,'bold'), bg='cyan4',fg='white')
label2.place(x=300, y=200)

label3=Label(root,text='Password', font=('Arial',32,'bold'), bg='cyan4',fg='white')
label3.place(x=300, y=300)

entry1 = Entry(root,font=('Arial',32,'bold'))
entry1.place(x= 600, y=200)

entry2 = Entry(root,font=('Arial',32,'bold'), show = "*")
entry2.place(x= 600, y=300)

def loginn():
    un = entry1.get()
    pw = entry2.get()
    if un=='admin' and pw=='1234':
        print("SUCCESS")
        obj1 = Toplevel(root)
        obj2 = Face_Recognition_System(obj1)
        root.iconify()


    else:
        print("Wrong Input")


button1=Button(root, text='Login', font=('Arial',20,'bold'), command=loginn)
button1.place(x=600, y=400)







root.mainloop()