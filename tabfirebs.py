import tkinter as tk
import firemod as fm


mainWindow = tk.Tk()
mainWindow.title = ("Student database")
heading_label = tk.Label(mainWindow, text="Database Entry")
heading_label.pack()

l1=tk.Label(mainWindow, text="Enter Name")
l1.pack()
n = tk.Entry(mainWindow)
n.pack()

l2=tk.Label(mainWindow, text="Enter Course")
l2.pack()
c =tk.Entry(mainWindow)
c.pack()

l3=tk.Label(mainWindow, text="Enter id")
l3.pack()
i =tk.Entry(mainWindow)
i.pack()

l4=tk.Label(mainWindow, text="Enter phone")
l4.pack()
p =tk.Entry(mainWindow)
p.pack()

l5=tk.Label(mainWindow, text="Enter Address")
l5.pack()
a =tk.Entry(mainWindow)
a.pack()

def add():
    name = n.get()
    course = c.get()
    id = i.get()
    phone = p.get()
    address = a.get()
    fm.data_add(name, course, id, phone, address)

def ret():
    students_record =fm.data_ret()
    for student in students_record.each():
        record = student.val()
        print("Student name is: ", record['name'])
        print("Student course is: ", record['course'])
        print("Student id is: ", record['id'])
        print("Student phone is: ", record['phone'])
        print("Student address is: ", record['address'])

button1 = tk.Button(mainWindow, text="Database Entry", command=lambda: add())
button1.pack()

button2 = tk.Button(mainWindow, text="Retrieve Data", command=lambda: ret())
button2.pack()

mainWindow.mainloop()