from tkinter import *

root = Tk()

# Name_box = Label(root, text='Enter your name !')
# Name_box.pack()


e = Entry(root, width=50, bg="blue", fg="white", borderwidth=5,)
e.pack()
e.insert(0, "Enter you name")

def my_Click():
    hello = "hello " + e.get()
    my_Label = Label(root, text=hello)
    my_Label.pack()


My_Button = Button(root, text="Submit", command=my_Click)

My_Button.pack()

root.mainloop()