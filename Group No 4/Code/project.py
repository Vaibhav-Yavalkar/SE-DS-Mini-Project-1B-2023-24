from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector
from tkinter import _setit
from tkinter import ttk

images = []
exerinfo = []
exername = []
            

#Start Page
class StartPage(Tk):

    def __init__(self):
        super().__init__()
        self.geometry('1080x720+240+40')
        self.resizable(0,0)
        self.title("Start Screen")
        self.initcomponents()

    def initcomponents(self):
        self.panBg = PanedWindow(self, bg = "#56ABBA", width = 1080, height = 720)
        self.panBg.grid(column = 0, row = 0, columnspan = 100, rowspan = 100)
        
        Button(self, text="Login", command=self.launch).grid(column=35, row=35, columnspan=12, rowspan=7, sticky=NSEW)
        Button(self, text="Calculator", command=self.opencalc).grid(column=53, row=35, columnspan=12, rowspan=7, sticky=NSEW)
    

    def launch(self):
        self.iconify()
        loginpage = LoginPage(self)
        loginpage.focus_set()

    def opencalc(self):
        self.iconify()
        calc = Calculator(self)
        calc.focus_set()


#Login Page
class LoginPage(Toplevel):  

    def __init__(self, root):
        self.root = root
        super().__init__(self.root)
        self.geometry('1080x720+240+40')
        self.title("Login Page")
        self.resizable(0,0)
        self.initcomponents()

        Button(self,text="Back", command=self.backToStart, bg="#FFFFFF", fg="#000000", font='roboto 16 bold', relief='raised'). grid(column=88, row=93, columnspan=10, rowspan=5, sticky=NSEW)

    
    def initcomponents(self):

        #bg:982AF8
        attr = {'bg': '#FFFFFF', 'fg':'#000000'}

        self.bgphoto = ImageTk.PhotoImage(Image.open("D:\\Codes\\MiniProject1B\\LoginpageBG.jpg"))
        Label(self,image=self.bgphoto).grid(column=0,row=0,columnspan=100,rowspan=100,sticky=NSEW)

        self.panFields = PanedWindow(self, bg='#FFFFFF',border=4, orient='vertical',  width=360, height=480, relief='ridge')
        self.panFields.grid(column=65,row=20, columnspan=25, rowspan=60, sticky=NSEW)

        #Login Area
        self.lblFill1 = Label(self, bg='#FFFFFF', height=2)
        self.panFields.add(self.lblFill1)

        #Username Fields
        self.lblUsername = Label(self, text="Username: ", height=2, anchor= 'w', padx=15, font=('ariel', 12, 'bold'),**attr)
        self.panFields.add(self.lblUsername)

        self.entUsename = Entry(self, **attr, bd=1, font=('ariel'), relief='solid')
        self.panFields.add(self.entUsename)
        
        #Password Fields
        self.lblPassword = Label(self, text="Password: ", height=2, **attr, anchor= 'w', font=('ariel', 12, 'bold'), padx=15)
        self.panFields.add(self.lblPassword)

        self.entPassword = Entry(self, **attr,show='*', bd=1, font=('ariel'), relief='solid')
        self.panFields.add(self.entPassword)
        

        self.lblFill2 = Label(self, bg='#FFFFFF', height=10)
        self.panFields.add(self.lblFill2)

        #Button Panel
        self.panButtons = PanedWindow(self, bg='#FFFFFF', height=50, bd=10, orient='horizontal')
        self.panFields.add(self.panButtons)

        self.btnLogin = Button(self, text="Login", relief='raised', bd=2, bg='#15A3C7', fg='#000000', font=('ariel', 12, 'bold'), width=9, command=self.getLoginCreds)
        self.panButtons.add(self.btnLogin)

        self.btnSignup = Button(self, text="Sign Up", relief='raised', bd=2, bg='#15A3C7', fg='#000000', font=('ariel', 12, 'bold'), command=self.goToSignUpPage)
        self.panButtons.add(self.btnSignup)

    def getLoginCreds(self):
        #Check if fields are filled
        if len(self.entUsename.get()) == 0 or len(self.entPassword.get()) == 0:
            messagebox.showwarning(title="No Input", message="Please type your credentials")
        else:
            un = self.entUsename.get()
            pw = self.entPassword.get()
            self.entUsename.delete(0,END)
            self.entPassword.delete(0,END)
            
            
            try:
            #Create databse connection
                loginConnection = mysql.connector.connect(host = 'localhost', username = 'root', password = 'siddhesh@2204', database = 'pythonproject')
                getCredentialsCursor = loginConnection.cursor()

            #Sql Query
                getCredentialsQuery = 'select * from login where username = %s and password = %s'
                getCredentialsValue = (un, pw)
                getCredentialsCursor.execute(getCredentialsQuery, getCredentialsValue)

            #Get Result
                getCredentialsResult = getCredentialsCursor.fetchone()

            #Verify if User exists
                if getCredentialsResult:
                    self.withdraw()
                    home = HomePage(un,self.root)
                    home.focus_set()
                else:
                    messagebox.showerror(title='Login Failed', message='Invalid Credentials')

                loginConnection.close()
                getCredentialsCursor.close()

            except Exception as e:
                messagebox.showerror(message=e)

    def goToSignUpPage(self):
        self.withdraw()
        signup = SignupPage(self.root)
        signup.focus_set()

    def backToStart(self):
        self.withdraw()
        self.root.deiconify()
        self.root.focus_set()


#Signup Page
class SignupPage(Toplevel):

    def __init__(self, root):
        self.root = root
        super().__init__()
        self.geometry('1080x720+240+40')
        self.resizable(0,0)
        self.title("SignUp Page")
        self.initcomponents()

    def initcomponents(self):
        # self.panBg = PanedWindow(self, bg = "#4E048E", width = 1080, height = 720)
        # self.panBg.grid(column = 0, row = 0, columnspan = 100, rowspan = 100)
        attr = {'fg':'black', 'bg':'white'}
        self.bgphoto = ImageTk.PhotoImage(Image.open("D:\\Codes\\MiniProject1B\\LoginpageBG.jpg"))
        Label(self,image=self.bgphoto).grid(column=0,row=0,columnspan=100,rowspan=100,sticky=NSEW)

        self.panComponents = PanedWindow(self, bg = "#FFFFFF", border=4, orient='vertical',  width=360, height=480, relief='ridge')
        self.panComponents.grid(column = 65, row = 20, columnspan = 25, rowspan = 60, sticky = NSEW)


        self.lblFill1 = Label(self, **attr, height = 1)
        self.panComponents.add(self.lblFill1)

    #Username Fields
        self.lblUsername = Label(self, text = 'Username:', height=2, **attr, anchor= 'w', font=('ariel', 12, 'bold'), padx=15)
        self.panComponents.add(self.lblUsername)
	
        self.entUsename = Entry(self, **attr, bd=1, font=('ariel'), relief = 'solid')
        self.panComponents.add(self.entUsename)
	
    #Password fields
        self.lblPassword = Label(self, text="Password: ", height=2, **attr, anchor= 'w', font=('ariel', 12, 'bold'), padx=15)
        self.panComponents.add(self.lblPassword)

        self.entPassword = Entry(self, **attr,show='*', bd=1, font=('ariel'), relief = 'solid')
        self.panComponents.add(self.entPassword)
	
    #Confirm Password Fields
        self.lblConfirmPassword = Label(self, text="Confirm Password: ", height=2, **attr, anchor= 'w', font=('ariel', 12, 'bold'), padx=15)
        self.panComponents.add(self.lblConfirmPassword)

        self.entConfirmPassword = Entry(self, **attr,show='*', bd=1, font=('ariel'), relief = 'solid')
        self.panComponents.add(self.entConfirmPassword)
	
        self.lblFill2 = Label(self, **attr, height = 6)
        self.panComponents.add(self.lblFill2)
    
    #Buttons Panel
        self.panButtons= PanedWindow(self, bg = 'white', bd = 5, orient = 'horizontal')
        self.panComponents.add(self.panButtons)

        self.btnBack = Button(self, text = "Go Back", bg = "#15A3C7", font=('ariel', 12, 'bold'), bd = 3, relief = RAISED, command = self.gotologin, width = 10)
        self.panButtons.add(self.btnBack)
	
        self.btnsignup = Button(self, text = "Sign Up", bg = "#15A3C7", font=('ariel', 12, 'bold'), bd = 3, relief = RAISED, command = self.storeuserinfo)
        self.panButtons.add(self.btnsignup)

    def gotologin(self):
        self.withdraw()
        loginpage = LoginPage(self.root)
        loginpage.focus_set()

    def storeuserinfo(self):
        un = self.entUsename.get()
        pw = self.entPassword.get()
        cpw = self.entConfirmPassword.get()

        #Check if user filled all fields
        if pw == cpw and len(un) != 0 and len(pw) >= 6:

            
            
            try:
            #Create Connection
                signupconnection = mysql.connector.connect(host = "localhost", username ="root", password = "siddhesh@2204", database = "pythonproject")
                storesignupcursor = signupconnection.cursor()

            #Create Login Table Query and Execute
                storesignupquery = 'insert into login (username, password) values (%s,%s);'
                storesignupvalues = (un, pw)
                storesignupcursor.execute(storesignupquery, storesignupvalues)
                signupconnection.commit()

            #Create Profile Table Query and Execute
                storeusernamequery = 'insert into profile (username) values (%s);'
                storeusernamevalues = (un,)
                storesignupcursor.execute(storeusernamequery, storeusernamevalues)
                signupconnection.commit()


                messagebox.showinfo(title="Success",message="Account Created Successfully ")
                storesignupcursor.close()
                signupconnection.close()

            #Clear Fields
                self.entUsename.delete(0, END)
                self.entPassword.delete(0,END)
                self.entConfirmPassword.delete(0,END)

            except mysql.connector.errors.IntegrityError:
                messagebox.showerror(title="Error", message="Username already in use, choose another")

            except Exception as e:
                messagebox.showerror(title="Error", message=e)


        else:
            messagebox.showerror(title="Error", message="Fill All Fields Correctly\nPassword should be atleast 6 characters long")


#Home Page
class HomePage(Toplevel):

    def __init__(self, username, root):
        self.root = root
        self.username = username
        super().__init__()
        self.geometry('1080x720+240+40')
        self.resizable(0,0)
        self.title("Home Page")
        self.initcomponents()
    
    def initcomponents(self):
        #BTN: 15A3C7, 
        btnattr = {'bg':'#FFFFFF', 'fg':'#000000', 'relief':'raised', 'bd': '3', 'font': 'roboto'}

        self.panBg = PanedWindow(self, bg = "#73e0e6", width = 1080, height = 720)
        self.panBg.grid(column = 0, row = 0, columnspan = 100, rowspan = 100)

        # self.panOptions = PanedWindow(self, bg = "#3E076E")
        # self.panOptions.grid(column = 0, row = 0, columnspan = 30, rowspan = 100, sticky = NSEW)
	
        self.lblWelcome = Label(self, text = "Welcome,\n" + self.username, font=('ariel', 20, 'bold'), bg = '#15A3C7', fg = '#FFFFFF', relief='ridge', bd = 7)
        self.lblWelcome.grid(column = 34, row = 8, columnspan = 30, rowspan = 17, sticky = NSEW)
	
        #self.lblUsername = Label(self, text = "Welcome,", font = ('ariel', 14), bg = '#AF53FF', fg = '#FFFFFF')
        #self.lblUsername.grid(column = 5, row = 12, columnspan = 9, rowspan = 5, sticky = NSEW)
	
        self.btnButton1 = Button(self, text = "Profile", **btnattr, command=self.openProfile)
        self.btnButton1.grid(column = 10, row = 40, columnspan = 20, rowspan = 7, sticky = NSEW)
	
        self.btnButton2 = Button(self, text = "Search", **btnattr, command=self.openSearch)
        self.btnButton2.grid(column = 40, row = 40, columnspan = 20, rowspan = 7, sticky = NSEW)
	
        self.btnButton3 = Button(self, text = "Favourites", **btnattr, command=self.openFavourites)
        self.btnButton3.grid(column = 25, row = 60, columnspan = 20, rowspan = 7, sticky = NSEW)
	
        self.btnButton4 = Button(self, text = "Calendar", **btnattr, command=self.openCalender)
        self.btnButton4.grid(column = 70, row = 40, columnspan = 20, rowspan = 7, sticky = NSEW)
	
        self.btnButton5 = Button(self, text = "Sign Out", **btnattr, command=self.signout)
        self.btnButton5.grid(column = 55, row = 60, columnspan = 20, rowspan = 7, sticky = NSEW)  

        # self.btnButton6 = Button(self, text = "Calculator", **btnattr, command=self.openCalculator)
        # self.btnButton6.grid(column = 10, row = 60, columnspan = 20, rowspan = 7, sticky = NSEW)      

    def signout(self):
        self.withdraw()
        self.root.deiconify()
        self.root.focus_set()

    def openProfile(self):
        self.withdraw()
        profile = Profile(self.username, self.root)
        profile.focus_set()

    def openSearch(self):
        self.withdraw()
        search = Search(root=self.root, username=self.username)
        search.focus_set()

    def openFavourites(self):
        self.withdraw()
        fav = Favourites(username=self.username, root=self.root)
        fav.focus_set()

    def openCalender(self):
        self.withdraw()
        cal = Calender(username=self.username, root=self.root)
        cal.focus_set()


#Calculator
class Calculator(Toplevel):

    def __init__(self, root):
        self.root = root
        super().__init__()
        self.geometry('1080x720+240+40')
        self.resizable(0,0)
        self.title("Profile")

        self.panBg = PanedWindow(self, bg = "#73e0e6", width = 1080, height = 720)
        self.panBg.grid(column = 0, row = 0, columnspan = 100, rowspan = 100)

        Label(self,text="BMI Calculator", bg="#15A3C7", fg="#FFFFFF", font='roboto 24 bold', relief='raised'). grid(column=14, row=8, columnspan=30, rowspan=10, sticky=NSEW)
        Label(self,text="Calorie Calculator", bg="#15A3C7", fg="#FFFFFF", font='roboto 24 bold', relief='raised'). grid(column=54, row=8, columnspan=30, rowspan=10, sticky=NSEW)
        Button(self,text="Back", command=self.backToHome, bg="#15A3C7", fg="#FFFFFF", font='roboto 16 bold', relief='raised'). grid(column=88, row=93, columnspan=10, rowspan=5, sticky=NSEW)

        self.initBMIFrame()
        self.initCalorieFrame()

    def initBMIFrame(self):

        #6e00cc, 8900FF
        labelattributes = {'bg':'#FFFFFF', 'fg':'#000000', 'anchor':'e', 'relief':'solid', 'bd':'1'}
        entryattributes = {'bg':'#FFFFFF', 'fg':'#000000', 'relief':'solid', 'bd':'1'}

        self.frameBMI = Frame(self, relief='sunken', bd=3)
        self.frameBMI.grid(column=10, row=22, columnspan=38, rowspan=68)

        self.panFrameBMIBg = PanedWindow(self.frameBMI, bg = "#59ABDF", width = 400, height = 480)
        self.panFrameBMIBg.grid(column = 0, row = 0, columnspan = 50, rowspan = 50)

        self.lblBMIHeight = Label(self.frameBMI, text="Enter Height (in cm): ", font='roboto 14 bold', **labelattributes)
        self.lblBMIHeight.grid(column=1,row=5, columnspan=27, rowspan=4, sticky=NSEW)

        self.entBMIHeight = Entry(self.frameBMI,  font='roboto 12 bold', **entryattributes)
        self.entBMIHeight.grid(column = 29, row = 5, columnspan=20, rowspan=4, sticky=NSEW)

        self.lblBMIWeight = Label(self.frameBMI, text="Enter Weight (in kg): ", font='roboto 14 bold', **labelattributes)
        self.lblBMIWeight.grid(column=1,row=15,columnspan=27, rowspan=4,sticky=NSEW)

        self.entBMIWeight = Entry(self.frameBMI,  font='roboto 12 bold', **entryattributes)
        self.entBMIWeight.grid(column = 29, row = 15, columnspan=20, rowspan=4,sticky=NSEW)

        self.btnCalc = Button(self.frameBMI, text="Find BMI", command=self.calcBMI, font='roboto 16 bold', bg='#15A3C7', fg='#FFFFFF', relief='raised', bd=3)
        self.btnCalc.grid(column = 10, row = 25, columnspan = 30, rowspan = 5, sticky=NSEW)

        self.lblBMIResult = Label(self.frameBMI, font='roboto 20 bold', bg = '#FFFFFF', fg = '#000000', relief='ridge', bd=3)
        
    def initCalorieFrame(self):
        
        #6e00cc, #8900FF
        labelattributes = {'bg':'#FFFFFF', 'fg':'#000000', 'anchor':'e', 'relief':'solid', 'bd':'1'}
        entryattributes = {'bg':'#FFFFFF', 'fg':'#000000', 'relief':'solid', 'bd':'1'}
        rdbuttonattributes = {'bg':'#FFFFFF', 'fg':'#000000', 'font':'roboto', 'anchor':'w', 'relief':'solid', 'bd':'1'}

        self.frameCalorie = Frame(self, relief='sunken', bd=3)
        self.frameCalorie.grid(column=50, row=22, columnspan=38, rowspan=68)

        self.panFrameCalorieBg = PanedWindow(self.frameCalorie, bg = "#59ABDF", width = 400, height = 480)
        self.panFrameCalorieBg.grid(column = 0, row = 0, columnspan = 50, rowspan = 50)

        #Gender Radio Buttons
        self.genderselect = IntVar(value=1)

        self.rdoCalorieMale = Radiobutton(self.frameCalorie, text="Male", variable=self.genderselect, value=1, **rdbuttonattributes)
        self.rdoCalorieMale.grid(column=1,row=20, columnspan=20, rowspan=5, sticky=NSEW)


        self.rdoCalorieFemale = Radiobutton(self.frameCalorie, text="Female", variable=self.genderselect, value=2, **rdbuttonattributes)
        self.rdoCalorieFemale.grid(column=1,row=26, columnspan=20, rowspan=5, sticky=NSEW)

        #Activity Radio Buttons
        self.activityselect = DoubleVar(value=1.4)

        self.rdoCalorieActivityLow = Radiobutton(self.frameCalorie, text="Low Activity", variable=self.activityselect, value=1.4, **rdbuttonattributes)
        self.rdoCalorieActivityLow.grid(column=26,row=20, columnspan=22, rowspan=3, sticky=NSEW)

        self.rdoCalorieActivityMedium = Radiobutton(self.frameCalorie, text="Medium Activity", variable=self.activityselect, value=1.55, **rdbuttonattributes)
        self.rdoCalorieActivityMedium.grid(column=26,row=24, columnspan=22, rowspan=3, sticky=NSEW)

        self.rdoCalorieActivityIntense = Radiobutton(self.frameCalorie, text="Intense Activity", variable=self.activityselect, value=1.75, **rdbuttonattributes)
        self.rdoCalorieActivityIntense.grid(column=26,row=28, columnspan=22, rowspan=3, sticky=NSEW)

        #Height Widgets
        self.lblCalorieHeight = Label(self.frameCalorie, text="Enter Height (in cm): ", font='roboto 14 bold', **labelattributes)
        self.lblCalorieHeight.grid(column=1,row=4, columnspan=27, rowspan=4, sticky=NSEW)

        self.entCalorieHeight = Entry(self.frameCalorie,  font='roboto 12 bold', **entryattributes)
        self.entCalorieHeight.grid(column = 29, row = 4, columnspan=20, rowspan=4, sticky=NSEW)

        #Weight Widgets
        self.lblCalorieWeight = Label(self.frameCalorie, text="Enter Weight (in kg): ", font='roboto 14 bold', **labelattributes)
        self.lblCalorieWeight.grid(column = 1, row = 9, columnspan = 27, rowspan = 4, sticky = NSEW)

        self.entCalorieWeight = Entry(self.frameCalorie,  font='roboto 12 bold', **entryattributes)
        self.entCalorieWeight.grid(column = 29, row = 9, columnspan=20, rowspan=4,sticky=NSEW)

        #Age Widgets
        self.lblCalorieAge = Label(self.frameCalorie, text="Enter Age (in years): ", font='roboto 14 bold', **labelattributes)
        self.lblCalorieAge.grid(column = 1, row = 14, columnspan = 27, rowspan = 4, sticky = NSEW)

        self.entCalorieAge = Entry(self.frameCalorie,  font='roboto 12 bold', **entryattributes)
        self.entCalorieAge.grid(column = 29, row = 14, columnspan=20, rowspan=4,sticky=NSEW)

        self.btnCalorieCalc = Button(self.frameCalorie, text="Find Calorie Requirement", command=self.calcCalorieReq, font='roboto 16 bold', bg='#15A3C7', fg='#FFFFFF', relief='raised', bd=3)
        self.btnCalorieCalc.grid(column = 8, row = 35, columnspan = 35, rowspan = 5, sticky=NSEW)

        self.lblCalorieResult = Label(self.frameCalorie, font='roboto 20 bold', bg = '#FFFFFF', fg = '#000000', relief='ridge', bd=3)
      
    def calcBMI(self):


        if (self.entBMIHeight.index("end")==0) or (self.entBMIWeight.index("end")==0):
            messagebox.showerror(title="Empty Fields", message="Enter All Details")
        
        else:
            try:

                height = float(self.entBMIHeight.get())
                weight = float(self.entBMIWeight.get())

                BMI = weight/pow((height/100),2)
                BMI = round(BMI,3)

                self.lblBMIResult.grid(column = 10, row = 35, columnspan = 30, rowspan = 10, sticky=NSEW)
                self.lblBMIResult.config(text="Your BMI is \n {} kg/m2".format(BMI))
            except ValueError:
                messagebox.showerror("Invalid Input", message="Enter Valid Values")

    def calcCalorieReq(self):

        if self.entCalorieHeight.get() and self.entCalorieWeight.get() and self.entCalorieAge.get():
            height = float(self.entCalorieHeight.get())
            weight = float(self.entCalorieWeight.get())
            age = float(self.entCalorieAge.get())

            if int(self.genderselect.get()) == 1:
                reqCal = (13.397*weight) + (4.799*height) - (5.677*age) + 88.362
                reqCal = reqCal * float(self.activityselect.get())
            elif int(self.genderselect.get()) == 2:
                reqCal = (9.247*weight) + (3.098*height) - (4.330*age) + 447.593
                reqCal = reqCal * float(self.activityselect.get())

            reqCal = str(round(reqCal,2)) + " calories/day"
            self.lblCalorieResult.config(text = reqCal)
            self.lblCalorieResult.grid(column = 3, row = 42, columnspan = 45, rowspan = 6, sticky=NSEW)
        else:
            messagebox.showerror(title="Empty Fields" ,message="Enter All Details")

    def backToHome(self):
        self.withdraw()
        self.root.deiconify()


#Profile
class Profile(Toplevel):

    def __init__(self, username, root):

        self.username = username
        self.root = root

        super().__init__()
        self.geometry('1080x720+240+40')
        self.resizable(0,0)
        self.title("Profile")
        
        PanedWindow(self, bg='#73e0e6', width=1080, height=720).grid(column=0, row=0, columnspan=100, rowspan=100)
        Button(self, text="Edit", bg='#15A3C7', fg='#FFFFFF', font='roboto 14 bold', relief='raised', command=self.openedit).grid(column=76, row=90, columnspan=10, rowspan=5, sticky=NSEW)
        Button(self, text="Back", bg='#15A3C7', fg='#FFFFFF', font='roboto 14 bold', relief='raised', command=self.backToHomepage).grid(column=88, row=90, columnspan=10, rowspan=5, sticky=NSEW)

        self.initProfileCreateFrame()
        self.initProfileDisplayFrame()
        self.checkProfile()

    def initProfileCreateFrame(self):
        self.frameProfileCreate = Frame(self, bg='#FFFFFF', bd=5, relief='sunken')
        self.frameProfileCreate.grid(column=35, row=10, columnspan=40, rowspan=80, sticky=NSEW)

        PanedWindow(self.frameProfileCreate, bg='#59ABDF', width=423, height=566).grid(column=0, row=0, columnspan=100, rowspan=100, sticky=NSEW)
        
        #Labels 56ABBA
        lblattr = {'anchor':'e', 'bg':'#59ABDF', 'fg':'#FFFFFF'}

        Label(self.frameProfileCreate, text='Height (in cm): ', font='roboto 16 bold', **lblattr).grid(column=5, row=10, columnspan=45, rowspan=8, sticky=NSEW)
        Label(self.frameProfileCreate, text='Weight (in kg): ', font='roboto 16 bold', **lblattr).grid(column=5, row=25, columnspan=45, rowspan=8, sticky=NSEW)
        Label(self.frameProfileCreate, text='Age (in years): ', font='roboto 16 bold', **lblattr).grid(column=5, row=40, columnspan=45, rowspan=8, sticky=NSEW)

        #Entry Widgets
        entattr = {}

        self.entProfileCreateHeight = Entry(self.frameProfileCreate, font='roboto 14 bold')
        self.entProfileCreateHeight.grid(column=55, row=10, columnspan=40, rowspan=8, sticky=NSEW)

        self.entProfileCreateWeight = Entry(self.frameProfileCreate, font='roboto 14 bold')
        self.entProfileCreateWeight.grid(column=55, row=25, columnspan=40, rowspan=8, sticky=NSEW)

        self.entProfileCreateAge = Entry(self.frameProfileCreate, font='roboto 14 bold')
        self.entProfileCreateAge.grid(column=55, row=40, columnspan=40, rowspan=8, sticky=NSEW)        

        #Gender Radio Buttons
        rdbtnattr = {'relief':'raised', 'bg':'#59ABDF', 'anchor':'w', 'font':'roboto'}
        self.genderProfileCreateSelect = IntVar(self.frameProfileCreate, value=1)

        self.rdbProfileCreateMale = Radiobutton(self.frameProfileCreate, text="Male", variable=self.genderProfileCreateSelect, value=1, **rdbtnattr)
        self.rdbProfileCreateMale.grid(column=5, row=59, columnspan=45, rowspan=8, sticky=NSEW)

        self.rdbProfileCreateFemale = Radiobutton(self.frameProfileCreate, text="Female", variable=self.genderProfileCreateSelect, value=2, **rdbtnattr)
        self.rdbProfileCreateFemale.grid(column=5, row=71, columnspan=45, rowspan=8, sticky=NSEW)

        #Activity Radio Buttons
        self.activityProfileCreateSelect = DoubleVar(self.frameProfileCreate, value=1.4)
        
        self.rdbProfileCreateActivityLow = Radiobutton(self.frameProfileCreate, text='Low Activity', variable=self.activityProfileCreateSelect, value=1.4, **rdbtnattr)
        self.rdbProfileCreateActivityLow.grid(column=55, row=55, columnspan=40, rowspan=8, sticky=NSEW)

        self.rdbProfileCreateActivityMed = Radiobutton(self.frameProfileCreate, text='Medium Activity', variable=self.activityProfileCreateSelect, value=1.55, **rdbtnattr)
        self.rdbProfileCreateActivityMed.grid(column=55, row=65, columnspan=40, rowspan=8, sticky=NSEW)

        self.rdbProfileCreateActivityIntense = Radiobutton(self.frameProfileCreate, text='Intense Activity', variable=self.activityProfileCreateSelect, value=1.75, **rdbtnattr)
        self.rdbProfileCreateActivityIntense.grid(column=55, row=75, columnspan=40, rowspan=8, sticky=NSEW)

        #Create Profile Button
        Button(self.frameProfileCreate, text='Create Profile', command=self.createProfile, font='roboto 16 bold', relief='raised',bd=3, bg='#15A3C7', fg='#FFFFFF').grid(column=30, row=88, columnspan=40, rowspan=8, sticky=NSEW)

    def initProfileDisplayFrame(self):
        self.frameProfileDisplay = Frame(self, bg='#FFFFFF', bd=5, relief='sunken')
        self.frameProfileDisplay.grid(column=20, row=15, columnspan=60, rowspan=70, sticky=NSEW)

        self.panProfileDisplayBG = PanedWindow(self.frameProfileDisplay, bg='#59ABDF', width=638, height=494)
        self.panProfileDisplayBG.grid(column=0, row=0, columnspan=100, rowspan=100, sticky=NSEW)

        #Labels 56ABBA
        lblattr = {'anchor':'e'}

        Label(self.frameProfileDisplay, text='Height (in cm): ', font='roboto 14 bold', **lblattr).grid(column=5, row=10, columnspan=23, rowspan=8, sticky=NSEW)
        Label(self.frameProfileDisplay, text='Weight (in kg): ', font='roboto 14 bold', **lblattr).grid(column=5, row=30, columnspan=23, rowspan=8, sticky=NSEW)
        Label(self.frameProfileDisplay, text='Gender: ', font='roboto 14 bold', **lblattr).grid(column=5, row=50, columnspan=23, rowspan=8, sticky=NSEW)
        Label(self.frameProfileDisplay, text='Age (in years): ', font='roboto 14 bold', **lblattr).grid(column=5, row=70, columnspan=23, rowspan=8, sticky=NSEW)

        #Display Labels
        self.lblProfileDisplayHeight = Label(self.frameProfileDisplay, text='173cm', font='roboto 14 bold')
        self.lblProfileDisplayHeight.grid(column=30, row=10, columnspan=15, rowspan=8, sticky=NSEW)

        self.lblProfileDisplayWeight = Label(self.frameProfileDisplay, text='40cm', font='roboto 14 bold')
        self.lblProfileDisplayWeight.grid(column=30, row=30, columnspan=15, rowspan=8, sticky=NSEW)

        self.lblProfileDisplayGender = Label(self.frameProfileDisplay, text='Male', font='roboto 14 bold')
        self.lblProfileDisplayGender.grid(column=30, row=50, columnspan=15, rowspan=8, sticky=NSEW)

        self.lblProfileDisplayAge = Label(self.frameProfileDisplay, text='19', font='roboto 14 bold')
        self.lblProfileDisplayAge.grid(column=30, row=70, columnspan=15, rowspan=8, sticky=NSEW)
        
        self.lblProfileDisplayBMIResult = Label(self.frameProfileDisplay, text='', font='roboto 16 bold')
        self.lblProfileDisplayBMIResult.grid(column=55, row=40, columnspan=40, rowspan=16, sticky=NSEW)
        
        self.lblProfileDisplayBMI = Label(self.frameProfileDisplay, text='Your Bmi is  kg/m2', font='roboto 16 bold')
        self.lblProfileDisplayBMI.grid(column=55, row=9, columnspan=40, rowspan=16, sticky=NSEW)

        self.lblProfileDisplayCalorieneed = Label(self.frameProfileDisplay, text='Your Daily Calorie\n need is /day', font='roboto 14 bold')
        self.lblProfileDisplayCalorieneed.grid(column=55, row=74, columnspan=40, rowspan=16, sticky=NSEW)

    def checkProfile(self):
        try:
            connProfile = mysql.connector.connect(host = 'localhost', username = 'root', password = 'siddhesh@2204', database = 'pythonproject')
            cursorProfile = connProfile.cursor()

            queryProfile = "select * from profile where username = %s"
            valueProfile = (self.username,)

            cursorProfile.execute(queryProfile,valueProfile)
            resultProfile = cursorProfile.fetchone()

            if resultProfile[1] == None:
                self.frameProfileDisplay.lower()

            else:
                self.frameProfileCreate.lower()
              
                self.lblProfileDisplayGender.config(text=resultProfile[1])
                self.lblProfileDisplayHeight.config(text=resultProfile[2])
                self.lblProfileDisplayWeight.config(text=resultProfile[3])
                self.lblProfileDisplayAge.config(text=resultProfile[4])
                self.lblProfileDisplayBMI.config(text='Your Bmi is {} kg/m2'. format(resultProfile[5]))
                self.lblProfileDisplayCalorieneed.config(text='Your Daily Calorie\n need is {}/day'.format(resultProfile[6]))

                if float(resultProfile[5]) < 18.5:
                    self.lblProfileDisplayBMIResult.config(text="You are underweight!")
                elif float(resultProfile[5]) > 25:
                    self.lblProfileDisplayBMIResult.config(text="You are overweight!")
                else:
                    self.lblProfileDisplayBMIResult.config(text="You are healthy!")



        except Exception as e:
            messagebox.showerror(message=e)

    def createProfile(self):

        #Check if all entries are filled
        if (self.entProfileCreateHeight.index('end') != 0) and (self.entProfileCreateWeight.index('end') != 0) and (self.entProfileCreateAge.index('end') != 0):
            
            #Get Height, Weight, Age
            createProfileHeight = float(self.entProfileCreateHeight.get())
            createProfileWeight = float(self.entProfileCreateWeight.get())
            createProfileAge = int(self.entProfileCreateAge.get())
            createProfileGender = 'Male'

            #Calculate BMI
            createProfileBMI = createProfileWeight/pow((createProfileHeight/100),2)
            createProfileBMI = round(createProfileBMI,3)

            #Calculate Reqired Calories Based on Gender
            createProfilereqCal = 0.0

            if self.genderProfileCreateSelect.get() == 1:
                createProfilereqCal = (13.397*createProfileWeight) + (4.799*createProfileHeight) - (5.677*createProfileAge) + 88.362
                createProfilereqCal = createProfilereqCal * float(self.activityProfileCreateSelect.get())
                createProfileGender = 'Male'
            elif self.genderProfileCreateSelect.get() == 2:
                createProfilereqCal = (9.247*createProfileWeight) + (3.098*createProfileHeight) - (4.330*createProfileAge) + 447.593
                createProfilereqCal = createProfilereqCal * float(self.activityProfileCreateSelect.get())
                createProfileGender = 'Female'

            createProfilereqCal = round(createProfilereqCal, 3)

            #Create Database Connection and Store Values
            try:
                connCreateProfile = mysql.connector.connect(host = 'localhost', username = 'root', password = 'siddhesh@2204', database = 'pythonproject')
                cursorCreateProfile = connCreateProfile.cursor()

                queryProfile = "update profile set gender = %s, height = %s, weight = %s, age = %s, bmi = %s, calorieneed = %s where username = %s"
                valueProfile = (createProfileGender,  str(createProfileHeight), str(createProfileWeight), str(createProfileAge), str(createProfileBMI), str(createProfilereqCal), self.username)

                cursorCreateProfile.execute(queryProfile,valueProfile)
                connCreateProfile.commit()

                
                connCreateProfile.close()
                cursorCreateProfile.close()

                messagebox.showinfo(message="Success")

                self.backToHomepage()

            except Exception as e:
                messagebox.showerror(message=e)



        else:
            messagebox.showerror(message="Please Fill All Fields")

    def backToHomepage(self):
        self.withdraw()
        homepage = HomePage(self.username, self.root)
        homepage.focus_set()
        
    def openedit(self):
        self.frameProfileDisplay.lower()
        self.frameProfileCreate.lift()


#Search
class Search(Toplevel):
    def __init__(self, root, username):
        self.root = root
        self.username = username
        super().__init__(root)
        self.geometry('1080x720+240+40')
        self.resizable(0,0)
        self.title("Exercises")
        
        PanedWindow(self, bg='#73e0e6', width=1080, height=720).grid(column=0, row=0, columnspan=100, rowspan=100, sticky=NSEW)
        PanedWindow(self, bg='#23C0FF').grid(column=0, row=0, columnspan=25, rowspan=100, sticky=NSEW)
        Button(self, text="Prev", command=self.showprev, font='roboto 16 bold', bg="#1593EF", fg="#FFFFFF").grid(column=2, row=90, columnspan=10, rowspan=7, sticky=NSEW)
        Button(self, text="Next", command=self.shownext, font='roboto 16 bold', bg="#1593EF", fg="#FFFFFF").grid(column=13, row=90, columnspan=10, rowspan=7, sticky=NSEW)
        Button(self, text="Back", command=self.openHomepage, font='roboto 16 bold', bg="#1593EF", fg="#FFFFFF").grid(column=2, row=5, columnspan=10, rowspan=5, sticky=NSEW)

        chkboxattr = {"bg":"#73e0e6", "fg":"#000000", "anchor":"w"}
        self.optionselect = StringVar(value='arms')
        self.chkboxArms = Radiobutton(self, text="Arms", command=self.showexercises, font='roboto 16 bold', variable=self.optionselect, value='arms', **chkboxattr)
        self.chkboxArms.grid(column=5, row=20, columnspan=15, rowspan=5, sticky=NSEW)

        self.chkboxLegs = Radiobutton(self, text="Legs", command=self.showexercises, font='roboto 16 bold', variable=self.optionselect, value='legs', **chkboxattr)
        self.chkboxLegs.grid(column=5, row=30, columnspan=15, rowspan=5, sticky=NSEW)

        self.chkboxAbs = Radiobutton(self, text="Abs", command=self.showexercises, font='roboto 16 bold', variable=self.optionselect, value='abs', **chkboxattr)
        self.chkboxAbs.grid(column=5, row=40, columnspan=15, rowspan=5, sticky=NSEW)

        self.chkboxBack = Radiobutton(self, text="Back", command=self.showexercises, font='roboto 16 bold', variable=self.optionselect, value='back', **chkboxattr)
        self.chkboxBack.grid(column=5, row=50, columnspan=15, rowspan=5, sticky=NSEW)

        self.chkboxJoints = Radiobutton(self, text="Chest", command=self.showexercises, font='roboto 16 bold', variable=self.optionselect, value='chest', **chkboxattr)
        self.chkboxJoints.grid(column=5, row=60, columnspan=15, rowspan=5, sticky=NSEW)



        self.pageNum = 1

        self.showexercises()

    def showexercises(self):
        self.loadPhotos()
        self.mainframe = MainFrame(pageNum=self.pageNum, username=self.username, parent=self)
        self.mainframe.grid(column=27, row=3, columnspan=72, rowspan=95, sticky=NSEW)

    def loadPhotos(self):
        global images, exerinfo, exername
        images = []
        exerinfo = []
        exername = []

        selectedOption = self.optionselect.get()

        try:
            exerconn = mysql.connector.connect(host = "localhost", username ="root", password = "siddhesh@2204", database = "pythonproject")
            exercursor = exerconn.cursor()

            exerquery = "select * from exercises where category = %s"

            exercursor.execute(exerquery, (selectedOption,))
            
            result = exercursor.fetchall()

            for i in result:
                exername.append(i[0])
                imgs = ImageTk.PhotoImage(Image.open(i[1]))
                images.append(imgs)
                exerinfo.append(i[2])
            
            exercursor.close()
            exerconn.close()

        except Exception as e:
            messagebox.showwarning(message=exerquery.format(selectedOption), title="TEST")

        # for i in selectedOption:
        #     imgs = ImageTk.PhotoImage(Image.open(i[0]))
        #     images.append(imgs)
        #     exerinfo.append(i[1])
        
        self.maxpages = round(len(images)/3)

    def shownext(self):
        if (self.pageNum<self.maxpages):
            self.pageNum += 1
            self.mainframe.grid_forget()
            self.showexercises()

    def showprev(self):
        if (self.pageNum>1):
            self.pageNum -= 1
            self.mainframe.grid_forget()
            self.showexercises()

    def openHomepage(self):
        self.destroy()
        homepage = HomePage(self.username, self.root)
        homepage.focus_set()


class MainFrame(Frame):
    def __init__(self, pageNum, username, parent):
        self.username = username
        self.pageNum = pageNum
        self.parent = parent
        super().__init__(parent)
        self.config(bg='#73E0E6')
        self.initMainFrame()

    def initMainFrame(self):
        global exerinfo, exername, images
        row = 5
        for i in range (((self.pageNum-1)*3), (self.pageNum*3)):
            if (i<len(exerinfo)):
                f = exerciseFrame(images[i], exerinfo[i], self, exername[i], self.username, parent=self.parent) 
                f.place(x=10, y=row)
                row += 230
                i+=1


class exerciseFrame(Frame):
    def __init__(self, photo, info, mainFrame, name, username, parent):
        super().__init__(mainFrame)
        self.name = name
        self.username = username
        self.parent = parent
        self.config(bg='#13A0FF', bd=5, relief='sunken', width=1000, pady=10)
        PanedWindow(self, bg='#13A0FF', width=750, height=150).grid(column=0, row=0, columnspan=100, rowspan=100)

        self.testinfo = info
        self.testphoto = photo

        b = Button(self, borderwidth=0, image=photo, command=self.openview)
        b.grid(column=2, row=10, columnspan=30, rowspan=80, sticky=NSEW)
        l = Label(self, font="roboto 12 bold", text=info)
        l.grid(column=35, row=10, columnspan=63, rowspan=80, sticky=NSEW)

    def openview(self):
        
        selectedexercise = SelectedExercise(img=self.testphoto, root=self, info=self.testinfo, name=self.name, username=self.username, parent=self.parent)
        selectedexercise.focus_get()
        

class SelectedExercise(Toplevel):
    def __init__(self, root, img, info, name, username, parent):
        self.name = name
        self.username = username
        super().__init__(root)
        self.geometry('1080x720+240+40')
        self.resizable(0,0)
        self.title(name)

        panBg = PanedWindow(self, bg="#73E0E6", width=1080, height=720)
        panBg.grid(column=0, row=0, columnspan=100, rowspan=100, sticky=NSEW)
        Label(self, image=img, bg="#13A0FF", relief="sunken", bd=5).grid(column=35, row=10, columnspan=30, rowspan=30, sticky=NSEW)
        Label(self, text=info, bg="#23C0FF", fg='white', font='roboto 16 bold', relief="sunken", bd=5).grid(column=20, row=45, columnspan=60, rowspan=50, sticky=NSEW)
        
        if str(type(parent).__name__) == "Search":
            Button(self, text="Add Favourite", command=self.addfav, bg="#23C0FF", fg='white', font='roboto 12 bold').grid(column=45, row=3, columnspan=12, rowspan=5, sticky=NSEW)
        else:
            Button(self, text="Remove Favourite", command=self.removefav, bg="#23C0FF", fg='white', font='roboto 12 bold').grid(column=44, row=3, columnspan=14, rowspan=5, sticky=NSEW)



        Button(self, text="Back", bg="#23C0FF", fg='white', command=self.close, font='roboto 12 bold').grid(column=89, row=92, columnspan=10, rowspan=5, sticky=NSEW)

    def addfav(self):
        try:
            exerconn = mysql.connector.connect(host = "localhost", username ="root", password = "siddhesh@2204", database = "pythonproject")
            exercursor = exerconn.cursor()

            exerquery = "insert into favourites values(%s,%s)"

            exercursor.execute(exerquery, (self.username,self.name))
            
            exerconn.commit()

            exercursor.close()
            exerconn.close()
            messagebox.showinfo(message="Success", parent=self)

        except mysql.connector.errors.IntegrityError as e:
            messagebox.showinfo(message="Exercise already added to favourites.", parent=self)
        
        except Exception as e:
            messagebox.showinfo(message=e, parent=self)

    def removefav(self):
        try:
            exerconn = mysql.connector.connect(host = "localhost", username ="root", password = "siddhesh@2204", database = "pythonproject")
            exercursor = exerconn.cursor()

            exerquery = "delete from favourites where username = %s and exername = %s"

            exercursor.execute(exerquery, (self.username,self.name))
            
            exerconn.commit()

            exercursor.close()
            exerconn.close()
            messagebox.showinfo(message="Success", parent=self)
            self.withdraw()

        except mysql.connector.errors.IntegrityError as e:
            messagebox.showinfo(message="Database Integrity Error: " + e, parent=self)
        
        except Exception as e:
            messagebox.showinfo(message=e, parent=self)

    def close(self):
        self.withdraw()


#Favourites
class Favourites(Toplevel):
    def __init__(self, root, username):
        self.root = root
        self.username = username
        super().__init__(root)
        self.geometry('1080x720+240+40')
        self.resizable(0,0)
        self.title("Exercises")
        
        PanedWindow(self, bg='#73e0e6', width=1080, height=720).grid(column=0, row=0, columnspan=100, rowspan=100, sticky=NSEW)
        PanedWindow(self, bg='#23C0FF').grid(column=0, row=0, columnspan=25, rowspan=100, sticky=NSEW)
        Button(self, text="Prev", command=self.showprev, font='roboto 16 bold', bg="#1593EF", fg="#FFFFFF").grid(column=2, row=90, columnspan=10, rowspan=7, sticky=NSEW)
        Button(self, text="Next", command=self.shownext, font='roboto 16 bold', bg="#1593EF", fg="#FFFFFF").grid(column=13, row=90, columnspan=10, rowspan=7, sticky=NSEW)
        Button(self, text="Back", command=self.openHomepage, font='roboto 16 bold', bg="#1593EF", fg="#FFFFFF").grid(column=2, row=10, columnspan=10, rowspan=5, sticky=NSEW)

        self.pageNum = 1

        self.showexercises()

    def showexercises(self):
        self.loadPhotos()
        self.mainframe = MainFrame(pageNum=self.pageNum, parent=self, username=self.username)
        self.mainframe.grid(column=27, row=3, columnspan=72, rowspan=95, sticky=NSEW)

    def loadPhotos(self):
        global images, exerinfo, exername
        images = []
        exerinfo = []
        exername = []

        try:
            exerconn = mysql.connector.connect(host = "localhost", username ="root", password = "siddhesh@2204", database = "pythonproject")
            exercursor = exerconn.cursor()

            exerquery = "select * from exercises natural join favourites where favourites.username = %s and favourites.exername = exercises.name;"

            exercursor.execute(exerquery, (self.username,))
            
            result = exercursor.fetchall()

            for i in result:
                exername.append(i[0])
                imgs = ImageTk.PhotoImage(Image.open(i[1]))
                images.append(imgs)
                exerinfo.append(i[2])
            
            exercursor.close()
            exerconn.close()

        except Exception as e:
            messagebox.showwarning(message=exerquery, title="TEST")

        # for i in selectedOption:
        #     imgs = ImageTk.PhotoImage(Image.open(i[0]))
        #     images.append(imgs)
        #     exerinfo.append(i[1])
        
        self.maxpages = round(len(images)/3)

    def shownext(self):
        if (self.pageNum<self.maxpages):
            self.pageNum += 1
            self.mainframe.grid_forget()
            self.showexercises()

    def showprev(self):
        if (self.pageNum>1):
            self.pageNum -= 1
            self.mainframe.grid_forget()
            self.showexercises()

    def openHomepage(self):
        self.withdraw()
        homepage = HomePage(self.username, self.root)
        homepage.focus_set()


class Calender(Toplevel):
    def __init__(self, username, root):
        self.username = username
        self.root = root
        super().__init__(root)
        self.geometry('1080x720+240+40')
        self.resizable(0,0)
        self.title("Calender")
        
        PanedWindow(self, bg='#73e0e6', width=1080, height=720).grid(column=0, row=0, columnspan=100, rowspan=100)
        Button(self,text="Back", command=self.backToHome, bg="#15A3C7", fg="#FFFFFF", font='roboto 16 bold', relief='raised'). grid(column=88, row=93, columnspan=10, rowspan=5, sticky=NSEW)
        Button(self,text="Add Entry", command=self.addentry, bg="#15A3C7", fg="#FFFFFF", font='roboto 16 bold', relief='raised'). grid(column=54, row=87, columnspan=12, rowspan=5, sticky=NSEW)

        self.loadoptmenu()
        self.initFrame()

    def loadoptmenu(self):
        self.menu = StringVar(value="Select Exercise")
        self.calopt = OptionMenu(self, self.menu, '')
        self.calopt.grid(column=40, row=87, columnspan=12, rowspan=5, sticky=NSEW)

        try:

            calconn = mysql.connector.connect(host = "localhost", username ="root", password = "siddhesh@2204", database = "pythonproject")
            calcursor = calconn.cursor()

            calquery = " select name from exercises group by name;"

            calcursor.execute(calquery)
            
            result = calcursor.fetchall()

            self.menu.set('')
            for i in result:
                self.calopt['menu'].add_command(label=i[0], command=_setit(self.menu,i[0]))

            self.menu.set("Select Exercise")

            calcursor.close()
            calconn.close()
            
        except Exception as e:
            messagebox.showinfo(master=self, message=e)

    def initFrame(self):
        self.frameCalender = Frame(self, bd=5, relief="sunken")
        self.frameCalender.grid(column=15, row=15, columnspan=70, rowspan=70)
            
        PanedWindow(self.frameCalender, bg='#59ABDF', width=746, height=494).grid(column=0, row=0, columnspan=100, rowspan=100)
            
        self.table = ttk.Treeview(self.frameCalender, columns=("1", "2"), show="headings")
        self.table.heading("1", text="Exercise Name")
        self.table.heading("2", text="Date")
        self.table.bind('<<TreeviewSelect>>')
        self.table.bind('<Delete>', lambda e: self.deleteentry())
        self.table.grid(column=5, row=5, columnspan=90, rowspan=90, sticky=NSEW)
        self.loadtable()

    def loadtable(self):
        try:

            calconn = mysql.connector.connect(host = "localhost", username ="root", password = "siddhesh@2204", database = "pythonproject")
            calcursor = calconn.cursor()

            calquery = "select exername, date from calender where username = %s;"

            calcursor.execute(calquery, (self.username,))
            
            result = calcursor.fetchall()

            for i in result:
                self.table.insert(parent='', index=0, values=i)



            calcursor.close()
            calconn.close()
            
        except Exception as e:
            messagebox.showinfo(master=self, message=e)

    def deleteentry(self):
        # print(self.table.item(self.table.selection())['values'][1])
        try:

            calconn = mysql.connector.connect(host = "localhost", username ="root", password = "siddhesh@2204", database = "pythonproject")
            calcursor = calconn.cursor()

            calquery = "delete from calender where username = %s and date = %s;"

            calcursor.execute(calquery, (self.username,self.table.item(self.table.selection())['values'][1]))
            
            calconn.commit()
            calcursor.close()
            calconn.close()

            self.initFrame()
            
        except IndexError as e:
            messagebox.showinfo(master=self, message="Select a entry")
        except Exception as e:
            messagebox.showinfo(master=self, message=e)

    def addentry(self):

        if self.menu.get() == "Select Exercise":
            messagebox.showerror(message="Select Exercise")
            return

        try:

            calconn = mysql.connector.connect(host = "localhost", username ="root", password = "siddhesh@2204", database = "pythonproject")
            calcursor = calconn.cursor()

            calquery = "insert into calender values(%s, %s, now());"

            calcursor.execute(calquery, (self.username,self.menu.get()))
            
            calconn.commit()
            calcursor.close()
            calconn.close()

            self.initFrame()
            self.menu.set("Select Exercise")
            
        except Exception as e:
            messagebox.showinfo(master=self, message=e)
    
    def backToHome(self):
        self.withdraw()
        homepage = HomePage(self.username, self.root)
        homepage.focus_set()









if __name__ == '__main__':
    startpage = StartPage()


    startpage.mainloop()