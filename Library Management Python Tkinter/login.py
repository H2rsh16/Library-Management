from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from databaseconnect import *
from dashboard import *
from register import RegisterAsAdmin, RegisterAsStudent
from ForgotPassword import VerificationA,VerificationS

def LoginAsAdmin():
    global root
    root = Tk()
    

    root.title('Library Management System')
    root.resizable(False, False)
    

    def VerifyAsAdmin():
        root.destroy()
        VerificationA()


    canvas = Canvas(
        root,
        bg = "#fff",
        height = 500,
        width = 700,
        bd = 0,
        highlightthickness = 0,

    )

    canvas.pack()
    loginStateAdmin = False

    def CheckDetails():
        global AdminName
        AdminName = ""
        username = Uname.get()
        psk = Password.get()
        if(username == '' and psk == ""):
            messagebox.showerror("Error","Fill the Above Details")
        elif(username == ''):
            messagebox.showerror("Error","Username Is Empty!!")
        elif(psk == ''):
            messagebox.showerror("Error","Password Is Empty!!")
        else:
            loginStateAdmin = True
            if(loginStateAdmin):
                query = "select email, password from admin where email = '" + username + "';"
                cursor.execute(query)
                var = ""
                for a in cursor:
                    var = a

                if((username,psk) == (var)):
                    query = "select name from admin where email = '" + username + "';"
                    cursor.execute(query)
                    for b in cursor:
                        AdminName = b

                    messagebox.showinfo("Success", "Login Successfull")
                    root.destroy()
                    DashboardAdmin()
                else:
                    Uname.config(text="")
                    Password.config(text="")
                    messagebox.showerror("Error", "Credentials are Incorrect")
            else:
                return
            
    def A():
        root.destroy()
        RegisterAsAdmin()

    background = ImageTk.PhotoImage(Image.open("Images\Background.jpg"))
    canvas.create_image(0, 0, image = background, anchor = NW)



    canvas.create_text(350, 50, text = "Login Admin", font=('Poppins', 40, 'bold'), fill="#fff")
    canvas.create_text(130, 200, text = "Username -", font=('Poppins', 15), fill="#fff")
    canvas.create_text(130, 300, text = "Password -", font=('Poppins', 15), fill="#fff")

    Uname = Entry(root, width=40, font=('Poppins', 10))
    Uname.place(x=250,y=185)

    Uname.focus()

    Password = Entry(root, width=40, font=('Poppins', 10))
    Password.place(x=250,y=285)
    Password.config(show="*")

    SubmitBtn = Button(root, text = 'Submit', font=('Poppins', 15, 'bold'), bg = '#6E91EA', fg = "#fff", width=10, command = CheckDetails)
    SubmitBtn.place(x=270, y=416)
    
    ForgotPassBtn = Button(root, text = 'Reset Password', font=('Poppins', 10), width=13, command = VerifyAsAdmin)
    ForgotPassBtn.place(x=550, y=450)
    
    RefisterBtn = Button(root, text = 'Register', font=('Poppins', 10), width=13, command = A)
    RefisterBtn.place(x=30, y=450)

    root.mainloop()
    
    




def LoginAsStudent():
    global root
    root = Tk()

    root.title('Library Management System')
    root.resizable(False, False)

    def VerifyAsStudent():
        root.destroy()
        VerificationS()

    
    canvas = Canvas(
        root,
        bg = "#fff",
        height = 500,
        width = 700,
        bd = 0,
        highlightthickness = 0,

    )

    canvas.pack()

    loginStateStudent = False


    def CheckDetails():
        global StudentName
        StudentName = ""
        username = Uname.get()
        psk = Password.get()
        if(username == '' and psk == ""):
            messagebox.showerror("Error","Fill the Above Details")
        elif(username == ''):
            messagebox.showerror("Error","Username Is Empty!!")
        elif(psk == ''):
            messagebox.showerror("Error","Password Is Empty!!")
        else:
            loginStateStudent = True
            if(loginStateStudent):
                query = "select email, password from students where email = '" + username + "';"
                cursor.execute(query)
                var = ""
                for x in cursor:
                    var = x
                if((username,psk) == (var)):
                    query = "select name from students where email = '" + username + "';"
                    cursor.execute(query)
                    for b in cursor:
                        StudentName = b
                    mydb.commit()
                    messagebox.showinfo("Success", "Login Successfull")
                    root.destroy()
                    DashboardStudent()
                else:
                    Uname.config(text="")
                    Password.config(text="")
                    messagebox.showerror("Error", "Credentials are Incorrect")

            return
        
    def R():
        root.destroy()
        RegisterAsStudent()

    background = ImageTk.PhotoImage(Image.open("Images\Background.jpg"))
    canvas.create_image(0, 0, image = background, anchor = NW)


    canvas.create_text(350, 50, text = "Login Student", font=('Poppins', 40, 'bold'), fill="#fff")
    canvas.create_text(130, 200, text = "Username -", font=('Poppins', 15), fill="#fff")
    canvas.create_text(130, 300, text = "Password -", font=('Poppins', 15), fill="#fff")

    Uname = Entry(root, width=40, font=('Poppins', 10))
    Uname.place(x=250,y=185)

    Uname.focus()

    Password = Entry(root, width=40, font=('Poppins', 10))
    Password.place(x=250,y=285)

    Password.config(show="*")
    SubmitBtn = Button(root, text = 'Submit', font=('Poppins', 15, 'bold'), bg = '#6E91EA', fg = "#fff", width=10, command = CheckDetails)
    SubmitBtn.place(x=270, y=416)

    ForgotPassBtn = Button(root, text = 'Reset Password', font=('Poppins', 10), width=13, command = VerifyAsStudent)
    ForgotPassBtn.place(x=550, y=450)

    RefisterBtn = Button(root, text = 'Register', font=('Poppins', 10), width=13, command = R)
    RefisterBtn.place(x=30, y=450)

    root.mainloop()
    
    
