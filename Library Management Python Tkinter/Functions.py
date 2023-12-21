from tkinter import *
from tkinter import ttk
import datetime as dt
from tkinter import messagebox
from PIL import ImageTk, Image
from databaseconnect import *
import dashboard as d
from login import *
from tkcalendar import *
import login as l



def AddingBooks():
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

    def Back():
        root.destroy()
        d.DashboardAdmin()

    def CheckDetails():
        n = name.get()
        a = author.get()
        c = category.get()
        d = description.get()
        q = quantity.get().replace("'","")
        if(((n and a and c and d and q) == "")):
            messagebox.showerror("Error","Please Fill All The Details")
        elif(n == ""):
            messagebox.showerror("Error","Please Fill All The Details")
        elif(a == ""):
            messagebox.showerror("Error","Please Fill All The Details")
        elif(c == ""):
            messagebox.showerror("Error","Please Fill All The Details")
        elif(d == ""):
            messagebox.showerror("Error","Please Fill All The Details")
        elif(q == ""):
            messagebox.showerror("Error","Please Fill All The Details")
        else:
            query = "select * from book where name = '" + n + "';"
            cursor.execute(query)
            i = ()
            for i in cursor:
                a = i
            if((n, a, c, d, q) == a):
                messagebox.showinfo("Error", "The Book is Already Added in Database!!")
            else:
                q2 = "insert into book(name, author, category, description, quantity) values('"+ n + "', '" + a + "', '" + c + "', '" + d + "', '" + q + "');"
                cursor.execute(q2)
                cursor.execute("set @num := 0;")
                cursor.execute("update book set id = @num := (@num + 1);")
                messagebox.showinfo("Successfull", "Book Added Successfully")
                mydb.commit()
    background = ImageTk.PhotoImage(Image.open("Images\Background.jpg"))
    rect = ImageTk.PhotoImage(Image.open("Images\Rectangle.png"))
    canvas.create_image(0, 0, image = background, anchor = NW)
    canvas.create_image(0, 23, image = rect, anchor = NW)


    canvas.create_text(120, 65, text = "Add Books", font=('Poppins', 30, 'bold'), fill="#fff")


    canvas.create_text(130, 140, text = "Name -", font=('Poppins', 15), fill="#fff")
    canvas.create_text(130, 200, text = "Author -", font=('Poppins', 15), fill="#fff")
    canvas.create_text(130, 265, text = "Category -", font=('Poppins', 15), fill="#fff")
    canvas.create_text(130, 330, text = "Description -", font=('Poppins', 15), fill="#fff")
    canvas.create_text(130, 395, text = "Quantity -", font=('Poppins', 15), fill="#fff")

    name = Entry(root, width=40, font=('Poppins', 10))
    name.place(x=250,y=125)

    name.focus()

    author = Entry(root, width=40, font=('Poppins', 10))
    author.place(x=250,y=185)


    category = Entry(root, width=40, font=('Poppins', 10))
    category.place(x=250,y=250)

    description = Entry(root, width=40, font=('Poppins', 10))
    description.place(x=250,y=315)

    quantity = Entry(root, width=40, font=('Poppins', 10))
    quantity.place(x=250,y=380)

    SubmitBtn = Button(root, text = "Submit", font=('Poppins', 10, 'bold'), bd = 0, width=10, command = CheckDetails)
    SubmitBtn.place(x = 340, y = 450)

    BackBtn = Button(root, text = "Go Back", font=('Poppins', 10, 'bold'), bd = 0, width=10, command = Back)
    BackBtn.place(x = 550, y = 450)

    root.mainloop()
    
def RemovingBooks():
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

    def Back():
        root.destroy()
        d.DashboardAdmin()

    def CheckDetails():
        n = name.get()
        a = author.get()

        if(((n and a) == "")):
            messagebox.showerror("Error","Please Fill All The Details")
        elif(n == ""):
            messagebox.showerror("Error","Please Fill All The Details")
        elif(a == ""):
            messagebox.showerror("Error","Please Fill All The Details")
        else:
            d = ()
            q = "select name, author from book where name = '" + n  + "' and author = '" + a + "';"
            cursor.execute(q)
            for i in cursor:
                d = i

            if((n, a) != d):
                messagebox.showwarning("Error", "Data is incorrect try again :( ")
            else:
                q2 = "delete from book WHERE name = '" + n + "' and author = '" + a + "';"
                cursor.execute(q2)
                cursor.execute("set @num := 0;")
                cursor.execute("update book set id = @num := (@num + 1);")
                messagebox.showinfo("Successfull", "Book Removed Successfully")
            mydb.commit()


    background = ImageTk.PhotoImage(Image.open("Images\Background.jpg"))
    rect = ImageTk.PhotoImage(Image.open("Images\Rectangle.png"))
    canvas.create_image(0, 0, image = background, anchor = NW)
    canvas.create_image(0, 23, image = rect, anchor = NW)


    canvas.create_text(160, 65, text = "Remove Books", font=('Poppins', 30, 'bold'), fill="#fff")


    canvas.create_text(130, 160, text = "Name -", font=('Poppins', 15), fill="#fff")
    canvas.create_text(130, 220, text = "Author -", font=('Poppins', 15), fill="#fff")

    name = Entry(root, width=40, font=('Poppins', 10))
    name.place(x=250,y=145)

    name.focus()

    author = Entry(root, width=40, font=('Poppins', 10))
    author.place(x=250,y=205)

    SubmitBtn = Button(root, text = "Submit", font=('Poppins', 10, 'bold'), bd = 0, width=10, command = CheckDetails)
    SubmitBtn.place(x = 340, y = 450)

    BackBtn = Button(root, text = "Go Back", font=('Poppins', 10, 'bold'), bd = 0, width=10, command = Back)
    BackBtn.place(x = 550, y = 450)

    root.mainloop()
    
def ShowStudents():
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

    def Back():
        root.destroy()
        d.DashboardAdmin()

    

    style = ttk.Style()
    style.configure("Treeview", rowheight = 30, rowwidth = 100)

    background = ImageTk.PhotoImage(Image.open("Images\Background.jpg"))
    rect = ImageTk.PhotoImage(Image.open("Images\Rectangle.png"))
    canvas.create_image(0, 0, image = background, anchor = NW)
    canvas.create_image(0, 23, image = rect, anchor = NW)


    canvas.create_text(120, 65, text = "Students -", font=('Poppins', 30, 'bold'), fill="#fff")

    tree = ttk.Treeview(root)
    
    tree.place(x=50,y=110)
    
    verscrlbar = ttk.Scrollbar(root,orient ="vertical",command = tree.yview)
    
    verscrlbar.place(x=660,y=250)
    
    tree.configure(xscrollcommand = verscrlbar.set)
    
    tree["columns"] = ("1", "2", "3", "4")
    
    tree['show'] = 'headings'
    
    tree.column("1", width = 150, anchor = CENTER)
    tree.column("2", width = 150, anchor = CENTER)
    tree.column("3", width = 150, anchor = CENTER)
    tree.column("4", width = 150, anchor = CENTER)
    
    tree.heading("1", text ="Student Id")
    tree.heading("2", text ="Student Name")
    tree.heading("3", text ="Student Email")
    tree.heading("4", text ="Student Password")


    BackBtn = Button(root, text = "Go Back", font=('Poppins', 10, 'bold'), bd = 0, width=10, command = Back)
    BackBtn.place(x = 550, y = 450)

    query = "select * from students;"
    cursor.execute(query)
    a = 0
    for i in cursor:
        tree.insert('', a, text = "", values = (i[0], i[1], i[2], i[3]))
        a = a + 1
    mydb.commit()
    root.mainloop()
    
def ShowBooksS():
    root = Tk()

    root.title('Library Management System')
    root.resizable(False, False)


    canvas = Canvas(
    root,
    bg = "#fff",
    height = 500,
    width = 820,
    bd = 0,
    highlightthickness = 0,
    )

    canvas.pack()

    def Back():
        root.destroy()
        d.DashboardStudent()

    

    style = ttk.Style()
    style.configure("Treeview", rowheight = 30, rowwidth = 100)

    background = ImageTk.PhotoImage(Image.open(r"Images\New BG.jpg"))
    rect = ImageTk.PhotoImage(Image.open(r"Images\New Rect.png"))
    canvas.create_image(0, 0, image = background, anchor = NW)
    canvas.create_image(0, 23, image = rect, anchor = NW)


    canvas.create_text(145, 65, text = "Show Books -", font=('Poppins', 30, 'bold'), fill="#fff")

    tree = ttk.Treeview(root)
    
    tree.place(x=40,y=110)
    
    verscrlbar = ttk.Scrollbar(root,orient ="vertical",command = tree.yview)
    
    verscrlbar.place(x=790,y=250)
    
    tree.configure(xscrollcommand = verscrlbar.set)
    
    tree["columns"] = ("1", "2", "3", "4", "5", "6")
    
    tree['show'] = 'headings'
    
    tree.column("1", width = 50, anchor = CENTER)
    tree.column("2", width = 150, anchor = CENTER)
    tree.column("3", width = 150, anchor = CENTER)
    tree.column("4", width = 150, anchor = CENTER)
    tree.column("5", width = 150, anchor = CENTER)
    tree.column("6", width = 90, anchor = CENTER)
    
    tree.heading("1", text ="Book Id")
    tree.heading("2", text ="Book Name")
    tree.heading("3", text ="Book Description")
    tree.heading("4", text ="Book Category")
    tree.heading("5", text ="Book Author")
    tree.heading("6", text ="Book Quantity")


    BackBtn = Button(root, text = "Go Back", font=('Poppins', 10, 'bold'), bd = 0, width=10, command = Back)
    BackBtn.place(x = 650, y = 450)

    query = "select * from book;"
    cursor.execute(query)
    a = 0
    for i in cursor:
        tree.insert('', a, text = "", values = (i[0], i[1], i[2], i[3], i[4], i[5]))
        a = a + 1
    mydb.commit()
    root.mainloop()
    
def ShowBooksA():
    root = Tk()

    root.title('Library Management System')
    root.resizable(False, False)


    canvas = Canvas(
    root,
    bg = "#fff",
    height = 500,
    width = 820,
    bd = 0,
    highlightthickness = 0,
    )

    canvas.pack()

    def Back():
        root.destroy()
        d.DashboardAdmin()

    

    style = ttk.Style()
    style.configure("Treeview", rowheight = 30, rowwidth = 100)

    background = ImageTk.PhotoImage(Image.open(r"Images\New BG.jpg"))
    rect = ImageTk.PhotoImage(Image.open(r"Images\New Rect.png"))
    canvas.create_image(0, 0, image = background, anchor = NW)
    canvas.create_image(0, 23, image = rect, anchor = NW)


    canvas.create_text(145, 65, text = "Show Books -", font=('Poppins', 30, 'bold'), fill="#fff")

    tree = ttk.Treeview(root)
    
    tree.place(x=40,y=110)
    
    verscrlbar = ttk.Scrollbar(root,orient ="vertical",command = tree.yview)
    
    verscrlbar.place(x=790,y=250)
    
    tree.configure(xscrollcommand = verscrlbar.set)
    
    tree["columns"] = ("1", "2", "3", "4", "5", "6")
    
    tree['show'] = 'headings'
    
    tree.column("1", width = 50, anchor = CENTER)
    tree.column("2", width = 150, anchor = CENTER)
    tree.column("3", width = 150, anchor = CENTER)
    tree.column("4", width = 150, anchor = CENTER)
    tree.column("5", width = 150, anchor = CENTER)
    tree.column("6", width = 90, anchor = CENTER)
    
    tree.heading("1", text ="Book Id")
    tree.heading("2", text ="Book Name")
    tree.heading("3", text ="Book Description")
    tree.heading("4", text ="Book Category")
    tree.heading("5", text ="Book Author")
    tree.heading("6", text ="Book Quantity")


    BackBtn = Button(root, text = "Go Back", font=('Poppins', 10, 'bold'), bd = 0, width=10, command = Back)
    BackBtn.place(x = 650, y = 450)

    query = "select * from book;"
    cursor.execute(query)
    a = 0
    for i in cursor:
        tree.insert('', a, text = "", values = (i[0], i[1], i[2], i[3], i[4], i[5]))
        a = a + 1
    mydb.commit()
    root.mainloop()  

def IshueeBookWindow():
    rootI = Tk()

    rootI.title('Library Management System')
    rootI.resizable(False, False)

    
    canvas = Canvas(
    rootI,
    bg = "#fff",
    height = 400,
    width = 400,
    bd = 0,
    highlightthickness = 0,
    background = "#fff"
    )

    canvas.pack()

    def pic_date(event):
        global cal, window
        window = Toplevel()
        window.grab_set()
        window.title("Choose Date")
        window.geometry("250x220+590+370")
        window.resizable(False, False)
        cal = Calendar(window, selectmode = "day", date_pattern = "DD/MM/YYYY")
        cal.place(x=0,y=0)
        Btn = Button(window, bd = 0, text = "Submit", bg = "#101010", fg = "#fff", command = grab_date)
        Btn.place(x=100, y=190)

    def grab_date():
        RDate.delete(0, END)
        RDate.insert(0, cal.get_date())
        window.destroy()


    def CheckDetails():
        i = IDate.cget("text")
        r = RDate.get()
        Bname = BookName.cget("text")
        Aname = AuthorName.cget("text")
        if(r == ("dd/mm/yyyy")):
            messagebox.showerror("Error", "Pic Return Date First !")
        else:
            s = str(l.StudentName).replace(",", "").replace("(","").replace(")", "").replace("'", "")
            b = IBookName
            Id = i
            Rd = r
            query = "insert into ishueedbooks(studentname, Bookname, ishueeddate, returndate) values('" + s + "', '" + b + "', '" + Id + "', '" + Rd + "');"
            cursor.execute(query)
            cursor.execute("set @num := 0;")
            cursor.execute("update ishueedbooks set id = @num := (@num + 1);")
            count = None
            temp = None
            a = "Select quantity from book where name = '" + Bname +  "' and author = '" + Aname + "';"
            cursor.execute(a)
            for i in cursor:
                count = i

            temp = str(count).replace("(","").replace(")","").replace(",", "")
            temp = int(temp) - 1

            q = "update book set quantity = '" + str(temp) + "' where name = '" + Bname +  "' and author = '" + Aname + "';"
            cursor.execute(q)

            mydb.commit()
            messagebox.showinfo("Success", "Book Ishueed Successfully")
            rootI.destroy()




    canvas.create_text(90, 30, text = "Book Name -", font=('Poppins', 12), fill="#000")
    canvas.create_text(90, 90, text = "Book Author -", font=('Poppins', 12), fill="#000")
    canvas.create_text(90, 150, text = "Ishueed Date -", font=('Poppins', 12), fill="#000")
    canvas.create_text(90, 210, text = "Return Date -", font=('Poppins', 12), fill="#000")

    BookName = Label(rootI, font=('Poppins', 12, 'bold'), bd = 0,bg = "#fff",fg = "#101010")
    BookName.place(x = 150, y = 15)
    
    AuthorName = Label(rootI, font=('Poppins', 12, 'bold'), bd = 0,bg = "#fff",fg = "#101010")
    AuthorName.place(x = 150, y = 75)
    
    IDate = Label(rootI, font=('Poppins', 12, 'bold'), bd = 0, bg = "#fff", fg = "#000")
    IDate.place(x = 150, y = 135)
    
    RDate = Entry(rootI, font=('Poppins', 12, 'bold'), bd = 0, bg = "#fff", fg = "#000")
    RDate.place(x = 150, y = 195)

    RDate.insert(END, "dd/mm/yyyy")

    d = dt.datetime.now()
    Date = d.strftime('%d/%m/%Y')

    IDate.config(text = Date)
    BookName.config(text = IBookName)
    AuthorName.config(text = IAuthorName)

    RDate.bind("<Button-1>", pic_date)

    SubmitBtn = Button(rootI, text = "Submit", font=('Poppins', 9, 'bold'), bd = 0,bg = "#000",fg = "#fff", width = 10, command = CheckDetails)
    SubmitBtn.place(x = 150, y = 350)

    rootI.mainloop()

    rootI.wm_attributes("-topmost", True)
    rootI.grab_set()

def IshueeBooks():
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

    def Back():
        root.destroy()
        d.DashboardStudent()

    def CheckDetails():
        global IBookName, IAuthorName
        IBookName = name.get()
        IAuthorName = author.get()
        if((IBookName and IAuthorName) == ""):
            messagebox.showerror("Error","Please Fill Details First!!!")
        else:
            query = "select name, author from book where name = '" + IBookName + "' and author = '" + IAuthorName + "';"
            cursor.execute(query)

            data = ()
            quantity = 0
            temp = 0

            for i in cursor:
                data = i
 
            query2 = "select quantity from book where name = '" + IBookName + "';"
            cursor.execute(query2)

            for a in cursor:
                quantity = a
            
            temp = str(quantity).replace("(","").replace(")","").replace(",","")

            if(int(temp) > 0):
                if((IBookName, IAuthorName) != data):
                    messagebox.showerror("Error","The Book are not available")
                else:
                    IshueeBookWindow()
            else:
                messagebox.showerror("Data Error","The Book you choose in not available right now,In some days book will be available")




    background = ImageTk.PhotoImage(Image.open("Images\Background.jpg"))
    rect = ImageTk.PhotoImage(Image.open("Images\Rectangle.png"))
    canvas.create_image(0, 0, image = background, anchor = NW)
    canvas.create_image(0, 23, image = rect, anchor = NW)
    canvas.create_text(145, 65, text = "Ishuee Books", font=('Poppins', 30, 'bold'), fill="#fff")

    canvas.create_text(145, 200, text = "Book Name -", font=('Poppins', 12), fill="#fff")
    canvas.create_text(145, 260, text = "Book Author -", font=('Poppins', 12), fill="#fff")

    name = Entry(root, font=('Poppins', 10), fg = "#101010", width = 40)
    name.place(x = 240, y = 183)
    name.focus()
    
    author = Entry(root, font=('Poppins', 10), fg = "#101010", width = 40)
    author.place(x = 240, y = 243)
    
    
    SubmitBtn = Button(root, text = "Submit", font=('Poppins', 10, 'bold'), bd = 0, width=10, command = CheckDetails)
    SubmitBtn.place(x = 340, y = 450)

    BackBtn = Button(root, text = "Go Back", font=('Poppins', 10, 'bold'), bd = 0, width=10, command = Back)
    BackBtn.place(x = 550, y = 450)

    root.mainloop()

def ReturnIshueeBooks():

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

    def CheckDetails():
        n = BookName.get()
        a = ishueeddate.get()
        if((n and a) == ""):
            messagebox.showerror("Error","Please Fill Details First!!!")
        elif("/" not in a):
            messagebox.showerror("Error","Date Is Incorrect")
        else:

            data = ()
            query2 = "select Bookname, ishueeddate from ishueedbooks where Bookname = '" + n + "' and ishueeddate = '" + a + "' and studentname = '" + str(l.StudentName).replace("(", "").replace(")", "").replace(",","").replace("'","") + "';"
            cursor.execute(query2)

            for i in cursor:
                data = i

            if((n, a) != data):
                messagebox.showwarning("Error", "Book not Found Try Again :)")
            else:
                q = "delete from ishueedbooks where Bookname = '" + n + "';"
                cursor.execute(q)
                count = None
                temp = None
                x = "Select quantity from book where name = '" + n + "';"
                cursor.execute(x)
                for i in cursor:
                    count = i

                temp = str(count).replace("(","").replace(")","").replace(",", "")
                temp = int(temp) + 1


                q = "update book set quantity = '" + str(temp) + "' where name = '" + n + "';"
                cursor.execute(q)

                messagebox.showinfo("Successfull","Book Returned")

    def Back():
        root.destroy()
        d.DashboardStudent()

    background = ImageTk.PhotoImage(Image.open("Images\Background.jpg"))
    rect = ImageTk.PhotoImage(Image.open("Images\Rectangle.png"))
    canvas.create_image(0, 0, image = background, anchor = NW)
    canvas.create_image(0, 23, image = rect, anchor = NW)
    canvas.create_text(240, 65, text = "Return Ishueed Books", font=('Poppins', 30, 'bold'), fill="#fff")

    canvas.create_text(145, 200, text = "Book Name -", font=('Poppins', 12), fill="#fff")
    canvas.create_text(145, 260, text = "Ishueed Date -", font=('Poppins', 12), fill="#fff")

    BookName = Entry(root, font=('Poppins', 10), fg = "#101010", width = 40)
    BookName.place(x = 240, y = 183)
    BookName.focus()
    
    ishueeddate = Entry(root, font=('Poppins', 10), fg = "#101010", width = 40)
    ishueeddate.place(x = 240, y = 243)
    
    
    SubmitBtn = Button(root, text = "Submit", font=('Poppins', 10, 'bold'), bd = 0, width=10, command = CheckDetails)
    SubmitBtn.place(x = 340, y = 450)

    BackBtn = Button(root, text = "Go Back", font=('Poppins', 10, 'bold'), bd = 0, width=10, command = Back)
    BackBtn.place(x = 550, y = 450)

    root.mainloop()
    
def CheckDue():
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

    def Back():
        root.destroy()
        d.DashboardStudent()

    

    style = ttk.Style()
    style.configure("Treeview", rowheight = 30, rowwidth = 100)

    background = ImageTk.PhotoImage(Image.open(r"Images\Background.jpg"))
    rect = ImageTk.PhotoImage(Image.open(r"Images\Rectangle.png"))
    canvas.create_image(0, 0, image = background, anchor = NW)
    canvas.create_image(0, 23, image = rect, anchor = NW)


    canvas.create_text(170, 65, text = "Ishueed Books -", font=('Poppins', 30, 'bold'), fill="#fff")

    tree = ttk.Treeview(root)
    
    tree.place(x=100,y=110)
    
    verscrlbar = ttk.Scrollbar(root,orient ="vertical",command = tree.yview)
    
    verscrlbar.place(x=610,y=250)
    
    tree.configure(xscrollcommand = verscrlbar.set)
    
    tree["columns"] = ("1", "2", "3", "4")
    
    tree['show'] = 'headings'
    
    tree.column("1", width = 50, anchor = CENTER)
    tree.column("2", width = 150, anchor = CENTER)
    tree.column("3", width = 150, anchor = CENTER)
    tree.column("4", width = 150, anchor = CENTER)
    
    tree.heading("1", text ="Id")
    tree.heading("2", text ="Book Name")
    tree.heading("3", text ="Book Ishuee Date")
    tree.heading("4", text ="Book Return Date")


    BackBtn = Button(root, text = "Go Back", font=('Poppins', 10, 'bold'), bd = 0, width=10, command = Back)
    BackBtn.place(x = 550, y = 450)

    query = "select id, Bookname, ishueeddate, returndate from ishueedbooks where studentname = '" + str(l.StudentName).replace("'","").replace("(","").replace(")","").replace(",","") + "';"
    cursor.execute(query)
    a = 0
    for i in cursor:
        tree.insert('', a, text = "", values = (i[0], i[1], i[2], i[3]))
        a = a + 1
    mydb.commit()

    root.mainloop()
    




    


