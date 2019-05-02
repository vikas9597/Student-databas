import modsql as ms
import tkinter as tk

mainWindow = tk.Tk()
mainWindow.title = ("Student database")
heading_label = tk.Label(mainWindow, text="Database Entry")
heading_label.pack()

l1=tk.Label(mainWindow, text="Enter Name")
l1.pack()
n = tk.Entry(mainWindow)
n.pack()

l2=tk.Label(mainWindow, text="Enter Collage")
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
    collage = c.get()
    id = i.get()
    phone = p.get()
    address = a.get()
    ms.data_add(name,collage,id,phone,address)

def ret():
    cursor = ms.data_ret()
    for row in cursor:
        print("Student id is: ", row[0])
        print("Student name is: ", row[1])
        print("Student collage is: ", row[2])
        print("Student phone is: ", row[3])
        print("Student address is: ", row[4])


button1 = tk.Button(mainWindow, text="Database Entry", command=lambda: add())
button1.pack()

button2 = tk.Button(mainWindow, text="Retrieve Data", command=lambda: ret())
button2.pack()

mainWindow.mainloop()