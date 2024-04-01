from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
x=Tk()
x.title("LOGIN")
x.geometry("925x500+300+200")
x.config(bg="#fff")
x.resizable(False,False)
def sign():
    username=user.get()
    password=code.get()

    if username=='admin' and password=='8320':
        root = tk.Tk()
        root.title("Management")

        connection = sqlite3.connect('management.db')

        TABLE_NAME = "management_table"
        STUDENT_ID = "student_id"
        STUDENT_NAME = "student_name"
        STUDENT_COLLEGE = "student_college"
        STUDENT_ADDRESS = "student_address"
        STUDENT_PHONE = "student_phone"

        connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + STUDENT_ID +
                   " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                   STUDENT_NAME + " TEXT, " + STUDENT_COLLEGE + " TEXT, " +
                   STUDENT_ADDRESS + " TEXT, " + STUDENT_PHONE + " INTEGER);")

        appLabel = tk.Label(root, text="Student Management System", fg="#06a099", width=35)
        appLabel.config(font=("Sylfaen", 30))
        appLabel.grid(row=0, columnspan=2, padx=(10,10), pady=(30, 0))

        class Student:
            studentName = ""
            collegeName = ""
            phoneNumber = 0
            address = ""

            def _init_(self, studentName, collegeName, phoneNumber, address):
                self.studentName = studentName
                self.collegeName = collegeName
                self.phoneNumber = phoneNumber
                self.address = address

        nameLabel = tk.Label(root, text="Enter your name", width=40, anchor='w',
                     font=("Sylfaen", 12)).grid(row=1, column=0, padx=(10,0),
                                                pady=(30, 0))
        collegeLabel = tk.Label(root, text="Enter your college", width=40, anchor='w',
                        font=("Sylfaen", 12)).grid(row=2, column=0, padx=(10,0))
        phoneLabel = tk.Label(root, text="Enter your phone number", width=40, anchor='w',
                      font=("Sylfaen", 12)).grid(row=3, column=0, padx=(10,0))
        addressLabel = tk.Label(root, text="Enter your address", width=40, anchor='w',
                        font=("Sylfaen", 12)).grid(row=4, column=0, padx=(10,0))

        nameEntry = tk.Entry(root, width = 30)
        collegeEntry = tk.Entry(root, width = 30)
        phoneEntry = tk.Entry(root, width = 30)
        addressEntry = tk.Entry(root, width = 30)

        nameEntry.grid(row=1, column=1, padx=(0,10), pady=(30, 20))
        collegeEntry.grid(row=2, column=1, padx=(0,10), pady = 20)
        phoneEntry.grid(row=3, column=1, padx=(0,10), pady = 20)
        addressEntry.grid(row=4, column=1, padx=(0,10), pady = 20)

        def takeNameInput():
            global nameEntry, collegeEntry, phoneEntry, addressEntry
            global list
            global TABLE_NAME, STUDENT_NAME, STUDENT_COLLEGE, STUDENT_ADDRESS, STUDENT_PHONE
            username = nameEntry.get()
            nameEntry.delete(0, tk.END)
            collegeName = collegeEntry.get()
            collegeEntry.delete(0, tk.END)
            phone = int(phoneEntry.get())
            phoneEntry.delete(0, tk.END)
            address = addressEntry.get()
            addressEntry.delete(0, tk.END)

            connection.execute("INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + ", " +
                       STUDENT_COLLEGE + ", " + STUDENT_ADDRESS + ", " +
                       STUDENT_PHONE + " ) VALUES ( '"
                       + username + "', '" + collegeName + "', '" +
                       address + "', " + str(phone) + " ); ")
            connection.commit()
            messagebox.showinfo("Success", "Data Saved Successfully.")


        def destroyRootWindow():
            root.destroy()
            secondWindow = tk.Tk()

            secondWindow.title("Display results")

            appLabel = tk.Label(secondWindow, text="Student Management System",
                        fg="#06a099", width=40)
            appLabel.config(font=("Sylfaen", 30))
            appLabel.pack()

            tree = ttk.Treeview(secondWindow)
            tree["columns"] = ("one", "two", "three", "four")

            tree.heading("one", text="Student Name")
            tree.heading("two", text="College Name")
            tree.heading("three", text="Address")
            tree.heading("four", text="Phone Number")

            cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")
            i = 0

            for row in cursor:
                tree.insert('', i, text="Student " + str(row[0]),
                            values=(row[1], row[2],
                                    row[3], row[4]))
                i = i + 1

            tree.pack()
            secondWindow.mainloop()

        button = tk.Button(root, text="Take input", command=lambda :takeNameInput())
        button.grid(row=5, column=0, pady=30)

        displayButton = tk.Button(root, text="Display result", command=lambda :destroyRootWindow())
        displayButton.grid(row=5, column=1)

        root.mainloop()
    elif username!='admin' and password!='8320':
        messagebox.showerror("invalid","invalid username & password")
    elif username!='admin':
        messagebox.showerror("wrong","you are not a user")
    elif password!='8320':
        messagebox.showerror("wrong"," entered wrong password")
        
    
        
img=PhotoImage(file=('C:\\Users\\Aravind\\Desktop\\file\\login.png'))
Label(x,image=img,bg='white').place(x=50,y=50)
frame=Frame(x,width=350,height=350,bg="white")
frame.place(x=480,y=70)
heading=Label(frame,text="SIGN IN",fg="#57a1f8",bg="white",font=("Microsoft YaHei UI Light",23,"bold"))
heading.place(x=100,y=5)
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'username')
user=Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
user.place(x=30,y=80)
user.insert(0,'username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)
#
def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'password')
code=Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
code.place(x=30,y=150)
code.insert(0,'password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)
#
Button(frame,text="sign in",bg="#57a1f8",fg="white",border=0,width=39,pady=7,command=sign).place(x=35,y=204)
label=Label(frame,text="Dont't have an account?",fg="black",bg="white",font=("Microsoft YaHei UI Light",9))
label.place(x=75,y=270)
sign_up=Button(frame,width=6,text="sign up",border=0,bg="white",cursor="hand2",fg="#57a1f8")
sign_up.place(x=215,y=270)
x.mainloop()
