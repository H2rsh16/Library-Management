from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from databaseconnect import *
import random
import string
import login as l


NewPassword = ""

def ForgotPasswordAdmin():

    root = Tk()

    root.title('Library Management System')
    root.resizable(False, False)

    def LoginA():
        root.destroy()
        l.LoginAsAdmin()

    canvas = Canvas(
        root,
        bg = "#fff",
        height = 500,
        width = 700,
        bd = 0,
        highlightthickness = 0,

    )

    canvas.pack()

    loginState = False


    def CheckDetails():
        n = name.get()
        username = Uname.get()
        password = Password.get()
        confirmpassword = ConfirmPassword.get()

        if ((n and username and password and confirmpassword) == ''):
            messagebox.showerror("Error", "Details are Empty!!")
        elif(password != confirmpassword):
            messagebox.showerror("Error", "Passwords are not matched !!")
        elif(password == confirmpassword):
            q = "select name, email from admin where name = '" + n +"';" 
            cursor.execute(q)
            a = ()
            for i in cursor:
                a = i

            if((n, username) != (a)):
                messagebox.showerror("Data error", "Data is not present in database !!")
            else:
                q = "update admin set password = '" + password + "' where name = '" + n + "';"
                cursor.execute(q)
                mydb.commit()
                if((n, username) == (a)):
                    messagebox.showinfo("Successfull", "Password Changed Successfully !!")
                    LoginA()
                else:
                    messagebox.showerror("Failed", "Fail to change password try again!!")


        else:
            return

    background = ImageTk.PhotoImage(Image.open("Images\Background.jpg"))
    canvas.create_image(0, 0, image = background, anchor = NW)


    canvas.create_text(300, 50, text = "Reset Admin Password ", font=('Poppins', 30, 'bold'), fill="#fff")
    canvas.create_text(130, 140, text = "Name -", font=('Poppins', 15), fill="#fff")
    canvas.create_text(130, 200, text = "Username -", font=('Poppins', 15), fill="#fff")
    canvas.create_text(130, 265, text = "Password -", font=('Poppins', 15), fill="#fff")
    canvas.create_text(130, 330, text = "Confirm Password -", font=('Poppins', 15), fill="#fff")

    name = Entry(root, width=40, font=('Poppins', 10))
    name.place(x=250,y=125)
    
    name.focus()

    Uname = Entry(root, width=40, font=('Poppins', 10))
    Uname.place(x=250,y=185)


    Password = Entry(root, width=40, font=('Poppins', 10))
    Password.place(x=250,y=250)
    
    ConfirmPassword = Entry(root, width=40, font=('Poppins', 10))
    ConfirmPassword.place(x=250,y=315)

    Password.config(show="*")
    SubmitBtn = Button(root, text = 'Reset', font=('Poppins', 15, 'bold'), bg = '#6E91EA', fg = "#fff", width=10, command = CheckDetails)
    SubmitBtn.place(x=270, y=416)
    
    LoginBtn = Button(root, text = 'Login', font=('Poppins', 10, 'bold'), bg = '#6E91EA', fg = "#fff", width=10, command = LoginA)
    LoginBtn.place(x=570, y=20)

    root.mainloop()
    
    


def ForgotPasswordStudent():

    root = Tk()

    root.title('Library Management System')
    root.resizable(False, False)

    def LoginS():
        root.destroy()
        l.LoginAsStudent()

    canvas = Canvas(
        root,
        bg = "#fff",
        height = 500,
        width = 700,
        bd = 0,
        highlightthickness = 0,

    )

    canvas.pack()

    loginState = False


    def CheckDetails():
        n = name.get()
        username = Uname.get()
        password = Password.get()
        confirmpassword = ConfirmPassword.get()
        if ((n and username and password and confirmpassword) == ''):
            messagebox.showerror("Error", "Details are Empty!!")
        elif(password != confirmpassword):
            messagebox.showerror("Error", "Passwords are not matched !!")
        elif(password == confirmpassword):
            q = "select name, email from students where name = '" + n +"';" 
            cursor.execute(q)
            a = ()
            for i in cursor:
                a = i

            if((n, username) != (a)):
                messagebox.showerror("Data error", "Data is not present in database !!")
            else:
                q = "update students set password = '" + password + "' where name = '" + n + "';"
                cursor.execute(q)
                mydb.commit()
                if((n, username) == (a)):
                    messagebox.showinfo("Successfull", "Password Changed Successfully !!")
                    LoginS()
                else:
                    messagebox.showerror("Failed", "Fail to change password try again!!")


        else:
            return

    background = ImageTk.PhotoImage(Image.open("Images\Background.jpg"))
    canvas.create_image(0, 0, image = background, anchor = NW)


    canvas.create_text(300, 50, text = "Reset Student Password ", font=('Poppins', 30, 'bold'), fill="#fff")
    canvas.create_text(130, 140, text = "Name -", font=('Poppins', 15), fill="#fff")
    canvas.create_text(130, 200, text = "Username -", font=('Poppins', 15), fill="#fff")
    canvas.create_text(130, 265, text = "Password -", font=('Poppins', 15), fill="#fff")
    canvas.create_text(130, 330, text = "Confirm Password -", font=('Poppins', 15), fill="#fff")

    name = Entry(root, width=40, font=('Poppins', 10))
    name.place(x=250,y=125)
    
    name.focus()

    Uname = Entry(root, width=40, font=('Poppins', 10))
    Uname.place(x=250,y=185)


    Password = Entry(root, width=40, font=('Poppins', 10))
    Password.place(x=250,y=250)
    
    ConfirmPassword = Entry(root, width=40, font=('Poppins', 10))
    ConfirmPassword.place(x=250,y=315)

    Password.config(show="*")
    SubmitBtn = Button(root, text = 'Reset', font=('Poppins', 15, 'bold'), bg = '#6E91EA', fg = "#fff", width=10, command = CheckDetails)
    SubmitBtn.place(x=270, y=416)
    
    LoginBtn = Button(root, text = 'Login', font=('Poppins', 10, 'bold'), bg = '#6E91EA', fg = "#fff", width=10, command = LoginS)
    LoginBtn.place(x=570, y=20)

    root.mainloop()
    
    



def VerificationA():
    root = Tk()

    root.title('Library Management System')
    root.resizable(False, False)

    canvas = Canvas(
        root,
        bg = "#fff",
        height = 500,
        width = 700,
        bd = 0,
        highlightthickness = 0,

    )

    canvas.pack()

    background = ImageTk.PhotoImage(Image.open("Images\Background.jpg"))
    canvas.create_image(0, 0, image = background, anchor = NW)

    TextCode = Label(root, text = "", font=('Poppins', 20, 'bold'), bg = "#fff", fg = "#101010", width = 15)
    TextCode.place(x=230, y=100)


    canvas.create_text(350, 50, text = "Reset Password ", font=('Poppins', 30, 'bold'), fill="#fff")

    canvas.create_text(350, 230, text = "Please Enter the Above Code to Verify", font=('Poppins', 10, 'bold'), fill="red")

    code = Entry(root, width=40, text="", font=('Poppins', 10))
    code.place(x=200,y=300)

    code.config(show="*")


    code.focus()

    def GenerateCode():
        letters = string.ascii_lowercase + string.ascii_uppercase + "!@#$%^&*()"
        NewPassword = ''.join(random.choice(letters) for i in range(8))
        TextCode.config(text = NewPassword)
   
    ReGenerateBtn = Button(root, text = 'Re-Generate', font=('Poppins', 10, 'bold'), bg = '#6E91EA', fg = "#fff", width=10, command = GenerateCode)
    ReGenerateBtn.place(x=295, y=350)

    GenerateCode()
    
    def CheckDetails():
        Code = code.get()
        if(Code == ''):
            messagebox.showerror("Error","Fill the Above Details")
        elif(Code == TextCode.cget('text')):
            messagebox.showinfo("Successfull","The Done Successfully")
            root.destroy()
            ForgotPasswordAdmin()
        else:
            code.config(text="")
            messagebox.showerror("Error","The Code Was not Matched")



    SubmitBtn = Button(root, text = 'Verify', font=('Poppins', 15, 'bold'), bg = '#6E91EA', fg = "#fff", width=10, command = CheckDetails)
    SubmitBtn.place(x=270, y=416)

    root.mainloop()
    
    

def VerificationS():
    root = Tk()

    root.title('Library Management System')
    root.resizable(False, False)

    canvas = Canvas(
        root,
        bg = "#fff",
        height = 500,
        width = 700,
        bd = 0,
        highlightthickness = 0,

    )

    canvas.pack()

    background = ImageTk.PhotoImage(Image.open("Images\Background.jpg"))
    canvas.create_image(0, 0, image = background, anchor = NW)

    TextCode = Label(root, text = "", font=('Poppins', 20, 'bold'), bg = "#fff", fg = "#101010", width = 15)
    TextCode.place(x=230, y=100)


    canvas.create_text(350, 50, text = "Reset Password ", font=('Poppins', 30, 'bold'), fill="#fff")

    canvas.create_text(350, 230, text = "Please Enter the Above Code to Verify", font=('Poppins', 10, 'bold'), fill="red")

    code = Entry(root, width=40, text="", font=('Poppins', 10))
    code.place(x=200,y=300)

    code.config(show="*")


    code.focus()

    def GenerateCode():
        letters = string.ascii_lowercase + string.ascii_uppercase + "!@#$%^&*()"
        NewPassword = ''.join(random.choice(letters) for i in range(8))
        TextCode.config(text = NewPassword)
   
    ReGenerateBtn = Button(root, text = 'Re-Generate', font=('Poppins', 10, 'bold'), bg = '#6E91EA', fg = "#fff", width=10, command = GenerateCode)
    ReGenerateBtn.place(x=295, y=350)

    GenerateCode()
    
    def CheckDetails():
        Code = code.get()
        if(Code == ''):
            messagebox.showerror("Error","Fill the Above Details")
        elif(Code == TextCode.cget('text')):
            messagebox.showinfo("Successfull","The Done Successfully")
            root.destroy()
            ForgotPasswordStudent()
        else:
            code.config(text="")
            messagebox.showerror("Error","The Code Was not Matched")



    SubmitBtn = Button(root, text = 'Verify', font=('Poppins', 15, 'bold'), bg = '#6E91EA', fg = "#fff", width=10, command = CheckDetails)
    SubmitBtn.place(x=270, y=416)

    root.mainloop()
    
    

