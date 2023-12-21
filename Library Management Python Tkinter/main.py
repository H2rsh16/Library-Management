from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from login import *

root = Tk()

root.title('Library Management System')
root.resizable(False, False)

def LoginAdmin():
    root.destroy()
    LoginAsAdmin() 

def LoginStudent():
    root.destroy()
    LoginAsStudent()

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

canvas.create_text(350, 156, text = "Wellcome to Library!!", font=('Poppins', 40, 'bold'), fill="#fff")

Btn_1 = Button(root, text = 'Admin', fg="#fff", background = '#6E91EA', font=('Poppins', 15), width = 9, command = LoginAdmin)
Btn_1.place(x=197,y=276)

Btn_2 = Button(root, text = 'Student', fg="#fff", background = '#6E91EA', font=('Poppins', 15), width = 9, command = LoginStudent)
Btn_2.place(x=385,y=276)

root.mainloop()
