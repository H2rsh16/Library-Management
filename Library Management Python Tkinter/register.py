from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from databaseconnect import *
import login as l

def RegisterAsAdmin():

    root = Tk()
    

    root.title('Library Management System')
    root.resizable(False, False)

    def A():
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
        n = Name.get()
        u = Uname.get()
        p = Password.get()
        rowData = ()
        q = "select name, email, password from admin where name = '"+ n +"' and email = '" + u + "' and password = '" + p + "';"
        cursor.execute(q)
        for i in cursor:
            rowData = i
        mydb.commit()
        if(n == "" and u == "" and p == ""):
            messagebox.showerror("Error", "Fill the details first!")
        elif(n, u, p):
            if((n, u, p) == rowData):
                messagebox.showwarning("Data Error", "Data is already present in Database")
            else:
                insertQuery = "insert into admin(name, email, password) values('" + n + "', '" + u + "', '" + p + "');"
                cursor.execute(insertQuery)
                mydb.commit()
                messagebox.showinfo("Successfull", "Data is inserted")
            
    background = ImageTk.PhotoImage(Image.open("Images\Background.jpg"))
    canvas.create_image(0, 0, image = background, anchor = NW)


    canvas.create_text(350, 50, text = "Register Admin", font=('Poppins', 40, 'bold'), fill="#fff")
    canvas.create_text(130, 210, text = "Name -", font=('Poppins', 15), fill="#fff")
    canvas.create_text(130, 280, text = "Username -", font=('Poppins', 15), fill="#fff")
    canvas.create_text(130, 350, text = "Password -", font=('Poppins', 15), fill="#fff")

    Name = Entry(root, width=40, font=('Poppins', 10))
    Name.place(x=250,y=195)
    Name.focus()


    Uname = Entry(root, width=40, font=('Poppins', 10))
    Uname.place(x=250,y=265)


    Password = Entry(root, width=40, font=('Poppins', 10))
    Password.place(x=250,y=335)
    Password.config(show="*")

    SubmitBtn = Button(root, text = 'Submit', font=('Poppins', 15, 'bold'), bg = '#6E91EA', fg = "#fff", width=10, command = CheckDetails)
    SubmitBtn.place(x=270, y=416)
    
    LoginBtn = Button(root, text = 'Login', font=('Poppins', 10), width=13, command = A)
    LoginBtn.place(x=550, y=450)

    root.mainloop()




def RegisterAsStudent():

    root = Tk()
    

    root.title('Library Management System')
    root.resizable(False, False)

    def S():
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
        n = Name.get()
        u = Uname.get()
        p = Password.get()
        rowData = ()
        q = "select name, email, password from students where name = '"+ n +"' and email = '" + u + "' and password = '" + p + "';"
        cursor.execute(q)
        for i in cursor:
            rowData = i
        mydb.commit()
        if(n == "" and u == "" and p == ""):
            messagebox.showerror("Error", "Fill the details first!")
        elif(n, u, p):
            if((n, u, p) == rowData):
                messagebox.showwarning("Data Error", "Data is already present in Database")
            else:
                insertQuery = "insert into students(name, email, password) values('" + n + "', '" + u + "', '" + p + "');"
                cursor.execute(insertQuery)
                mydb.commit()
                messagebox.showinfo("Successfull", "Data is inserted")
            
    background = ImageTk.PhotoImage(Image.open("Images\Background.jpg"))
    canvas.create_image(0, 0, image = background, anchor = NW)


    canvas.create_text(350, 50, text = "Register Admin", font=('Poppins', 40, 'bold'), fill="#fff")
    canvas.create_text(130, 210, text = "Name -", font=('Poppins', 15), fill="#fff")
    canvas.create_text(130, 280, text = "Username -", font=('Poppins', 15), fill="#fff")
    canvas.create_text(130, 350, text = "Password -", font=('Poppins', 15), fill="#fff")

    Name = Entry(root, width=40, font=('Poppins', 10))
    Name.place(x=250,y=195)
    Name.focus()


    Uname = Entry(root, width=40, font=('Poppins', 10))
    Uname.place(x=250,y=265)


    Password = Entry(root, width=40, font=('Poppins', 10))
    Password.place(x=250,y=335)
    Password.config(show="*")

    SubmitBtn = Button(root, text = 'Submit', font=('Poppins', 15, 'bold'), bg = '#6E91EA', fg = "#fff", width=10, command = CheckDetails)
    SubmitBtn.place(x=270, y=416)
    
    LoginBtn = Button(root, text = 'Login', font=('Poppins', 10), width=13, command = S)
    LoginBtn.place(x=550, y=450)

    root.mainloop()

