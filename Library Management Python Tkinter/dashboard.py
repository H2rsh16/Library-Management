from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from time import *
import datetime as dt
import login as l
import Functions as f


def DashboardStudent():

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

    def LogOutStudents():
        root.destroy()
        l.LoginAsStudent()

    def time():
        string = strftime('%H:%M:%S %p')
        TimeText.config(text=string)
        TimeText.after(1000, time)

    def B():
        root.destroy()
        f.ShowBooksS()

    def C():
        root.destroy()
        f.CheckDue()
    
    def Ishuee():
        root.destroy()
        f.IshueeBooks()
    
    def ReturnIshueed():
        root.destroy()
        f.ReturnIshueeBooks()

    d = dt.datetime.now()
    Date = d.strftime('%d/%m/%Y')

    background = ImageTk.PhotoImage(Image.open("Images\Background.jpg"))
    rect = ImageTk.PhotoImage(Image.open("Images\Rectangle.png"))
    canvas.create_image(0, 0, image = background, anchor = NW)
    canvas.create_image(0, 23, image = rect, anchor = NW)

    global StudentName

    StudentName = l.StudentName

    canvas.create_text(210, 65, text = "Student Dashboard", font=('Poppins', 30, 'bold'), fill="#fff")
    canvas.create_text(550, 110, text = "Name -" , font=('Poppins', 10), fill="#fff")
    canvas.create_text(30, 110, text = "Date -" , font=('Poppins', 10), fill="#fff")
    canvas.create_text(620, 110, text = str(StudentName).replace("'","").replace("(","").replace(")","").replace(",","") , font=('Poppins', 10), fill="#fff")
    canvas.create_text(90, 110, text = Date , font=('Poppins', 10), fill="#fff")

    Ishuee_bookBtn = Button(root, text = "Ishuee Book", font = ('Poppins', 12), bd = 0, width = 15, command = Ishuee)
    Ishuee_bookBtn.place(x=158, y=176)
    
    Return_bookBtn = Button(root, text = "Return Book", font = ('Poppins', 12), bd = 0, width = 15, command = ReturnIshueed)
    Return_bookBtn.place(x=361, y=176)
    
    CheckDue_bookBtn = Button(root, text = "Check\nIshueed Books", font = ('Poppins', 12), height=1, pady=10, bd = 0, width = 15, padx=10, command = C)
    CheckDue_bookBtn.place(x=361, y=260)
    
    Show_bookBtn = Button(root, text = "Show Book", font = ('Poppins', 12), bd = 0, width = 15, command = B)
    Show_bookBtn.place(x=158, y=269)
    
    LogOutBtn = Button(root, text = "Log-Out", font = ('Poppins', 12), bd = 0, width = 10, command = LogOutStudents)
    LogOutBtn.place(x=287, y=342)

    TimeText = Label(root, text = "00:00:00", background="#14100E", fg = "#fff", font=('Poppins', 20, 'bold'), width= 11)
    TimeText.place(x=515, y=450)
    
    time()

    root.mainloop()
    
    

def DashboardAdmin():

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
    
    def LogOutAdmin():
        root.destroy()
        l.LoginAsAdmin()
    
    d = dt.datetime.now()
    Date = d.strftime('%d/%m/%Y')
    CurrentTime = '00:00:00'



    background = ImageTk.PhotoImage(Image.open("Images\Background.jpg"))
    rect = ImageTk.PhotoImage(Image.open("Images\Rectangle.png"))
    canvas.create_image(0, 0, image = background, anchor = NW)
    canvas.create_image(0, 23, image = rect, anchor = NW)

    global AdminName

    AdminName = l.AdminName

    def A():
        root.destroy()
        f.AddingBooks()
    
    def R():
        root.destroy()
        f.RemovingBooks()
    
    def S():
        root.destroy()
        f.ShowStudents()
    
    def B():
        root.destroy()
        f.ShowBooksA()

    canvas.create_text(210, 65, text = "Admin Dashboard", font=('Poppins', 30, 'bold'), fill="#fff")
    canvas.create_text(550, 110, text = "Name -" , font=('Poppins', 10), fill="#fff")
    canvas.create_text(30, 110, text = "Date -" , font=('Poppins', 10), fill="#fff")
    canvas.create_text(620, 110, text = str(AdminName).replace("'","").replace("(","").replace(")","").replace(",","") , font=('Poppins', 10), fill="#fff")
    canvas.create_text(90, 110, text = Date , font=('Poppins', 10), fill="#fff")

    Add_bookBtn = Button(root, text = "Add Book", font = ('Poppins', 12), bd = 0, width = 15, command = A)
    Add_bookBtn.place(x=158, y=176)
    
    Remove_bookBtn = Button(root, text = "Remove Book", font = ('Poppins', 12), bd = 0, width = 15, command = R)
    Remove_bookBtn.place(x=361, y=176)
    
    Check_StudentBtn = Button(root, text = "Check Students", font = ('Poppins', 12), bd = 0, width = 15, command = S)
    Check_StudentBtn.place(x=160, y=257)
    
    ShowBooksBtn = Button(root, text = "Check Books", font = ('Poppins', 12), bd = 0, width = 15, command = B)
    ShowBooksBtn.place(x=360, y=257)
    
    LogOutBtn = Button(root, text = "Log-Out", font = ('Poppins', 12), bd = 0, width = 10, command = LogOutAdmin)
    LogOutBtn.place(x=287, y=342)

    TimeText = Label(root, text = "00:00:00", background="#14100E", fg = "#fff", font=('Poppins', 20, 'bold'), width= 11)
    TimeText.place(x=515, y=450)


    def time():
        string = strftime('%H:%M:%S %p')
        TimeText.config(text=string)
        TimeText.after(1000, time)

    
    time()

    root.mainloop()


